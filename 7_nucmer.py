import glob
import subprocess


##This creates the directory in which the graphs will be stored. Change the name by simply replacing "nucmergraphs".##
subprocess.run(['mkdir', './nucmergraphs'])


##Since nucmer uses one file as a reference to compare other files with, we grab a referencefile here.##
##This should be changed depending on the phylogenetic tree.##
##The second line simply uses glob to get all other files. This is dependent on the location of the assembly files.##
referencefile = "/mnt/studentfiles/2024/2024MBI10/vulturna/assembly2/modifiedassembly/bc14_IHEM26071_Q10_fltr/assembly.fasta"
queryfile = glob.glob('./assembly2/modifiedassembly/bc*/assembly.fasta')

##Here we compare every globbed file with the reference file.##
##output1 should be changed to reflect which file is being used as a reference (in this case bc14).##
for file in queryfile:
    output1 = file.replace('./assembly2/modifiedassembly/', './nucmergraphs/bc14_vs_')
    finaloutput = output1.replace('/assembly.fasta', '.png')
    print(finaloutput)
    subprocess.run(['nucmer', referencefile, file])
    subprocess.run(['mummerplot','--png',  './out.delta'])
    subprocess.run(['mv', './out.png', finaloutput])
