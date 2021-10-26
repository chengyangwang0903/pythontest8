def pingfang(n):
    return n*n
def list_prime(x):
    s=0
    for i in range(2,x+1):
        if(x%i==0):
            s+=1
    if s==1:
        return 1
    else:
        return 0
num=[]
sum=0
while 1:
    x=eval(input())
    if(list_prime(x)==1):
        sum=sum+pingfang(x)
        num.append(x)
    else:
        break
print(sum)
print(num)