import glob
import subprocess

##We start by creating a directory for Orthofinder, which will contain the assemblies and the output for Orthofinder.##
subprocess.run(['mkdir', 'orthofinder'])

##Get all the right files with glob! This is dependent on file names and locations for the assemblies but can be changed.##
fastas = glob.glob('./augustusoutput/bc*/proteinseqs.fasta')
for file in fastas:

#Here we copy the assembly files to the same folder, each named after their respective strains, which is required for orthofinder.##
    newname = file.replace("./augustusoutput/", "./orthofinder/" )
    newername = newname.replace("/", "_")
    name3 = newername.replace("_b", "/b")
    name5 = name3.replace("._", "./")

    subprocess.run(["cp", file, name5])

##Finally, we run orthofinder.##
subprocess.run(["orthofinder", "-f", "./orthofinder"])
