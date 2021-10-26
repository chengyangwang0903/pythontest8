shuzi=[]
zimu=[]
def numlist(l):
    for i in range(1,l):
        shuzi.append(i)
def charlist(k=[]):
    for i in k:
        zimu.append(chr(i+96))
a=27
numlist(a)
charlist(shuzi)
dir={}
for x in range(len(shuzi)):
    dir[shuzi[x]]=zimu[x]
print(dir)

