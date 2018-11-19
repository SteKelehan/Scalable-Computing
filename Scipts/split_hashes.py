import sys

File = sys.argv[1]
md5 = "md5.hashes"
sha256 = "sha256.hashes"
sha512 = 'sha512.hashes'
PBk256 = "PBK256.hashes"
argon = "argon.hashes"
DES = "DES.hashes"

with open(File, "r") as f:
    lines = f.readlines()
for line in lines:
    if "$1$" in line:
        with open(md5, "a") as f:
            f.write(line + "\n") 
    if "$5$" in line:
        with open(sha256, "a") as f1:
            f1.write(line + "\n") 
    if "$6$" in line:
        with open(sha512, "a") as f2:
            f2.write(line + "\n") 
    if "sha256:29000:" in line:
        with open(PBk256, "a") as f3:
            f3.write(line + "\n") 
    if "$argon2i$" in line:
        with open(argon, "a") as f4:
            f4.write(line + "\n") 
    else:
        with open(DES, "a") as f5:
            f5.write(line + "\n")


f.close()
f1.close()
f2.close()
f3.close()
f4.clsoe()
f5.close()

