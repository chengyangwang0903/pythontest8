square=lambda x:x*x
list_p=[]
def list_prime(l=[]):
    for i in l:
        s=0
        if i<=1:
            s=0
        for j in range(2,i+1):
            if(i%j==0):
                s+=1
        if s==1:
            list_p.append(i)
    return list_p
input_num=input("请输入一组数字，用逗号隔开：")
num=input_num.split(",")
num=map(int,num)
sum=0
for i in list_prime(num):
    sum+=square(i)
print(list_prime(num))
print(sum)
