from sage.all import xgcd
# https://infosecwriteups.com/rsa-attacks-common-modulus-7bdb34f331a5

def attack(N,e1,C1,e2,C2):
  F = Integers(N)
  gcd_, x, y = xgcd(e1,e2) # x and y are such that: a*e1 + y*e2 == gcd(e1,e2)
  # since y will be negative it is necessary that: gcd(C1, N) == 1. This allow the existence of inverse(C1,N)
  M = F(C1)^x * F(C2)^y
  M = bytes.fromhex(hex(M)[2:]).decode()
  print(M)

