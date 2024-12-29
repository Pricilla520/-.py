import time
def GCD(p,q):
    i=q
    while p%i!=0 or q%i!=0:
        i=i-1
    return i

def GCD1(p,q):
    while p%q!=0:
        p,q=q,p%q
    return q

start=time.time()
gcd=GCD(192704808,11335577)
end=time.time()
print(end-start)
print(gcd)

start=time.time()
gcd1=GCD1(192704808,11335577)
end=time.time()
print(end-start)
print(gcd1)