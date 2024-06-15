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
