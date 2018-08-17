#AUTOR: Jose Luis Jimenez Espinoza
#FECHA: 16/08/18
#PROGRAMA DESARROLLADO A PARTIR DEL DIAGRAMA DE FLUJO VISTO EN CLASE

p = int(input("Inserte un numero entero: "))
s=12
if p%2==0: #El programa reconoce si p es par solo una vez y agrega 1 a su valor para volverlo impar. Es innecesario colocarlo dentro de un ciclo.
    p=p+1
if p<s: #Hay dos etapas durante todo el proceso. La primera de ellas es cuando p<s, en esta etapa el valor de s disminuye en funcion del valor de p y de si es primo o no.
    while p < s:
      A = 1
      B = 1
      C = 0
      while A < p-1:
        A=A+1
        C=p%A 
        if C==0:
          B=0         
          break
      if B==1:
          s=s-p    
      p=p+2
while s > 0: #La segunda etapa ocurre cuando cuando p=>s. Aqui s disminuye su valor de 1 en 1 y en funcion de si p es primo o no.
    D = 1
    F = 1
    G = 0
    while D < p-1:
        D = D+1
        G = p%D
        if G==0:
            F=0
            break
    if F==1:
        s=s-1
    p=p+2
m=p-2 #Asigne esta variable para anular el proceso de agregarle 2 a p que ocurre en la ultima iteracion de la segunda etapa, despues de que s alcanza su valor 0 y antes de imprimir p.   
print(m)

#En general el programa imprime el doceavo numero primo despues de p (incluido p, si p es primo) cuando p=>12. 
