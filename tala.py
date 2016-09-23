#coding=utf-8



import time

password= "guajolotitos"
correcto= 0
intentos= 1

print ("Bienvenido al centro educativo patria.")


while (correcto ==0 ) & ( intentos<= 4 ):
	intento=input ("introduce tu contraseña : ")
	if intento == password:
			correcto = 1
			print ( "tu contrasena es correcta!" )
	else:
			time. sleep(5)
			print ("la contraseña que has introducido es incorrecta")
			intentos = intentos +1
			if intentos > 4 :
				print ("has intriducido demaciadas contraseñas" )
			     
			     
