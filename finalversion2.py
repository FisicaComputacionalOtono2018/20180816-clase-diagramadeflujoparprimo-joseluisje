#AUTOR: Jose Luis Jimenez Espinoza
#FECHA: 16/08/18
#PROGRAMA DESARROLLADO A PARTIR DEL DIAGRAMA DE FLUJO VISTO EN CLASE

p = int(input("Inserte un numero entero: "))
s=12
def primo(num):
    flag= True
    if num<2:
       flag=False
    elif p==2:
       flag=True
    else:
      for i in range (2,num-1/2):
         if num%i==0:
           flag=False
           break
    return flag
if p%2==0:
  p=p+1
if p<s:
    while p < s:
      if primo(p):
          s=s-p    
      p=p+2
while s > 0:
      if primo(p):
          s=s-1
      p=p+2
m=p-2    
print(m)
