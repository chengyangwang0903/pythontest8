def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
def sum(m):
    result=0
    for i in range(1,m+1):
        result+=fact(i)
    return result
n=eval(input("请输入一个数："))
print(sum(n))