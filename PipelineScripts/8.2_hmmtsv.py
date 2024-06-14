import glob
import subprocess

##So, hmmsearch pretends to make tsv-files. They look similar but they're not.##
##They're actually separated by some amount of spaces. This script fixes this, to prepare for the merge with the augustus files.##

##We grab the right files with glob. Again, these directory names may vary based on earlier changes made by the user.##
##Subprocess is only here to make another directory. There's a lotta those but it makes it easier to work with.#3

hmmfiles= glob.glob('./hmmsearch_out/bc*')
subprocess.run(['mkdir', './hmmtsv'])


for file in hmmfiles:
##We start by making new names for the output files.##
    intermediate= file.replace('./hmmsearch_out/','./hmmtsv/')
    tsvfile= intermediate + '.tsv'

##From here, we start with fixing the table. Every line is read, spaces are removed and then replaced by tabs.##
##This is then written to the new file.##
    with open(file, 'r') as output:
        lines =  output.readlines()
    with open(tsvfile, 'w') as handle:
        for line in lines:
            if not line.startswith('#'):
                newline = '\t'.join(line.split())
                handle.write(f'{newline}\n')

