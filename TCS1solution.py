l=[-1,60,20,100,78,98]
d=dict()
p=1
for i in range(len(l)):
    if(i == len(l)-1):
#         print(i)
        p=l[i-1] * l[0]
        d[i] = p
#         print(p)
    else:
#         print(i)
        p=l[i-1] * l[i+1]
#         print(p)
        d[i] = p
#         print(d)
    p=1
print(l[max(d, key= lambda x: d[x])])