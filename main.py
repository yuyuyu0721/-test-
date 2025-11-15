#题目要求：计算在k天内完成任务所需的总工作量   wao
k=int(input())
total=0
i=1
while k>0:
    days=min(k,i)#
    total+=days*i
    k-=days
    i+=1