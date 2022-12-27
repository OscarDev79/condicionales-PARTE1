# bucle if

numero = 25

if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo")
else:
    print("El numero es cero")
# bucle while

numerowhile = 1

while numerowhile < 3:
    numerowhile+= 1
    print("La variable numerowhile vale: ",numerowhile)

# do while en python no existe, esto seria equivalente

numerodo = 3
numerodo+=1
while numerodo < 3:
    print("El bucle while no se imprime")

# bucle for en python ejemplo
for i in range(0,3):
    print(i)

# bucle switch en python no existe en su lugar se usa if , elif, else

estacion = "otoño"

if estacion=="verano":
    print("Estamos en verano")
elif estacion=="Invierno":
    print("Estamos en invierno")
elif  estacion=="Primavera":
    print("Estamos en primavera")
else:
    print("Estamos en : ", estacion)





    



