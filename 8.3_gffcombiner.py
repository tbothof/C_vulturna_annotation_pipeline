import csv
import subprocess

##Give the file path to each input file here##
hmmfile = "/mnt/studentfiles/2024/2024MBI10/vulturna/hmmtsv/bc14_IHEM26071_Q10_fltr.tsv"
augustusgff = "/mnt/studentfiles/2024/2024MBI10/vulturna/cleangff/bc14_IHEM26071_Q10_fltr.gff"

##Here we're just setting up the output directory and##
##Make sure to change the name of the finalfile!!##
subprocess.run(['mkdir', './combinedoutput'])
outputfile = './tempoutput.csv'
finalfile = './combinedoutput/bc14_IHEM26071.gff'

##First, turning the hmmfile into a dictionary##
hmmdictionary = {}
with open(hmmfile, 'r') as handle:
    tsvhmm = csv.reader(handle, delimiter = '\t')
    for row in tsvhmm:
       hmmdictionary[row[0]] = [row[2], row[3]]

##And now for the difficult part##
##Essentially, this checks the augustus file for rows containing the word 'gene'##
##If this is present, it checks if the gene number is also present in hmmsearch's file##
##If so, it adds the correct gene info to the row and writes the row to a temporary file##
##If it does not have the word gene, or if the gene number isn't in hmmsearch, it writes the row as is##
with open(augustusgff, 'r') as tsvfile:
    augtsv = csv.reader(tsvfile, delimiter = '\t')
    for row in augtsv:
        if row[2] == 'gene':
            internumber = row[8].replace('ID=', '')
            genenumber = internumber + '.t1'
            if genenumber in hmmdictionary.keys():
               print(hmmdictionary[genenumber])
               newrow = row + hmmdictionary[genenumber]
               with open(outputfile, 'a') as handle:
                   writer = csv.writer(handle)
                   writer.writerow(newrow)

            else:
               with open(outputfile, 'a') as handleb:
                   writer = csv.writer(handleb)
                   writer.writerow(row)
        else:
            with open(outputfile, 'a') as handlec:
                writer = csv.writer(handlec)
                writer.writerow(row)

##Because this writes it as a csv, here we turn it into a tsv file and write it to a final file##

with open(outputfile, 'r') as handled:
    lines = handled.readlines()
    for line in lines:
        newline = line.replace(',', '\t')

        with open(finalfile, 'a') as output:
            output.write(newline)
subprocess.run(['rm', outputfile])



