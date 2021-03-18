import os
#from datetime import date
from datetime import datetime
import time

# esperar los 4 minutos desde que inicia el proceso
#time.sleep(240) 

# imagen 01

print(datetime.now())


cuadro = 1
repetir_cuadro = True
while repetir_cuadro:
	# esperar 60 segundos antes de la siguiente secuencia
	time.sleep(15)
	# recorrer bucle para tomar 4 fotos en cada cuadro
	
	i = 1
	repetir_bucle = True
	while repetir_bucle:
	    time.sleep(2)
	    now = datetime.now()
	    format = now.strftime('%d%m%Y-%H%M%S')
	    nombreArchivo=str(cuadro)+'-'+format+'.jpg'
	    os.system('raspistill -r -o '+nombreArchivo)
	    print(nombreArchivo)
	    i = i + 1
	    if i>4:
		    repetir_bucle = False
	
	cuadro = cuadro + 1
	if cuadro > 6 :
	    repetir_cuadro = False
	

print(datetime.now())
print('FIN PROCESO')
