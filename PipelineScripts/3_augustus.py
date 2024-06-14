import glob
import subprocess

##We start by creating a directory for all the sub-directories.##
subprocess.run(['mkdir', './augustusoutput'])

##Get all the right files with glob. This is dependent on file names and locations for the assemblies but can be changed.##
fastas = glob.glob('./assemblyoutput/bc*/assembly.fasta')
for file in fastas:

##Here we create all the subdirectories we will store the annotation files in.##
    interfile = file.replace("./assemblyoutput/", "")

    dirname = interfile.replace("/assembly.fasta","")

    outputdir = f'./augustusoutput/{dirname}'
    print(outputdir)
    subprocess.run(['mkdir', outputdir])

##And here it's just running augustus.##
##The name of the output files can be changed here in the "--outfile=" section and reference species in the "--species=" section.##
    subprocess.run(['augustus','--outfile=augustus_output.gff', '--gff3=on', '--species=candida_albicans', file])
    subprocess.run(['mv', 'augustus_output.gff', outputdir])

##After this, use the getAnnoFasta.pl file to extract the amino acid sequences, used for hmmsearch.##
print("Run the getAnnoFasta.pl file on the augustus output files to get the AA sequences.")
