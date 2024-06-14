import glob
import subprocess

##We start by selecting all our augustus files and making a directory to store our cleaned-up gffs in.##
augustusfiles= glob.glob('./augustusoutput/*/augustus_output.gff')
subprocess.run(['mkdir', './cleangff'])


##Here we go over every selected file, first making a new name for the file, consisting only of the name of the original raw data and .gff.##

for file in augustusfiles:
    intermediate= file.replace('./augustusoutput/','./cleangff/')
    cleanfile= intermediate.replace('/output_new.gff', '.gff')
##Here we read the contents of the original file. If it starts with a #, it doesn't get written to a new file. If it doesn't, it's added to the file.##
    with open(file, 'r') as handle:
        lines =  handle.readlines()
    with open(cleanfile, 'w') as handle:
        for line in lines:
            if not line.startswith('#'):

                handle.write(line)
