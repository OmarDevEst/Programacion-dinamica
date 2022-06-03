def mult(i, j):
    if(i == j):
        return 0
    else:
        res = arr[i] * arr[j] * arr[j+1]
        return res

archivo = open("ejemploEntradaP4.txt", "r")
salida = open("salida.txt", "w")
arr = []
flag2 = 0

for line in archivo:
  flag = 0
  for number in line.split():
    flag += 1
    flag2 += 1
    if flag2 == 2:
      arr.append(int(number))
    if flag == 3 and not number.isalpha():
      arr.append(int(number))

size = len(arr) - 1
v = [[0 for x in range(size)] for x in range(2, size)]
v2 = [['0' for x in range(size)] for x in range(2, size)]

for l in range(size):
  for k in range(size - l):
    j = k + 1 + l
    if(l == 0):
      res1 = mult(k, j-1)
      res2 = mult(j, k)
    else:
      res1 = mult(k, j-1) + v[(l+2) % 2][k]
      res2 = mult(j, k) + v[(l+2) % 2][k+1]
    if(res1 <= res2):
      v[(l+2-1) % 2][k] = res1
      result = v[(l+2-1) % 2][k]
      buffer = "(" + v2[(l+2) % 2][k] + ")" + chr(64 + j)
      v2[(l+2-1) % 2][k] = buffer
    else:
      v[(l+2-1) % 2][k] = res2
      result = v[(l+2-1) % 2][k]
      buffer = chr(65) + "(" + v2[(l+2) % 2][k+1] +")"
      v2[(l+2-1) % 2][k] = buffer

letra = 65

for i in range(size + 1):
  buffer = buffer.replace("((0)" + chr(letra) + ")", chr(letra))
  letra += 1

salida.write(buffer + "\n")
salida.write(str(result))