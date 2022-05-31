from asyncio.windows_events import INFINITE
from unicodedata import numeric

letra = 0

def parentesis(i, j, n, bracket):
  if i == j:
    globals()['letra'] = letra + 1
    # print(chr(letra), end="")
    salida.write(chr(letra))
    return;
  # print("(", end="")
  salida.write("(")

  parentesis(i, bracket[i][j], n, bracket)
  parentesis(bracket[i][j] + 1, j, n, bracket)

  # print(")", end="")
  salida.write(")")

def ordenarMatrices(arr, n):
  m = [[0 for x in range(n)] for x in range(n)]
  bracket = [[0 for x in range(n)] for x in range(n)]

  for i in range(1, n):
    m[i][i] = 0

  for L in range(2, n):
    for i in range(1, n-L+1):
      j = i + L - 1
      m[i][j] = INFINITE
      for k in range(i, j):
        q  = m[i][k] + m[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
        if q < m[i][j]:
          m[i][j] = q
          bracket[i][j] = k

  globals()['letra'] = 64
  # print("Mejor secuencia : ", end="")
  parentesis(1, n-1, n, bracket)
  # print("\nCosto : ")
  # print("\n" + str(m[1][n - 1]))
  salida.write("\n" + str(m[1][n - 1]))

archivo = open("ejemploEntradaP4.txt", "r")
salida = open("salida.txt", "w")

arr = []
arr2 = []

for line in archivo:
  for number in line.split():
    if not number in arr2 and not number.isalpha():
      arr2.append(number)

for i in arr2:
  arr.append(int(i))

n = len(arr)
globals()['letra'] = 30

ordenarMatrices(arr, n)

