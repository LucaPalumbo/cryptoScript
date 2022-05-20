# sage cheatsheet

## discrete log
Solve for x `a^x=b (mod n)`
```py
R = Integers(99)
a = R(4)
b = a^9
x = b.log(a)
```

## Interger nth root for huge number
```py
def integer_root(x, n): return ZZ(x).nth_root(n, truncate_mode=1)[0]
```

## Root modulo n
```py
x = mod(a, n).nth_root(e)
```
