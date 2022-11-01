from multiprocessing.sharedctypes import Value


def sumofnumbers(sha):
    sum=0
    while(sha>0):
        rem=sha % 10
        sum=sum +(rem**3)
        sha=sha//10
        return sum
Valuetocheck=132
x=sumofnumbers(Valuetocheck)
if Valuetocheck==x:
    print("armstrng")
else:
 print("no armstrng")