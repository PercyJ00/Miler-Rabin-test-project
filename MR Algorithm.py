import math
import random


def decomposition(n):

  m = int(n)
  power = 0

  while(m % 2 == 0):
    m = int(m/2)
    power += 1

  return power, m


def millerRabin(a, n):

  s, d = decomposition(n-1)

  x = a
  times = 0
  print(a, n)

  for j in range(d-1):
    x = x * a
    x = x % n
    times += 1
  

  y = 0

  for i in range(s):
    y = (x**2) % n


    if y == 1 and x != 1 and x != n-1 :
      return "composite"
        
    x = y

  if y != 1:  
      return "composite"

  return "Probably prime" 

  
