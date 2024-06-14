##In this script, there is a loop to run the hmmsearch over protein sequences.##
import subprocess
import sys
import os

##This function extracts the protein sequences from the augustus ouput dir and loops over it with hmmsearch.##
def hmm_search(seq_dir, seq_files, pfam, output_dir):
    for item in seq_files:
        file = seq_dir + item + "/" + "proteinseqs.fasta"
        output = output_dir + item
        subprocess.run(["hmmsearch", "--tblout", output, "--cut_tc", pfam, file])

##Regulate input.##
if len(sys.argv) < 2:
    print("Please provide 1: an dir with the augustus output files 2: the path to the pfam database and 3: an dir where the output hmmsearch files are made")
else:
    seq_dir = sys.argv[1]
    seq_files = os.listdir(sys.argv[1])
    seq_files.sort()
    pfam = sys.argv[2]
    output_dir = sys.argv[3]
    hmm_search(seq_dir, seq_files, pfam, output_dir)
