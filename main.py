def calc_tamanho(vetor):
  contador = 0
  for letra in vetor:
    contador += 1
  return contador

def inverte(vetor):
  contador = 0
  novo_vetor = ''
  for letra in vetor:
    contador -= 1
    novo_vetor += vetor[contador]
  return novo_vetor

def inverte2(vetor):
  novo_vetor = ''
  for i in range(calc_tamanho(vetor)-1, -1, -1):
    novo_vetor += vetor[i]
  return novo_vetor

def max_ab(a, b):
  return a if a > b else b

def max_ab2(a, b):
  maior = a
  if b > a:
    maior = b
  return maior

def min_ab(a, b):
  return a if a < b else b

def min_ab2(a, b):
  minimo = a
  if b < a:
    minimo = b
  return minimo

def max_lista(vetor):
  maior = vetor[0]
  for i in range(calc_tamanho(vetor) -1):
   maior_temp = max_ab(vetor[i], vetor[i+1])
   if maior_temp > maior:
     maior = maior_temp
  return maior

def min_lista(vetor):
  minimo = vetor[0]
  for i in range(calc_tamanho(vetor) - 1):
    minimo_temp = max_ab(vetor[i], vetor[i+1])
    if minimo_temp < minimo:
      minimo = minimo_temp
  return minimo
  

def maximo(*args):
  return max_lista(args)
  
def minimo(*args):
  return min_lista(args)

vetor = [2, 10, 5, 45, 15, 20, 60, 70, 2, 5]

resultado = maximo(*vetor)
print(resultado)


########### DESAFIO #####################

def max_abc(a, b, c):
  pass

def min_abc(a, b, c):
  pass
