# DSA
Digital signature algorithm
It generates 2 numbers as a signature

## parameters
g,p,q are public
x is secret

## sign
generate k randomply each time
```
# r = [ g ** k  mod p ] (mod q)
# s = k^(-1) * ( H(m) + x*r )  (mod q)
```

## problem
if k is known the algorithm is not secure. You can recover x, and sign what you want
