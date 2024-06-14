#In this script, there is an loop to run quast over all the 15 assembly's
import subprocess
import sys
import os

#This function extracts the fasta files form the flye output dir and the fastq reads dir and loops over it with Quast
def quast(annotation_dir, annotation_files, fastq_files):
    i = 0
    test = []
    for item in annotation_files:
        file = annotation_dir + item + "/" + "assembly.fasta"
        subprocess.run(["quast.py", "--nanopore", fastq_files[i], "--fungus", file, "-o", item])
        i += 1


#Regulate input
if len(sys.argv) < 2:
    print("Please provide an 1: dir with the output files from the flye assembly and 2: an dir with fastq reads")
else:
    annotation_dir = sys.argv[1]
    annotation_files = os.listdir(sys.argv[1])
    annotation_files.sort()

    fastq_dir = sys.argv[2]
    fastq_files = os.listdir(sys.argv[2])

    fastq_files2 = []
    for item in fastq_files:
        fastq_files2.append(fastq_dir + item)
    fastq_files2.sort()

    quast(annotation_dir, annotation_files, fastq_files2)

