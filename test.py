def gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b) 
'''

p=int(input("p= "))
q=int(input("q= "))
e=int(input("e= "))
M=int(input("M= "))

N=p*q
print("N= ",N)

r=(p-1)*(q-1)
print("r= (p-1)(q-1) = ",r)
print("gcd(r,e)= ",gcd(r,e))
d=0
for i in range(r):
    tmp=e*i
    if(tmp%r == 1):
        d=i
        print("d= ",i)
        break
print("Public Key= {e,N}= {",e,",",N,"}")
print("Private Key= {d,N}= {",d,",",N,"}")

print("encryption:")
C=1
for j in range(e):
    C=C*M
C=C%N
print("C = M^e mod N =  ",C)

print("decription:")
Mm=1
for j in range(d):
    Mm=Mm*C
Mm=Mm%N
print("M = C^d mod N =  ",Mm)
'''
#==============
C=1
for j in range(59):
    C=C*61
C=C%91
print("C = M^e mod N =  ",C)
#==================

d=0
for i in range(4620):
    tmp=47*i
    if(tmp%4620 == 1):
        d=i
        print("d= ",i)
        break
        
        
        
        



