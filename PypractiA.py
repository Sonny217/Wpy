lista1=[20, 24, 15, 24, 90, 18, 16]
cant=0
for x in lista1:
   if x >= 18:
       cant+=1

print(f"Edades mayores e iguales a 18:{cant}")

def cargar_fecha():
   dd=int(input("Ingrese numero de dia:"))
   mm=int(input("Ingrese numero de mes:"))
   aa=int(input("Ingrese numero de año:"))
   return (dd,mm,aa)


def imprimir_fecha(fecha):
   print(fecha[0],fecha[1],fecha[2],sep="/")


bloque principal

fecha=cargar_fecha()
imprimir_fecha(fecha)

cuadra = int(input("Ingrese el lado del cuadrado:"))
peri= cuadra*4
print(f"El perimetro del lado del cuadtrado es:{peri}")

listA=[]
for i in range(4):
   numero=int(input("Ingrese uno de los cuatro numeros:"))
   listA.append(numero)
suma= listA[0]+listA[1]
multip= listA[2]*listA[3]
print(f"Suma del primer y segundo elemento:{suma} \n producto del segundo y cuarto valor:{multip}")


numeros=[]
for i in range(4):
   val=int(input("Ingrese uno de los cuatro valores:"))
   numeros.append(val)

suma = numeros[i]+numeros[i]
prom= suma/len(numeros)
print(f"Suma :{suma} y promedio de los cuatro elementos:{prom}")


sueldo=int(input("Ingrese Sueldo del mensual del empleado:"))
oras_traba=(input("Ingrese horas trabajadas:"))
sueldo= horas_traba*sueldo
print(f"El sueldo a pagar e:s {sueldo}")

for x in range(1,101):
  if x % 3 == 0:
##     if x % 5 == 0:
        print("buzz")
#     else:
      x % 3 and x % 5 == 0
     print("Fizz Buzz")
else:
   print(x)

valor1=int(input("Ingrese un valor:"))
valor2 = int(input("Ingrese un segundo valor:"))

if valor1 > valor2:
  adic = valor1 + valor2
  sustra= valor1 -valor2
 print(f"suma:{adic} y resta:{sustra}")

else:
   multi= valor2*valor1
   div = valor2/valor1
   print(f"Multiplicacion:{multi} y division:{div}")

nota1=int(input("ingrese la primera nota:"))
nota2=int(input("Ingrese la segunda nota:"))
nota3=int(input("ingrese la tercera nota:"))
promedio= (nota1+nota2+nota3)/3
if promedio >= 7:
print(f"El alumno ha sido promocionado:{promedio}")
else:
   print(f"El alumno no ha sido promocionado:{promedio}")

valor = int(input("Ingrese un valor:"))
if valor >= 10 and valor <=99:
print(f"El valor posee ds digitos:{valor}")
elif valor < 9:
print(f"El valor es de un solo digito:{valor}")
else:
 valor >=100
 print(f"El valor tiene tres digitos:{valor}")

valor1= int(input("Ingrese un valor:"))
valor2=int(input("Ingrese otro valor:"))
valor3=int(input("Ingres un ultimo valor:"))
if valor1 > valor2 and valor1 > valor3:
   print(f"El numero mayor es:{valor1}")
elif valor2 > valor1 and valor2 > valor3:
   print(f"El valor mayor es:{valor2}")
else:
   print(f"El valor mayor es:{valor3}")

spreguntas=int(input("Ingrese el numero de prguntas:"))
respuetas = int(input("Ingrese numer de preguntas correctas:"))
porcentaje = respuetas*100/preguntas
if porcentaje >= 90:
   print(f"El postulantes tiene nivel máximo:{porcentaje}")
elif porcentaje >= 75 and porcentaje < 90:
   print(f"El postulantes tiene nivel medio:{porcentaje}")
elif porcentaje >= 50 and porcentaje < 75:
   print(f"El postulantes tiene nivel regulas:{porcentaje}")
else:
   print(f"El postulantes esta fuera nivel:{porcentaje}")

día=int(input("Ingrese el dia:"))
mes=int(input("Ingrese el mes:"))
if día == 25 and mes == 12:
   print(f"La fecha Ingresada pertenece a navidad:{día}/{mes}/2024")

else:
  print(f"La fecha ingresada no pertece a navidad:{día}/{mes}/2024")

def valores(v1,v2,v3):
   if v1 and v2 and v3 < 10:
       print(f"Los valores ingresados son menores a 10")

   else:
       print("los valores no son menors a 10")
valores(30,54,51)

def val(v1,v2,v3):
   if v1 and v2 and v3 < 10:
       print("Alguno de los numeros es menor a diez")
   elif v1 and v2 and v3 > 10:
        print("Alguno de los numeros ingresados mayor o igual a diez")

val(11,11,12)

def valores(v1,v2,v3):
   if v1 == v2 and v2 == v3:
       sumar= (v1 + v2)*v3
       print(sumar)
      return sumar
   else:
       print("Los valores no son iguales:")
       return None

