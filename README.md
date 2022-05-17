# cryptoScript
usefull script about crypto attack



### Interger nth root for huge number
```py
def integer_root(x, n): return ZZ(x).nth_root(n, truncate_mode=1)[0]
```
### Root modulo n
```py
x = mod(a, n).nth_root(e)
```

### Right-Padding `m` with zero `\x00`
This basically means to multyply by 2, so you can use modular arithmetic product property to recover `c` generated from only `m`

### Bleichenbacher - Craft signature for a message that ends with some bytes
Suppose you know the public key (N,e) and you want to craft a signature for a message that end with *flag*, this mean that you are looking for a number `s` such that:
`pow(s,e,n)` has the least significant bytes that represent *flag*. 
Now, *flag* is `l` bit long, this mean `pow(s,e,2**l) == bytes_to_long('flag')`.
So basically you have to use rsa, but with `2**l` as modulus (not N)
```py
n = 2**l
phi = 2**(l-1)
d = pow(e,-1,phi)
s = pow(bytes_to_long('flag'), d, n)
```
