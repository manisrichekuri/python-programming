s=input().split()
g=0
for x in s:
    if(g<len(s)):
        if(g%2==0):
            s[g]=x[::-1]
            g=g+1
        else:
            g=g+1
v=" ".join(map(str,s))
print(v)