valor1= int(input("Ingrese un valor:"))
valor2= int(input("Ingrese un segundo valor:"))
valor3= int(input("Ingrese un  ultimo valor:"))
valores(valor1,valor2,valor3,)

def coordenada(cuaX, cuaY):
   if cuaX>0 and cuaY >0:
       print(f"Las coordenadas ingresadas son del cuadrante >1<:{cuaX},{cuaY}")
   elif cuaX<0 and cuaY>0:
       print(f"Las coordenadas ingresadas son del cuadrante >2<:{cuaX},{cuaY}")
   elif cuaX < 0 and cuaY < 0:
       print(f"Las coordenadas ingresadas son del cuadrante >3<:{cuaX},{cuaY}")
   elif cuaX > 0 and cuaY < 0:
       print(f"Las coordenadas ingresadas son del cuadrante >4<:{cuaX},{cuaY}")
   else:
       print(f"Las coordenadas están en el eje X o Y:{cuaX},{cuaY}")

x=int(input("Ingrese la coordenada de x:"))
y=int(input("Ingrese la coordenada de y:"))
coordenada(x,y)

def operario(sueldo, años):
   if sueldo < 500 and años >= 10:
       aumento = sueldo * 0.20
       print(f"Tiene un aumento del 20%: {aumento + sueldo}")
   elif sueldo < 500 and años < 10:
       aument1 = sueldo * 0.05
       print(f"Tiene un aumento del 5%: {aument1 + sueldo}")
   elif sueldo >=500:
       print(f"No se aplica aumento:{sueldo}")

suel=int(input("Ingrese sueldo del operario:"))
tiempo=int(input("Ingrese años del orperario:"))
operario(suel,tiempo)

def rango(val1, val2, val3):
   mayor = max(val1, val2, val3)
   menor = min(val1, val2, val3)
   print(f"El valor mayor es: {mayor} y el valor menor es: {menor}")

val1 = int(input("Ingrese el primer valor: "))
val2 = int(input("Ingrese el segundo valor: "))
val3 = int(input("Ingrese el tercer valor: "))
rango(val1,val2,val3)

def clasificar_notas(notas):
   mayores = [n for n in notas if n >= 7]
   menores = [n for n in notas if n < 7]

   print(f"Notas mayores o iguales a 7: {mayores}")
   print(f"Notas menores a 7: {menores}")

def obtener_notas():
   return [int(input("Ingrese la nota (0-10): ")) for _ in range(10)]

clasificar_notas(obtener_notas())

def calcular_altura_promedio():
   n = int(input("¿Cuántas personas hay? "))
   suma = 0
   for _ in range(n):
       altura = float(input("Ingrese la altura: "))
       suma += altura
   promedio = suma / n
   print("Altura promedio:", promedio)

Ejecutar la función
calcular_altura_promedio()

#def sueldos():
#    n = int(input("¿Cuantos empleados son?"))
#    conta=0
#    conta1=0
    x=0
    while x < n:
        cobro= int(input("Ingrese sueldo del empleado:"))
        if cobro >=100 and cobro <=300:
            conta+=1
        elif cobro > 300:
            conta1+=1
        x=x+1
    print(f"Empleados que cobran entres 100 a 300:{conta}")
    print(f"Empleados que cobran mas de 300:{conta1}")

sueldos()

def contador():
   x=0
   while x < 100:
       print(x)
       x=x+11
contador()

#def muitiplos():
    x=8
    while x <= 500:
        print(x)
        x=x+8

muitiplos()

def list_mayor(listaA, listaB):
    if  len(listaA) > len(listaB):
        print("La lista 1 es mayor")
    elif len(listaB) > len(listaA):
      print("La lista 2 es mayor")
    else:
        print("listas iguales")


def listas():
    lista1=[]
    lista2=[]
    x=0
    n=int(input("Ingrese cuantos valores tendra las listas:"))
    while x < n:
        valor=int(input("Ingrese valor a la lista1:"))
        lista1.append(valor)
        valor1=int(input("Ingrese valor a la lista2:"))
        lista2.append(valor1)
        x=x+1
    return  lista1, lista2


lista1, lista2 = listas()
list_mayor(lista1,lista2)

def triangulos():
    cant=0
    n=int(input("Ingrese  el numero de lados del triangulo:"))
    for x in range(n):
        bas=int(input("Ingrese base del triangulo:"))
        alt=int(input("Ingrese altura del triangulo:"))
        superficie= (bas*alt)/2
        print("La superficie del triangulo es: ", superficie)
        if superficie > 12:
            cant=cant+1
            print(f"Hay ", {cant}, "triangulos con superficie mayor a 12")

triangulos()

def coordenada(cuaX, cuaY):
    if cuaX>0 and cuaY >0:
        print(f"Las coordenadas ingresadas son del cuadrante >1<:{cuaX},{cuaY}")
    elif cuaX<0 and cuaY>0:
        print(f"Las coordenadas ingresadas son del cuadrante >2<:{cuaX},{cuaY}")
    elif cuaX < 0 and cuaY < 0:
        print(f"Las coordenadas ingresadas son del cuadrante >3<:{cuaX},{cuaY}")
    elif cuaX > 0 and cuaY < 0:
        print(f"Las coordenadas ingresadas son del cuadrante >4<:{cuaX},{cuaY}")
    else:
        print(f"Las coordenadas están en el eje X o Y:{cuaX},{cuaY}")

