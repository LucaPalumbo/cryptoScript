# cryptoScript
usefull script about crypto attack



### Interger nth root for huge number
```py
def integer_root(x, n): return ZZ(x).nth_root(n, truncate_mode=1)[0]
```


### Right-Padding `m` with zero `\x00`
This basically means to multyply by 2, so you can use modular arithmetic product property to recover `c` generated from only `m`
