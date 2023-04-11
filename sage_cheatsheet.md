# sage cheatsheet

## discrete log
Solve for x `a^x=b (mod n)`
```py
R = Integers(99)
a = R(4)
b = a^9
x = b.log(a)
```
## Root modulo n
solve for x: `x^e = a (mod n)`
```py
x = mod(a, n).nth_root(e)
```

## Interger nth root for huge number
```py
def integer_root(x, n): return ZZ(x).nth_root(n, truncate_mode=1)[0]
```
## Solving modular systems of equation
over Z/pZ
```py
# 6x + 3y = 1 (mod 17)
# 3x + 8y = 2 (mod 17)
A = matrix(GF(17), [[6,3], [3,8]])
b = matrix(GF(17), [1, 2]).transpose()
print( A.solve_right(b) )
print( (6*14+3*12) % 17 == 1 )
print( (3*14+8*12) % 17 == 2 )
```
over Z
```py
A = matrix(ZZ, [[6,3], [3,8]])
b = matrix(ZZ, [1,2]).transpose()
A.change_ring(GF(q)).solve_right(b.change_ring(GF(q)))
```

## Solve polynomial equation
```py
x = PolynomialRing(RationalField(),'x').gen()
f = x^6 - 2*x^5 + 3*x^4 - 3*x^3 + 3*x^2 - 2*x +1 - n
x = f.roots()[0][0]
```

## next prime
```py
(46).next_prime()
```