x=int(input("Ingrese la coordenada de x:"))
y=int(input("Ingrese la coordenada de y:"))
coordenada(x,  y)


oracion= str(input("Ingrese una oracion:"))
oracion1 = oracion.lower()
cant = 0
x=0
while x < len(oracion1):
    if oracion[x] == "a"or oracion[x] =="e" or oracion[x] == "i" or oracion[x] =="o" or oracion[x] == "u":
        cant = cant + 1
    x += 1

print(f"La cantidad de vocales en la oracion es: {cant}")

def contra():
    contra1 = input("Ingrese una clave: ")
    cant = 0
    x = 0

    while x < len(contra1):

        if ord(contra1[x]) > 10 and ord(contra1[x]) < 20:
            cant += 1
        x += 1

    if cant < 10:
        print(f"La clave NO es valida: {cant} caracteres válidos")
    else:
        print(f"La clave es valida: {cant} caracteres válidos")

contra()

lista=[100,700,300,580,200, 21, 5, 4, 7]
x=0
cantidad=0
while x < len(lista):
    if lista[x] >= 100:
        cantidad += 1
    x += 1

print(f"La cantidad de elementos en la lista que son mayores o iguales a 100 es: {cantidad}")

def lista1():
 lista =[5,7,8,9,10,4,7]
 x=0
 cantidad = 0
 for x in range(len(lista)):
  if  lista[x] >= 7:
    cantidad += 1
 print(f"la cantidad de elementos mayores o igual a 7 son: {cantidad}")
 return  cantidad

lista1()

def nombres(name):
  cantidad=0
  for  x in range(len(name)):
     if len(name[x]) >= 5:
        cantidad += 1
  print(f"la cantidad de letras en el nombre que son mayores o iguales a 5 son: {cantidad}")
  return cantidad

names=["Sofía","Mateo","Valentina","Leonardo","Isabela","Diego","Camila","Alejandro","Lucía","Samuel"]
nombres(names)

def duadrado():
   valor = int(input("Ingrese un valor:"))
   cuadrado = valor**2
   print(f"El cuadrado del valor ingresado es: {cuadrado}")

def product():
    valor1 = int(input("Ingrese el primer valor: "))
    valor2 = int(input("Ingrese el segundo valor: "))
    producto = valor1 * valor2
    print(f"El producto de los valores ingresados es: {producto}")


duadrado()
product()  # No se puede llamar a una función dentro de otra función en este caso,

def numero():
    valor = int(input("Ingrese un primer valor: "))
    valor1 = int(input("Ingrese  el segundo valor: "))
    valor2 = int(input("Ingrese un tercer valor:"))
    if valor < valor1 and valor < valor2:
        print(f"El valor {valor} ingresado es menor que los otros dos valores")
    elif valor1 < valor and valor1 < valor2:
        print(f"El valor {valor1} ingresado es menor que los otros dos valores")
    elif valor2 < valor and valor2 < valor1:
        print(f"El valor {valor2} ingresado es menor que los otros dos valores")

numero()

def word():
    contador=0
    palabra = input("Ingrese una palabra: ")
    for  x in palabra:
        if x in "aeiouAEIOU":
            contador +=1
    print(f"La cantidad de letras es:{contador}" )
word()


def ord(num1, num2, num3):
    if num1 <= num2 and num1 <= num3:
        if num2 <= num3:
            print(f"El orden de los valores ingresados es: {num1} {num2} {num3}")
        else:
            print(f"El orden de los valores ingresados es: {num1} {num3} {num2}")
    elif num2 <= num1 and num2 <= num3:
        if num1 <= num3:
            print(f"El orden de los valores ingresados es: {num2} {num1} {num3}")
        else:
            print(f"El orden de los valores ingresados es: {num2} {num3} {num1}")
    else:  # Aquí se asume que num3 es el menor
        if num1 <= num2:
            print(f"El orden de los valores ingresados es: {num3} {num1} {num2}")
        else:
            print(f"El orden de los valores ingresados es: {num3} {num2} {num1}")

def number():
    valor1 = int(input("Ingrese el primer valor: "))
    valor2 = int(input("Ingrese el segundo valor: "))
    valor3 = int(input("Ingrese el tercer valor: "))
    ord(valor1, valor2, valor3)

number()


def suma(v1, v2,v3,v4=0,v5=0):
    return v1 + v2 + v3 + v4 + v5

print(suma(1,2,3))

def carga_datos():
    numero = []
    for x in range(5):
        numt = int(input("Ingrese un número: "))
        numero.append(numt)
    return numero

def numeros_va(numero):
    may = numero[0]
    men = numero[0]
    for x in range(1, len(numero)):
        if numero[x] > may:
            may = numero[x]
        elif numero[x] < men:
            men = numero[x]
    return (may, men)

