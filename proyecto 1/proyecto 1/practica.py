import random
import os
import time

temperaturas = []
humedades = []
coordenadas = []
presiones_atmosfericas =[] 

diccionario = {}

def obtener_humedad_temperatura_():
    #genera valores randoms de humedad y temperatura
    humedad = random.randint(0, 100)
    temperatura = random.randint(25, 60)
    return (humedad, temperatura)



def obtener_coordenadas():
     #genera valores randoms de coordenadas
    x = random.randint(00, 100)
    y = random.randint(00, 100)
    return (x,y)

def obtener_presion_atmosferica():
    #genera valores randoms de presion atmosferica
    presion = random.randint(1000, 1500)
    return presion 


while True:
    
    humedad, temperatura = obtener_humedad_temperatura_()
    x, y = obtener_coordenadas()
    presion_atmosferica = obtener_presion_atmosferica()

    humedades.append(humedad)
    temperaturas.append(temperatura)
    coordenadas.append((x,y))
    presiones_atmosfericas.append(presion_atmosferica)

    print("El drone sobrevuela las coordenadas", (x,y), "area de Vermount View")
    
    #if len(temperaturas) > 10 and len(temperaturas) % 10 == 0:
        #print("Ultimos registros Temp:", temperaturas[-10])
        #print("Ultimos registros Hum:", humedades[-10])
        #print("Ultimos registros Pres:", presiones_atmosfericas[-10])


    print("temperatura:",(temperatura), " C")
    print("presion atmosferica:", presion_atmosferica, "hPa")
    print("humedad ambiental:", humedad)
    time.sleep(1)
    
    if humedad > 60:
        print("\nALERTA: Tormenta inminente")
        time.sleep(1)
    elif temperatura > 50:
        print("\nALERTA: Ola de calor inminente")
        time.sleep(1)
    
    
    os.system('cls')

