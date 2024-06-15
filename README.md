# C_vulturna_annotation_pipeline
This is the repository containing the different parts of the pipeline we devised to assemble and annotate Nanopore reads from C. vulturna on behalf of Westerdijk Fungal Biodiversity Institute.

The different steps are named and numbered. The first step should be creating environments for and downloading the different tools.

## 1_tool_install.sh
This is a bash script that should install all the tools and dependencies you'll need in the pipeline. This does require conda.
If conda is installed, it's simply a matter of running "bash 1_tool_install.sh"

## 2.1_flye_assembly.py
This runs Flye, with scaffolding, on every fastq.gz file in a directory called rawdata/.
This can be changed if need be. The script is annotated to show where to change.

## 2.2_busco.py
An optional step. Simply runs busco on all assemblies.
Gives stats on the quality of the assembly.

## 2.3_quast.py
Again, optional. More quality control.

## 3_augustus.py
This script runs Augustus to perform gene annotation, focused on protein-coding sequences. It outputs gff-files, with some extra data in comments.
These are all put in a collective directory, with named directories within this for each assembly.

## 4_AA_extraction.sh
A small bash script to extract the amino acid sequences provided by Augustus, since we'll be using them later down the line.
Uses the file getAnnoFasta.pl, as provided by https://rnnh.github.io/bioinfo-notebook/docs/augustus.html.

Note: May have some trouble running in byobu. Simply exiting byobu should do the trick. Don't worry, it doesn't take long at all.
If it still doesn't work, you'll have to run each file separately.

## 5_hmmsearch.py
This script uses hmmsearch to identify the amino acid sequences. It allows for the input of the directory where the AA-sequences are located, the location of the PFam database and the directory for the output.

Note: The Pfam database for this needs to be downloaded separately. Available at : https://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.hmm.gz

## 6_orthofinder.py
This script runs Orthofinder on the output files of augustus. It puts them in a separate folder first. This should also contain your out-group files (such as the 3 included in this repo). By default, the phylogenetic tree is based on the STAG method, but it includes options to change this. "orthofinder -h" will get you a list of the customizable options.

## 7_nucmer.py
This uses nucmer, a program from MUMmer, to make MSA graphs, showing inversions in the sequences. It uses one reference file and any amount of query files. The reference file should be chosen based on the phylogenetic tree from Orthofinder.

## 8_*.py
These 3 scripts are pure file-parsing. They should be run in sequence (1-2-3, for those that might still have difficulty with this). 8.1 simply removes the comments from the augustus output, preparing them for a nice merge with the files from hmmsearch. 8.2 removes spaces from the hmmsearch output files, replacing them with tabs, for ease of use. 8.3 then takes both of these files, reads the lines and combines them. It takes the protein function and PFam accession number from hmm, and adds it to the first line corresponding to that gene. This is all written to a new file, giving a final file containing all protein sequences Augustus could detect, along with their function, so long as it's available in Pfam.

# General Notes:
Some of these tools can take quite a while to run. If working from a pc connected to a server, it's advisable to run them on byobu. This will make sure the programs keep running even if your device disconnects from the server.

# Acknowledgements:
None of these tools were made by us. We're infinitely grateful to all the people that did make them. Provided below are the names of these tools and the links to their respective github pages:

Flye:
https://github.com/fenderglass/Flye

Busco:
https://github.com/metashot/busco

Quast:
https://github.com/ablab/quast

Augustus:
https://github.com/Gaius-Augustus/Augustus?tab=readme-ov-file

Hmmer:
https://github.com/EddyRivasLab/hmmer?tab=readme-ov-file

Orthofinder:
https://github.com/davidemms/OrthoFinder?tab=readme-ov-file

MUMmer:
https://github.com/mummer4/mummer