numero = carga_datos()

mayor, menor = numeros_va(numero)

print("Mayor valor de la lista:", mayor)
print("Menor valor de la lista:", menor)

def carga_datos():
    nombre=str(input("Ingrese el nombre del empleado:"))
    sueldo=int(input("Ingrese el sueldo:"))
    return (nombre, sueldo)

def mayor_sueldo(empleado1, empleado2):
    if empleado1[1] > empleado2[1]:
         print(empleado1[0],"tiene mayor sueldo")
    else:
        print(empleado2[0],"tiene mayor sueldo")


empleado1 = carga_datos()
empleado2 = carga_datos()
mayor_sueldo(empleado1,empleado2)

def cargas_lados():
    lado=int(input("Ingrese los lados del cuadrado:"))
    perimetro = lado * 4
    print(f"El perimetro del cuadrado es: {perimetro}")

cargas_lados()

def calcular():
    nume=[]
    for x in range(4):
     while True:
        try:
           num=int(input(f"Ingrese un número:"))
           nume.append(num)
           break
        except ValueError:
           print("Error, ingrese un número")
    return nume

def sumar(nume):
   if len(nume) >=4:
    suml=nume[0] + nume[1]
    print(f"La suma de los dos primeros números es:{suml}")
    multi= nume[2]*nume[3]
    print(f"La multimplicacion de los dos últimos números es: {multi}")

calcular()
sumar()


def calcular():
    nume=[]
    for x in range(4):
     while True:
        try:
           num=int(input(f"Ingrese un número:"))
           nume.append(num)
           break
        except ValueError:
           print("Error, ingrese un número")
    return nume

def sumar(nume):
   if len(nume) >=4:
    suml=nume[0] + nume[1]  + nume[2] + nume[3]
    print(f"La suma de los cuatro números es: {suml}")
    promedio=  suml/4
    print(f"El promedio números es: {promedio}")

nume=calcular()
sumar(nume)

def datos_operario():
    canti_horas=int(input("Ingrese la cantidad de horas trabajadas:"))
    horas=int(input("Ingrese el valor de las horas:"))
    return canti_horas, horas

def calcular_salario(canti_horas, horas):
    salario = canti_horas * horas
    print(f"El sueldo apagar  es: ${salario}")


cantti_horas, horas= datos_operario()
calcular_salario(cantti_horas, horas)def      b

def cargar():
    num1=int(input("Ingrese el primer número:"))
    num2=int(input("Ingrese el segundo número:"))
    return num1, num2

def verificar(num1, num2):
    if num1 > num2:
        duma= num1+ num2
        dama= num1/num2
        print(f"La suma del mayor por el menor:{duma}\n La división del mayor por el menor:{dama}")

    if num2 > num1:
        tuna = num2*num1
        suna= num2/num1
        print(f"La multiplicación del mayor por el menor:{tuna}\n La división del mayor  por el menor:{suna}")

num1, num2 = cargar()
verificar(num1 , num2)


