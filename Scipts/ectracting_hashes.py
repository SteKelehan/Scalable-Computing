import sys


File = sys.argv[1]
File2 = sys.argv[2]
File3 = sys.argv[3]
Dict = {}
HDict = {}

with open(File, "r") as f:
    hashes = [line.rstrip() for line in f]
f.close()

with open(File2, "r") as f:
    broken = [line.rstrip() for line in f]
f.close()

with open(File3, "r") as f:
    missmatch = [line.rstrip() for line in f]
f.close()

for var in broken:
    var1, var2 = var.split(" ")[0], var.split(" ")[-1]
    Dict[var1] = var2


with open("kelehans.hashes_mine", "w") as f:
    for var in hashes:
        if var in Dict.keys():
            f.write(var + " " + str(Dict[var]) + "\n")    
f.close()


with open("kelehans.notcracked", "w") as f:
    for var in missmatch:
        f.write(var.split(" ")[0] + "\n")
    for var in hashes:
        if var not in Dict.keys():
            f.write(var + "\n")

f.close()



#print("contentA: ")
#print(contentA)
#print("contentB: ")
#print(contentB)
