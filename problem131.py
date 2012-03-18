def primes(n):
    s=range(0,n+1)
    s[1]=0
    bottom=2
    top=n//bottom
    while (bottom*bottom<=n):
        while (bottom<=top):
            if s[top]:
                    s[top*bottom]=0
            top-=1
        bottom+=1
        top=n//bottom
    return [x for x in s if x]

def is_perfect_cube(n):
    if n ** (1/3)

all_primes = primes(1000000)