def ingre_nota():
    notas = []
    for x in range(4):
        while True:
            try:
                nota = int(input("Ingrese una nota: "))  
                if 0 <= nota <= 10:  
                    notas.append(nota)
                    break  
                else:
                    print("La nota debe estar entre 0 y 10. Intente de nuevo.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
    return notas 


def prome(notas):
    if len(notas) >= 4:
        sul = sum(notas)
        prom = sul / 4
        print(f"El promedio de las notas es: {prom}")
        return prom


def validar(prom):
    if prom > 7:
        print(f"El  estudiante Promocionado:{prom}")
    else:
        print(f"El estudiante no promocionado:{prom}")


ingrR = ingre_nota()
pom = prome(ingrR)
validar(pom)

def carga_numero():
    valor=int(input("Ingrese un numero:"))
    return valor

def validar(valor):
    if valor > 10 and valor <99:
        print(f"El valor ingresado es de dos digitos: {valor}")
    if  valor < 10:
        print(f"El numero tiene un solo digito:{valor}")

valor=carga_numero()
validar(valor) 

def carga_numero():
    numbers=[]
    for x in range(5):
        while True:
            try:
                valor=int(input(f"Ingrese el {x+1} numero:"))
                numbers.append(valor)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
    return numbers



def numero_mayor(numbers):
    if len(numbers):
        print(f"El número mayor es: {max(numbers)}")


numbers=carga_numero()
numero_mayor(numbers) 

def notas_alumnos():
    notas=[]
    for x in range(5):
        while True:
            try:
                nota=float(input(f"Ingrese la nota del alumno:"))
                notas.append(nota)
                if nota >= 0 and nota <= 10:
                 break
            except ValueError:
             print("Por favor, ingrese un número válido.")
    return  notas

def carga_notas(notas):
   cont=0
   for val in notas:
      if val >= 7:
         cont+=1
         print(f"Los estdiantes aprovados son:{cont}")
        

notass= notas_alumnos()
carga_notas(notass)

def cargar_lista():
    listat=[]
    for x in range(5):
        val=int(input("Ingrese un valor:"))
        listat.append(val)
        return (listat)

def mayor_menor(list):
    may=list[0]
    men=list[0]
    for x in range(1,len(list)):
        if list[x]>may:
            may=list[x]
        elif list[x]<men:
            men=list[x]
    return (may,men)


list=cargar_lista()
mayor, menor=mayor_menor(list)
print(f"El mayor es: {mayor}")
print(f"El menor es: {menor}")
        
def cargar_lista():
    lista = []
    for _ in range(5):
        valor = int(input("Ingrese un valor: "))
        lista.append(valor)
    return lista

def encontrar_mayor_y_menor(lista):
    mayor = lista[0]
    menor = lista[0]
    for valor in lista[1:]:
        if valor > mayor:
            mayor = valor
        if valor < menor:
            menor = valor
    return mayor, menor

lista = cargar_lista()
mayor, menor = encontrar_mayor_y_menor(lista)
print(f"El mayor es: {mayor}")
print(f"El menor es: {menor}")

def datos_empleados():
    nombre=str(input("Ingrese nombre del empleado:"))
    sueldo=int(input("Ingrese el sueldo:"))
    return (nombre,sueldo)

def mostrar_datos(empleado1,empleado2):
    if empleado1 > empleado2:
        print(f"El empleado {empleado1[0]} tiene un sueldo mayor")
    else:
        print(f"El empleado {empleado2[0]} tiene un sueldo mayor")

empleado1=datos_empleados()
empleado2=datos_empleados()
mostrar_datos(empleado1,empleado2)

def cargar_paisespoblacion():
    paises=[]
    for x in range(5):
        nom=input("Ingresar el nombre del pais:")
        cant=int(input("Ingrese la cantidad de habitantes:"))
        paises.append((nom,cant))
    return paises


def imprimir(paises):
    print("Paises y su poblacion")
    for x in range(len(paises)):
        print(paises[x][0],paises[x][1])


def pais_maspoblacion(paises):
    pos=0
    for x in range(1,len(paises)):
        if paises[x][1]>paises[pos][1]:
            pos=x
    print("Pais con mayor cantidad de habitantes:",paises[pos][0])
    

paises=cargar_paisespoblacion()
imprimir(paises)
pais_maspoblacion(paises)

def cargar_empleados_sueldos():
    empleados = []
    for x in range(3):
        nombre = input("Ingrese el nombre del empleado: ")
        sueldo=int(input("Ingrese tres sueldos:"))
        empleados.append((nombre,sueldo))
        return empleados

def monto_total(empleados):
    print("Total del sueldo de los empleados")
    for x in range(5):
        total=empleados[x][1][0]+empleados[x][1][1]+empleados[x][1][2]
        print(empleados[x][0],total)



def ingreso_mayor10000(empleados):
    print("Empleados con ingresos superiores a 10000 en los ultimos 3 meses")
    for x in range(5):
        total=empleados[x][1][0]+empleados[x][1][1]+empleados[x][1][2]
        if total>10000:
            print(empleados[x][0],total)

empleados=cargar_empleados_sueldos()
monto_total(empleados)
ingreso_mayor10000(empleados)

def cargar_empleados():
    empleados=[]
    for x in range(5):
        nom=input("Ingrese el nombre del empleado:")
        su1=int(input("Primer sueldo:"))
        su2=int(input("Segundo sueldo:"))
        su3=int(input("Tercer sueldo:"))
        empleados.append([nom,(su1,su2,su3)])
    return empleados


def ganancias(empleados):
    print("Monto total ganado por empleado en los ultimos tres meses")
    for x in range(5):
        total=empleados[x][1][0]+empleados[x][1][1]+empleados[x][1][2]
        print(empleados[x][0],total)


def ganancias_superior10000(empleados):
    print("Empleados con ingresos superiores a 10000 en los ultimos 3 meses")
    for x in range(5):
        total=empleados[x][1][0]+empleados[x][1][1]+empleados[x][1][2]
        if total>10000:
            print(empleados[x][0],total)

empleados=cargar_empleados()
ganancias(empleados)
ganancias_superior10000(empleados)

def votos_candidatos():
    candidatos = []
    for x in range(3):
     candi=str(input("Ingrese nombre del candidato:"))
     provincia=str(input("Ingrese provicia del candidatos:"))
     votos=int(input("Ingrese cantidad de votos obtenidos:"))
     candidatos.append([candi,(votos,provincia)])
    return candidatos

def carga_palabras():
    palabras = []
    for x in range(5):
        palabra = input("Ingrese una palabra:")
        palabras.append(palabra)
    return palabras

def  contar_palabras(palabras):
    print("Palabras con mas de 5 caracteres:")
    for pala in palabras:
        if  len(pala)>5:
            print(pala)
            

palabras=carga_palabras()
contar_palabras(palabras)

def cargar():
    doc_personas={}
    for x in range(4):
        nombre= str(input("Ingrese nombre:"))
        num_doc=int(input("ingrese  numero de documento:"))
        doc_personas[nombre] =num_doc
    return doc_personas

def mostras_Proct(doc_persona):
    print("Lista completa:")
    for nombre in doc_persona:
        print(f"Nombre: {nombre} N. Documento: {doc_persona[nombre]}")

def consulta(doc_persona):
    consul = input("Ingrese nombre de consulta:")
    if  consul in doc_persona:
        print(f"El documento de {consul} es: {doc_persona[consul]}")


doc_persona=cargar()
mostras_Proct(doc_persona)
consulta(doc_persona)

def main():
    print("Calculadora en Python")
    
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        
        operador = input("Introduce el operador (+, -, *, /): ")
        
        if operador == "+":
            resultado = num1 + num2
            print(f"Resultado: {resultado}")
        elif operador == "-":
            resultado = num1 - num2
            print(f"Resultado: {resultado}")
        elif operador == "*":
            resultado = num1 * num2
            print(f"Resultado: {resultado}")
        elif operador == "/":
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado: {resultado}")
            else:
                print("Error: No se puede dividir entre cero.")
        else:
            print("Operador no válido.")
    
    except ValueError:
        print("Por favor, introduce valores numéricos válidos.")

if __name__ == "__main__":
    main()

using System;

class Calculadora
{
    static void Main(string[] args)
    {
        double num1, num2, resultado;
        string operacion;

        // Mostrar el menú
        Console.WriteLine("Calculadora en C#");
        Console.WriteLine("Selecciona una operación:");
        Console.WriteLine("1. Sumar");
        Console.WriteLine("2. Restar");
        Console.WriteLine("3. Multiplicar");
        Console.WriteLine("4. Dividir");

        // Leer la opción de operación
        operacion = Console.ReadLine();

        // Pedir los dos números
        Console.Write("Ingresa el primer número: ");
        num1 = Convert.ToDouble(Console.ReadLine());

        Console.Write("Ingresa el segundo número: ");
        num2 = Convert.ToDouble(Console.ReadLine());

        // Realizar la operación seleccionada
        switch (operacion)
        {
            case "1":
                resultado = num1 + num2;
                Console.WriteLine($"Resultado: {num1} + {num2} = {resultado}");
                break;
            case "2":
                resultado = num1 - num2;
                Console.WriteLine($"Resultado: {num1} - {num2} = {resultado}");
                break;
            case "3":
                resultado = num1 * num2;
                Console.WriteLine($"Resultado: {num1} * {num2} = {resultado}");
                break;
            case "4":
                if (num2 != 0)
                {
                    resultado = num1 / num2;
                    Console.WriteLine($"Resultado: {num1} / {num2} = {resultado}");
                }
                else
                {
                    Console.WriteLine("Error: No se puede dividir entre 0.");
                }
                break;
            default:
                Console.WriteLine("Opción no válida.");
                break;
        }

        // Esperar para cerrar la aplicación
        Console.WriteLine("Presiona cualquier tecla para salir.");
        Console.ReadKey();
    }
}

class humano:
    def personal(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

    def seda(self):
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")

persona1=humano()
persona1.personal("tito", 19)
persona1.mostrar()
persona1.seda()

class angulos_triangulos:

    def carga_lados(self):
        self.lado1 = int(input("Ingrese el primer lado: "))
        self.lado2 = int(input("Ingrese el segundo lado: "))
        self.lado3 = int(input("Ingrese el tercer lado: "))
    
    def imprimir(self):
        print(f"Lado 1: {self.lado1}")
        print(f"Lado 2: {self.lado2}")
        print(f"Lado 3: {self.lado3}")

    
    def mostrar(self):
        if self.lado1 != self.lado2 and self.lado1 != self.lado3:
            print(f"El triángulo no es equilátero")
        else:
            print("El triangulo es equilátero")
        
        if self.lado1>self.lado2 and self.lado1>self.lado3:
            print(f"El lado 1 es el mayor:{self.lado1}")
        elif self.lado2>self.lado1 and self.lado2>self.lado3:
            print(f"El lado 2 es el mayor:{self.lado2}")
        elif self.lado3 >self.lado1 and self.lado3>self.lado2:
           print(f"El lado 3 es el :{self.lado3}")
        else:
            print("Los lados son iguales")
        
angulos=angulos_triangulos()
angulos.carga_lados()
angulos.imprimir()
angulos.mostrar()

# codigo optimizado:
class AngulosTriangulos:
    
    def carga_lados(self):
        """Carga los lados del triángulo desde la entrada del usuario."""
        self.lados = [int(input(f"Ingrese el lado {i+1}: ")) for i in range(3)]
    
    def imprimir(self):
        """Imprime los tres lados del triángulo."""
        for i, lado in enumerate(self.lados, start=1):
            print(f"Lado {i}: {lado}")
    
    def mostrar(self):
        """Determina el tipo de triángulo y el lado mayor."""
        # Verificar si es un triángulo equilátero
        if self.lados[0] == self.lados[1] == self.lados[2]:
            print("El triángulo es equilátero.")
        else:
            print("El triángulo no es equilátero.")
        
        # Determinar el lado mayor
        mayor = max(self.lados)
        if self.lados.count(mayor) == 1:
            print(f"El lado mayor es: {mayor}")
        else:
            print("Los lados mayores son iguales.")
    

# Crear instancia y ejecutar los métodos
angulos = AngulosTriangulos()
angulos.carga_lados()
angulos.imprimir()
angulos.mostrar()

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        areas=self.lado**2
        print(f"El area del cuadrdo es {areas}")
    
    def perimetro(self):
        perimet=self.lado*4
        print(f"El perimetro del cuadrado es {perimet}")
    
cuadrado1=Cuadrado(4)
cuadrado1.area()
cuadrado1.perimetro()

class Fizz_buzz:
    def __init__(self):
        for self.numero in range(1,100):
            if self.numero % 3 == 0 and self.numero % 5 == 0:
                print("fizzbuzz")
            else:
                if self.numero % 2 == 0:
                    print("fizz")

fizz_buzz()

class Operaciones:
    def __init__(self):
        self.numero1 = int(input("Ingrese el primer número: "))
        self.numero2 = int(input("Ingrese el segundo número: "))
    
    def operal(self):
        print(f"La división de los dos números es: {self.numero1 / self.numero2}")
        print(f"La multiplicación es: {self.numero1*self.numero2}")
        print(f"La suma de los dos números es: {self.numero1+self.numero2}")
        if self.numero1 > self.numero2:
            print(f"La resta es: {self.numero1-self.numero2}")
        elif print(f"La resta es: {self.numero2-self.numero1}"):
            pass
             
ope=Operaciones()
ope.operal()

class personal_Agenda:
    def __init__(self):
        self.nombre = []
        self.telefono = []
        self.mail = []

    def menu(self):
        agendados = 0
        while agendados != 6:
            print("-" * 10)
            print("1. Agregar contacto")
            print("2. Buscar contacto")
            print("3. Eliminar contacto")
            print("4. Mostrar contactos")
            print("5. Modificar teléfono y mail")
            print("6. Salir")
            print("-" * 10)
            try:
                agendados = int(input("Elija su opción: "))
            except ValueError:
                print("Por favor, ingrese un número válido.")
                continue
            print("-" * 10)
            if agendados == 1:
                self.nombre.append(input("Ingrese el nombre del contacto: "))
                self.telefono.append(input("Ingrese el teléfono del contacto: "))
                self.mail.append(input("Ingrese el mail del contacto: "))
            elif agendados == 2:
                self.buscar_contacto()
            elif agendados == 3:
                self.eliminar_contacto()
            elif agendados == 4:
                self.mostrar_contactos()
            elif agendados == 5:
                self.modifica_tele_mail()
            elif agendados == 6:
                confirmacion = input("¿Está seguro que desea salir? (s/n): ").lower()
                if confirmacion == 's':
                    print("Gracias por usar la agenda.")
                    break
                else:
                    print("Volviendo al menú...")

    def buscar_contacto(self):
        nombre1 = input("Ingrese el nombre del contacto a buscar: ")
        if nombre1 in self.nombre:
            indice = self.nombre.index(nombre1)
            print(f"El contacto {nombre1} tiene el teléfono {self.telefono[indice]} y el mail {self.mail[indice]}")
        else:
            print("El contacto no existe.")

    def eliminar_contacto(self):
        nombre2 = input("Ingrese el nombre del contacto a eliminar: ")
        if nombre2 in self.nombre:
            indice = self.nombre.index(nombre2)
            self.nombre.pop(indice)
            self.telefono.pop(indice)
            self.mail.pop(indice)
            print(f"El contacto {nombre2} ha sido eliminado.")
        else:
            print("El contacto no existe.")

    def mostrar_contactos(self):
        if not self.nombre:
            print("No hay contactos.")
            return
        print("Listado de contactos:")
        for i in range(len(self.nombre)):
            print(f"Nombre: {self.nombre[i]} - Teléfono: {self.telefono[i]} - Mail: {self.mail[i]}")

    def modifica_tele_mail(self):
        nombre3 = input("Ingrese el nombre del contacto a modificar: ")
        if nombre3 in self.nombre:
            indice = self.nombre.index(nombre3)
            telefono = input("Ingrese el nuevo teléfono del contacto: ")
            maill = input("Ingrese el nuevo mail del contacto: ")
            self.telefono[indice] = telefono
            self.mail[indice] = maill
            print(f"El contacto {nombre3} ha sido modificado.")
        else:
            print("El contacto no existe.")


agend = personal_Agenda()
agend.menu()

import flet as ft

class PersonalAgenda:
    def __init__(self):
        self.contactos = []  # Lista de tuplas (nombre, telefono, mail)

    def agregar_contacto(self, nombre, telefono, mail):
        self.contactos.append((nombre, telefono, mail))

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto[0] == nombre:
                return contacto
        return None

    def eliminar_contacto(self, nombre):
        contacto = self.buscar_contacto(nombre)
        if contacto:
            self.contactos.remove(contacto)
            return True
        return False

    def modificar_telefono_mail(self, nombre, telefono, mail):
        contacto = self.buscar_contacto(nombre)
        if contacto:
            indice = self.contactos.index(contacto)
            self.contactos[indice] = (nombre, telefono, mail)
            return True
        return False

    def mostrar_contactos(self):
        return [f"Nombre: {nombre} - Teléfono: {telefono} - Mail: {mail}" 
                for nombre, telefono, mail in self.contactos]


def main(page: ft.Page):
    agenda = PersonalAgenda()

    # Widgets de la interfaz
    nombre_input = ft.TextField(label="Nombre del contacto")
    telefono_input = ft.TextField(label="Teléfono del contacto")
    mail_input = ft.TextField(label="Mail del contacto")
    output = ft.Column()

    def agregar_click(e):
        nombre = nombre_input.value
        telefono = telefono_input.value
        mail = mail_input.value
        if nombre and telefono and mail:
            agenda.agregar_contacto(nombre, telefono, mail)
            output.controls.append(ft.Text(f"Contacto {nombre} agregado."))
            nombre_input.value = telefono_input.value = mail_input.value = ""
            page.update()

    def buscar_click(e):
        nombre = nombre_input.value
        contacto = agenda.buscar_contacto(nombre)
        if contacto:
            output.controls.append(ft.Text(f"El contacto {nombre} tiene el teléfono {contacto[1]} y el mail {contacto[2]}"))
        else:
            output.controls.append(ft.Text("El contacto no existe."))
        page.update()

    def eliminar_click(e):
        nombre = nombre_input.value
        if agenda.eliminar_contacto(nombre):
            output.controls.append(ft.Text(f"El contacto {nombre} ha sido eliminado."))
        else:
            output.controls.append(ft.Text("El contacto no existe."))
        page.update()

    def modificar_click(e):
        nombre = nombre_input.value
        telefono = telefono_input.value
        mail = mail_input.value
        if agenda.modificar_telefono_mail(nombre, telefono, mail):
            output.controls.append(ft.Text(f"El contacto {nombre} ha sido modificado."))
        else:
            output.controls.append(ft.Text("El contacto no existe."))
        page.update()

    def mostrar_click(e):
        contactos = agenda.mostrar_contactos()
        if contactos:
            output.controls.extend([ft.Text(contacto) for contacto in contactos])
        else:
            output.controls.append(ft.Text("No hay contactos."))
        page.update()

    # Botones de interacción
    agregar_btn = ft.ElevatedButton("Agregar contacto", on_click=agregar_click)
    buscar_btn = ft.ElevatedButton("Buscar contacto", on_click=buscar_click)
    eliminar_btn = ft.ElevatedButton("Eliminar contacto", on_click=eliminar_click)
    modificar_btn = ft.ElevatedButton("Modificar teléfono y mail", on_click=modificar_click)
    mostrar_btn = ft.ElevatedButton("Mostrar contactos", on_click=mostrar_click)

    # Añadir controles (inputs, botones, etc.)
    page.add(
        nombre_input,
        telefono_input,
        mail_input,
        agregar_btn,
        buscar_btn,
        eliminar_btn,
        modificar_btn,
        mostrar_btn,
        output
    )

ft.app(target=main)

lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)

print(lst)

lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0

for number in lst:
    add += number
    lst_2.append(add)

print(lst_2)

class animal:
    def __init__(self):
        self.nombre = input("Imgrese nombre del animal:")
        self.edad = int(input("Ingrese edad del animal:"))
    
    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

    def vida_util(self):
        if self.edad > 7:
            print("El animal es viejo")
        elif self.edad < 7:
            print("El animal es joven")
    

animal1=animal()
animal1.imprimir()
animal1.vida_util()

class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = input("Ingrese el titular:")
        self.cantidad = int(input("Ingrese la cantidad:"))
    
    def mostrar(self):
        print(f"Titular: {self.titular}")
        print(f"Cantidad: {self.cantidad}")

class CajaAhorra(Cuenta):
    def __init__(self, titular, cantidad):
        super().__init__(titular,cantidad)
    def mostrar(self):
        print("cuenta de caja de ahorro:")
        super().mostrar()


class PlazoFijo(Cuenta):
    def __init__(self, titular, cantidad , plazo, interes):
        super().__init__(titular,cantidad)
        self.plazo=plazo
        self.interes=interes
    
    def imprimir(self):
        print("Cuenta de plazo fijo:")
        super().mostrar()
        print(f"Plazo en diás: {self.plazo}")
        print(f"Interés: {self.interes}%")
        self.ganancias_interes()
    
    def ganancias_interes(self):
        ganancia= self.cantidad*self.interes/100
        print(f"Ganancia por interes: {ganancia}")

cajaahorro=CajaAhorra("tito", 3000)
cajaahorro.mostrar()

plazofijo=PlazoFijo("tito", 3000, 30, 0.75)
plazofijo.imprimir()

add=0
for x in range(1, 100):
    add+=x
    print(add)