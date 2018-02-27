'''input
2
6 113 3
1 2 3 4 5 6
1 4
6 113 70
1 2 3 4 5 6
1 4 3
'''
n1=input()
from collections import defaultdict as df
def query(l,r,root=1):
    if r<L[root] or R[root]<l:
        return 1
    if l<=L[root] and r>=R[root]:
    	
        return seg[root]

    return  (query(l,r,root*2)*query(l,r,root*2+1))%p

for _ in range(n1):
    n,p,q=[int(x) for x in raw_input().split()]
    A=[int(x) for x in raw_input().split()]
    B=[int(x) for x in raw_input().split()]
    nn=1
    while nn<n:
    	nn*=2
    nn*=2

    seg=[1]*nn
    L=[9999999]*nn
    R=[-1]*nn
    for i in range(nn/2,nn):
        L[i]=i-nn/2
        R[i]=i-nn/2
        if i<nn/2+n:
        	seg[i]=A[i-nn/2]
    for i in range(nn-1,0,-1):
        L[i/2]=min(L[i],L[i/2])
        R[i/2]=max(R[i],R[i/2])
    	seg[i/2]=(seg[i/2]*seg[i])%p

 
    x=0
    #print seg
    for i in range(q):
 
        if i%64==0:
            l=(B[i/64]+x)%n
            r=(B[i/64 + 1]+x)%n
 
        else:
            l=(pl+x)%n
            r=(pr+x)%n
        l,r=sorted([l,r])
        pl,pr=l,r
        ans=query(l,r)
        #print ans,i,l,r
        #print x,i,l,r,ans,SA[r+1],SA[l]
        x=(ans+1)
 
    print x%p