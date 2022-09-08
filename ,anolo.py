print("Bienvenida a comidas rapidas PROCOM :)")
#GENERAR FACTURA, DECIDIR COMO PARAR, STOCK
#creando diccionario
food={"combo":20000,"combo2":25000,"combo3":18000,"combo4":24500,"papas":3000,"jugos_naturales": 7000,"cerveza":3500,"agua":4000,"gaseosas":2500}
for x, y in food.items():
    print(x, y)
#generar menu d eopciones
condicion = int(input("Enter ur option 1.vender un producto,2.Eliminar un producto comprado 3.Generar factura 4.Cerrar el chuzo"))
#Aqui debi de haber crado una funcion para cuando termien de pedir por ejemplo el combo, vuelva aca y vuelva a pedir otra cosa
if condicion == 1:
   option_1=int(input("Que quieres vender:1.combo1,2.combo2,3.combo3,4.combo4,5.papas,6.jugos naturales,7.cerveza,8.agua,9.gaseosas"))
   
#Funcion para eelgir la opcion e ir pidiendo con un maximo de 5 por el mismo producto
def sell_product(option):
   if option == 1:
        cantidad =  int(input("cantidad?"))
        precio_final=20000*cantidad
        if cantidad == 5:
             print("Ya pediste la cantidad maxima")
        else:
             print("Listo")
             return precio_final
   elif option ==2:               

 option_1=int(input("Que quieres vender:1.combo1,2.combo2,3.combo3,4.combo4,5.papas,6.jugos naturales,7.cerveza,8.agua,9.gaseosas"))
sell_product(option_1)

#Debi de haber creado un contador para que ese return precio_final fuera aumentando sin borrarse

