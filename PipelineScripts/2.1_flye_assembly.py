import glob
import subprocess

##This creates a directory in which the assemblies will be stored. Change the second argument as needed to change directory name.##
subprocess.run(["mkdir", "./assemblyoutput"])


##This uses glob to grab all files in a rawdata directory ending in fastq.gz, AKA gzipped fastq files. Change the part after * to change##
## the file type used. Flye accepts both gzipped and unzipped files.##
sequences = glob.glob('./rawdata/*.fastq.gz')

##This uses one of the properties of glob to loop over every selected file, AKA the raw reads.##
for file in sequences:

##Here we prepare the directories we will be placing the complete assembly and corresponding files in. The names it uses for these are dependent##
## on the names of the original read files. These names are also used for all the other parts of the pipeline, so choose them carefully.##
##The original files all started with bc..., so use this for convenience.##
    interfile = file.replace("rawdata/", "")
    dirname = interfile.replace(".fastq.gz","")
    outputdir = f'./assemblyoutput/{dirname}'
    subprocess.run(['mkdir', outputdir])

#Now we just run Flye on every single file.##
#We use --nano-corr, because these reads have been filtered.##
##Flye has other options for specific filtering options. Check https://github.com/fenderglass/Flye/blob/flye/docs/USAGE.md for details##

    subprocess.run(['flye','--scaffold', '--nano-corr', file, '-o', outputdir])

