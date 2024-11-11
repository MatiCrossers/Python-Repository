#Productos de la panaderia
CODPROD=["PAN01","PAN02","PAN03","PAN04","PAN05"]
NOMPROD=["Pan De Molde","Baguette","Croissant","Pan Integral","Donut"]
PREPROD=[1.5,2.0,1.8,1.2,0.5]
CANT=[50,30,20,40,100]

#Productos de la panaderia
CART=[]
TOTAL=0.0

print("Bienvenido a la panaderia Joshe!")

#Mostrar productos disponibles
print("PRODUCTOS DISPONIBLES")
for i in range(len(CODPROD)):
    print(CODPROD[i],"-",NOMPROD[i],"-S/.",PREPROD[i],"(Stock",CANT[i],")")

#Procesos de compra
while True:
    COD=input("Ingrese El Codigo del producto (o 'salir' para finalizar):").upper()
    if COD=='SALIR':
        break

    if COD in CODPROD:
        for i in range(len(CODPROD)):
            if CODPROD[i] == COD:

CANCOMPRAR=int(input("¿Cuanto desea comprar?"))
if CANCOMPRAR <= CANT[i]:
    CART.append((NOMPROD[i],PREPROD[i],CANCOMPRAR))
    CANT[i]-=CANCOMPRAR #ACTUALIZAR STOCK
    TOTAL+=PREPROD[i]*CANCOMPRAR
    print("Añadido:",NOMPROD[i],"X",CANCOMPRAR)
    else:
        print("No Hay Stock Disponible")

print("--RESUMEN DE LA COMPRA--")
for item in CART:
    print(item[0],"-S/.",item[1],"x",item[2])

print("TOTAL A PAGAR:S/.",TOTAL)
print("Gracias por tu compra")
