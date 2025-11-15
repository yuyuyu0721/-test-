#python_luogu_p2669
k=int(input())
total=0
i=1
while k>0:
    days=min(k,i)#
    total+=days*i
    k-=days

    i+=1
