#Alumno: Jose Luis Jimenez
#Fecha: 17/08/2018
#Programa que imprime si un valor de entrada es primo o no

def primo(num):
    flag = True	
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
p=input ("Introduzca un numero entero: ")
if primo(p):
   print ("El numero es primo.")
else:
   print ("El numero no es primo.")
   
 
