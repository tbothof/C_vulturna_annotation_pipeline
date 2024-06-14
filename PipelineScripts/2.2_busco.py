#In this script, there is an loop to run Busco over all the 15 assembly's
import subprocess
import sys
import os

#This function extracts the fasta files form the flye output dir and loops over it with Busco
def busco(Dir, files, output_dir):
    for item in annotation_files:
        file = Dir + item + "/" + "assembly.fasta"
        output = output_dir + item
        subprocess.run(["busco", "-i", file, "-m", "genome", "-l", "saccharomycetes_odb10", "-o", output])


#Regulate input
if len(sys.argv) < 2:
    print("Please provide 1: an dir with the output files from the flye assembly and 2: an dir where the output Busco files are made")
else:
    annotation_dir = sys.argv[1]
    annotation_files = os.listdir(sys.argv[1])
    Output_dir = sys.argv[2]
    annotation_files.sort()
    busco(annotation_dir, annotation_files, Output_dir)

