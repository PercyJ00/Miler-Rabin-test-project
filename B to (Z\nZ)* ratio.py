import numpy as np
import math
import random
import matplotlib.pyplot as plt

def is_prime(n):

  for i in range(2,int(n/2)):

    if (n%i) == 0:
      return False

  return True


def decomposition(n):

  m = int(n)
  power = 0

  while(m % 2 == 0):
    m = int(m/2)
    power += 1

  return power, m


numbers_table = np.array([0])
size_of_euler_table = np.array([0])
size_of_B_table = np.array([0])
indicator = True


for n in range(5000):

  if n%2 == 0:
    continue

  if is_prime(n) == True:
    continue


  power, m = decomposition(n-1)

  size_of_euler = 0
  size_of_B = 0

  for i in range(n):
    a = i
    if math.gcd(i, n) == 1:
      size_of_euler += 1

      for j in range(m-1):
        a = a * i
        a = a % n
    
      if a % n == 1 or a % n == n - 1:
        indicator = False

      for k in range(power):
        a = (a**2) % n

        if a % n == n - 1:
          indicator = False
          break

      if indicator == True :
        size_of_B += 1

      indicator = True

  numbers_table = np.append(numbers_table, [n])
  size_of_euler_table = np.append(size_of_euler_table, [size_of_euler])
  size_of_B_table = np.append(size_of_B_table, [size_of_B])


ratio = np.zeros(size_of_euler_table.size)

plt.figure(figsize=(10,10))

for p in range(size_of_euler_table.size):
  ratio[p] = size_of_B_table[p] / size_of_euler_table[p]

for q in range(size_of_euler_table.size):

  if numbers_table[q] % 5 == 0:
    plt.scatter(numbers_table[q], ratio[q], color = 'green')
  
  elif numbers_table[q] % 7 == 0:
    plt.scatter(numbers_table[q], ratio[q], color = 'blue')

  elif numbers_table[q] % 11 == 0:
    plt.scatter(numbers_table[q], ratio[q], color = 'black')

  elif numbers_table[q] % 13 == 0:
    plt.scatter(numbers_table[q], ratio[q], color = 'yellow')
  
  elif numbers_table[q] % 17 == 0:
    plt.scatter(numbers_table[q], ratio[q], color = 'purple')
  
  else:
    plt.scatter(numbers_table[q], ratio[q], color = 'red')

plt.show()
