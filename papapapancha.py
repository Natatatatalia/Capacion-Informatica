#coding=utf-8
#programa para tomar la orden 

costo=0
pedido=1
print ("Bienvenido a Carls Jr.")
orden= input("Cual es tu orden?") 
print("""1. famus star $90
2. papas grandes $40
3. santa fe $100
4. soda grande $30
5. salir """)

while(pedido<5):
    pedido = int(input("Dame tu pedido:"))

    if(pedido==1):
      costo= costo+90
    elif(pedido==2):
      costo= costo+40
    elif(pedido==3):
      costo=costo+ 100 
    elif(pedido==4):
      costo= costo+30 

    print("tu orden es de un total de %s" %(costo))
    
else:
		
		print("gracias")


