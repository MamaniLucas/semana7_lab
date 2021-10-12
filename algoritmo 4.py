numerospares=0
numerosimpares=0
suma=0
for i in range (6):
    numero =int (input("ingrese un numero: "))
    if numero%2 ==0:
        numerospares +=1
    else:
        numerosimpares+=1
print("la cantidad de numeros pared es : ", numerospares)
print("la cantidad de numeros impares es: ", numerosimpares)
