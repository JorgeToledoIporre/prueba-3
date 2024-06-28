asientos= ("asiento comun", "espacio adicional para piernas","no reclina")#tupla de precios de asientos
f=[["F","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x",],
["E","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x",],
["D","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x",],
["C","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x",],
["B","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x",],
["A","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x",]]
numeros=["/","1","2","3","4","5","6","7","8","9",10,"11",12,"13","14",15,"16",17,18,"19","20",21,"22",23,"24",25,"26",27,28,"29","30",31,"32",33]
rut=[]
cont1=0
cont2=0
cont3=0
def comprar_pasajes(cont1=0,cont2=0,cont3=0):
    delimite=int(input("cuantos asientos desea comprar?"))
    if delimite>0:
        for i in range(delimite):
            print(f[0],"\n",f[1],"\n",f[2],"\n",numeros,"\n",f[3],"\n",f[4],"\n",f[5],"\nlas x son asientos libres,0 son los ocupados")
            linea=input("qué linea desea comprar?")
            fila=int(input("qué fila desea comprar?"))
            for l in range (5):
                if linea in f[l]:
                    f[l][fila]="0"
                    print(f[l])
            print("qué tipo de asiento va a requerir?(asiento comun, espacio adicional para piernas o no reclina)")
            while True:
                TipAsiento=input()
                if TipAsiento in asientos:
                    if TipAsiento== "asiento comun":
                        cont1 = cont1+1
                    elif TipAsiento == "espacio adicional para piernas":
                        cont2 = cont2+1
                    elif TipAsiento =="no reclina":
                        cont3= cont3+1
                    break
                else:
                    print("ingrese un asiento valido")

            print("ingrese el rut del asiento",i+1,"sin puntos ni digito verificador")
            rut.append(int(input()))
    print(cont1)
    return cont1
def mostrar_ubicacion():
    print(f[0],"\n",f[1],"\n",f[2],"\n",numeros,"\n",f[3],"\n",f[4],"\n",f[5],"\nlas x son asientos libres,0 son los ocupados")
    return
def listado_pasajeros():
    rut.sort
    op=int(input("1 para listar todos los pasajeros, 2 para buscar uno en contreto o 3 para cancelar operacion"))
    if op==1:
        print(rut)
    elif op==2:
        op2=int(input("ingrese el rut"))
        if op2 in rut:
            print("el rut si está registrado")
        else:
            print("el rut no está registrado")
    return
def mostrar_ganancias():
    print("tipo de asiento                      cantidad                total")
    print("Asiento comun            60.000     ",cont1,             cont1*60000)
    print("Asiento para piernas     80.000     ",cont2,             cont2*80000)
    print("no reclina               50.000     ",cont3,             cont3*50000)
    return
def cambiar_rut ():
    n=int(input("ingrese el rut que desea cambiar"))
    if m in rut:
        for m in rut:
            if rut[m]==n:
                rut[m]=n
    else:
        print("no existe ese rut")
        
def main():
    print("qué desea hacer?\n 1.-comprar pasajes\n 2.- mostrar ubicaciones disponibles\n 3.-ver listado de pasajeros\n 4.-reasignar pasajeros\n 5.-mostrar ganancias \n6.salir")
    opcion=int(input())
    if opcion==1:
        comprar_pasajes()
    elif opcion==2:
        mostrar_ubicacion()
    elif opcion==3:
        listado_pasajeros()
    elif opcion==4:
        cambiar_rut()
    elif opcion==5:
        mostrar_ganancias()
    elif opcion==6:
        exit