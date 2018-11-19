#!/usr/local/bin/python/


def openfile(filename):
    with open(filename + ".txt", "r") as f:
        lines = f.readlines()
    return lines


md5 = []
sha256 = []
sha512 = []
PBK256 = []
argon = []
DES = []
alph_index = []
length_index = []
num_index = []


with open("hashes.plotfile", "r") as f:
    lines = f.readlines()
for line in lines:
    if "$1$" in line:
        md5.append(line.split(":")[-1].rstrip("\r\n"))
    if "$5$" in line:
        sha256.append(line.split(":")[-1].rstrip("\r\n"))
    if "$6$" in line:
        sha512.append(line.split(":")[-1].rstrip("\r\n"))
    if "sha256:29000:" in line:
        PBK256.append(line.split(":")[-1].rstrip("\r\n"))
    if "$argon2i$" in line:
        argon.append(line.split(":")[-1].rstrip("\r\n"))
    else:
        DES.append(line.split(":")[-1].rstrip("\r\n"))

dr_alph = dict(enumerate(openfile("rockyou_alph")))
#r_length = dict(enumerate(openfile("rockyou").sort(lambda x, y: cmp(len(x), len(y)))))
dr_num = dict(enumerate(openfile("rockyou_num")))
drockyou = dict(enumerate(openfile("rockyou")))

r_num = dict((v, k) for k, v in dr_num.iteritems())
r_alph = dict((v, k) for k, v in dr_alph.iteritems())
rockyou = dict((v, k) for k, v in drockyou.iteritems())

for item in md5:
    if item + '\n' in r_alph.keys():
        print(item)
        print(r_alph[item + '\n'])
        num_index.append(r_alph[item + '\n'])

print(len(md5))
print(num_index)


#for key in r_alph.keys():
#    for item in md5:
#        if item == r_alph[key]:
#            print(r_alph[key] + ": " + str(key))


#for item in md5:
#    for val, key in r_alph:
#        if item in val:
#            print (item + ": " + r_alph[val])
#            alph_index.append(r_alph[val])

#for item in md5:
#    for val, key in rockyou:
#        if item in val:
#            print (item + ": " + rockyou[val])
#            alph_index.append(rockyou[val])




#for item in md5:
#    if item in r_length:
#        print (item + ": " + r_length[item])
#        length_index.append(r_length[item])

#for item in md5:
#    for val, key in r_num:
#        if item in val:
#            print (item + ": " + r_num[val])
#            num_index.append(r_num[val])


#for item in DES:
#    if item in r_length:
#    print (item + ": " + r_length[item])
#   length_index.append(r_length[item])


#for item in DES:
#    for val, key in r_alph:
#        if item in r_alph:
#            print (item + ": " + r_alph[val])
#            alph_index.append(r_alph[val])

