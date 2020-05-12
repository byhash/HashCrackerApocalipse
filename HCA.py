#!/usr/bin/python

import sys, math, hashlib,readline
from time import time, localtime, strftime
from hashlib import md5, sha1, sha224, sha256, sha384 , sha512

########################### CONFIGURACION BASICA #########################

LONGITUD = 12
ALFABETO = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789_-.@!~/\|"

##########################################################################
#header       
print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdmdmmdmmmmmmmmmdyooydmmmmmmdmddddmdmddddmmmmmmmmmmmmdmmmmmmmmmmmmmmm")
print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdmmmmmmmmmmdhyo/------:+shmmmmdmdddddddddddddddddmmddddddmmmmmmmddddd")
print("mmmmmmmmmmmmmmmmmmmmmmmdmdmmmmmmmmmmmmmhs+:--------------:+shdmmmmmdddmmdddmmmmmmmmmmmmmmmdmmmmmmmmm")
print("mmmmmmmmmmmmmmmmmmmmmmdmddmmmmmmmmmhs+:-----------------------/oydmmdmdddhddddmmmmmmmdddmmdmdmmmmmmm")
print("mmmmmmmmmmmmmmmmmmmmmmmmmdmmmmmho/-:o:---:o:------------:o:---:+/:/ohdddddddddmmmmddddddddddddmmmmmm")
print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm/---:s+ossos/------------/soos+/o:--:/dhhhhhhhhhhddhhhhhddddhhddddddd")
print("mmmmmddmdddddddddhdddddddmmmmmm/----ommmddd/------------/hddddds----/dddhddddddddddddddddddddddddmmm")
print("mmmmmmmmmmmmmmdddddddmmdhdddddd/--:+dmhdmmdh------------hdhhhhhh+---:dddddddhddddhhhhhhhhhhhhddddmmm")
print("mmmmmmmmmmmmmmmmmdddmmmmmddddhh/:hoydddhhhdd/h/------/y/yyyyyyyyo/s::hhhhhhyyhhhhyyyyyyyyyyyyyhhhdmm")
print("mmmmmmmmmmmmmmmmmmmmdmmmmdmmddd/---+hhhddddy-:--------:-sdddddddo---:ddddddddddmmdddddddddddddmmmmmm")
print("mmmmmmmmmmmmmmmmmmmmmmmdddmmmmm/----sddddds--------------sdddmdy----:mmmmmmmdmmmmmdmmmmmmmmmmmmmmmmm")
print("mmmmmmmmmdddddddddmddddddddmmmm/----s++o++s/------------:s++oooy:---/mmmmddmddmmmmmmmmmmmmmmmmmmmmmm")
print("mmmmmmmddhhyhhhhhhhhhhhhhhddddhy+:--+:----+:----+os+----:+:---:o---+hmdddddddmmmmmmmmmmdhdmmmmmmmmmm")
print("mmmmmdddmdddddddddddddddddddddddddhs++yo--------++++--------oyo+shmdddmmddmmmmmmmmmmmmmdhdmmmmmmmmmm")
print("mmmmmmmmmmddddddddmmmddmdmdmmdmdmdmmmmdd---//----------:/---hmmmmmmddddmmmmmmmmmmmmmmmmmdmmmmmmmmmmm")
print("mmmdmmmmmmmmddmmmdmddddddmdddddddddddddd+:-oo--++--+o--+s-:+mmmmdddddddmmmmmmmmddmddddddmmmmmmmmmmmm")
print("mmmmmmdmmmmmmmmmdmddddddddddddmddddhdddddmddy:-os--os-:sddmmmdddddmmmmmmmmmmmmddmmmmmmmmmmmmmmmmmmmm")
print("mmmmmmmmmmddddmmmmmmddhddddddddmmmddddddmdddddddy//yddmdmddmmdmmdmmmmmmmmmmmmmmmmmmmmmmmmmmmddmmmmmm")
print("mmmmmmmmmmmmmmmmmmmmmmmmmmmddmmmmmmmmmmmmmdhddmddddddddddddmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdddddmm")
print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print "+              HASH CRACKER APOCALIPSE v 1.0           +"
print "+                   #adm@T3am-Whoami                   +"
print "+                  #Created : byhash :)                +"
print "+     #Algoritmos: md5-sha1-sha256-sha384-sha512       +" 
print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
HASH_BUSCADO = raw_input("Inserte hash:")
TYPE  =  input ("Inserta el tipo de hash:")
info = raw_input("Presiona Enter Para iniciar el Ataque ^_^")

########################### CONFIGURACION EXTRA ####################

CALCULAR_TIEMPO_RESTANTE = True

LLAMAR_EVENTO = False

GENERAR_FICHERO = True
DESTINO_FICHERO = "passdic.txt"

BUSCAR_HASH = True
HASH_ALGORITMO = (TYPE) # Opciones: md5, sha1, sha224, sha256, sha384, sha512
HASH_BUSCADO = (HASH_BUSCADO)

#len

if len(HASH_BUSCADO) == 32:

   print ("Tu hash es un:MD5")

elif len(HASH_BUSCADO) == 40:
 
   print ("Tu hash es un:SHA1")

elif len(HASH_BUSCADO) == 56:

        print ("Tu hash es un:SHA224")

elif len(HASH_BUSCADO) == 60:

         print ("Tu hash es un:SHA256")

elif len(HASH_BUSCADO) == 96:

         print ("Tu hash es un:SHA384")

elif len(HASH_BUSCADO) == 128:

         print ("Tu hash es un:SHA512")


####################################################################

########################## CALLBACK ###############################

# ES UN CALLBACK MODIFICABLE SEGUN LA FUNCIONALIDAD A IMPLEMENTAR
def eventoPalabraGenerada(palabra):
  print palabra

####################################################################

########################## FUNCIONES ###############################

def getVariacionesConRepeticion(ALFABETO , LONGITUD):
  sumatorio = 0
  for i in range(LONGITUD):
    producto = 1
    for j in range(i+1):
      producto = producto * len(ALFABETO)
    sumatorio = sumatorio + producto
  return sumatorio

####################################################################

##################### VARS AUXILIARES ##############################

variacionesConRepeticion = getVariacionesConRepeticion(ALFABETO , LONGITUD)
PERIODO_MOSTRAR_ESTADISTICAS = 600000
inicioReloj = time()
cont = 0
progreso = 0

####################################################################

if GENERAR_FICHERO:
  f = open(DESTINO_FICHERO,"w")

LONGITUD_MAXIMA = LONGITUD
LONGITUD = 1
while LONGITUD <= LONGITUD_MAXIMA:
  try:
    contadores = []                                   # ponemos los contadores a 0
    for i in range(LONGITUD):
      contadores.append(0)

    fin = False
    while not fin:

      palabra=[]                                      # Creas una lista vacia (y liberas de paso)
      for i in range(LONGITUD):
        palabra.append(ALFABETO[contadores[i]])       # Vas metiendo al final letra a letra
      palabra_formada = "".join(palabra)

      if GENERAR_FICHERO:
        f.write("%s\n" % palabra_formada)

      if LLAMAR_EVENTO:
        eventoPalabraGenerada(palabra_formada)        # Envias a tu callback tada la lista unida

      if BUSCAR_HASH:
        # algorimos disponibles:
        HASH = HASH_ALGORITMO(palabra_formada).hexdigest()
        if HASH == HASH_BUSCADO:
          print "\n\nDesencriptado el HASH %s !!!!\n" % HASH
          print "Su hash Desencriptado es: \"%s\"\n\n" % palabra_formada
          raise KeyboardInterrupt

      if CALCULAR_TIEMPO_RESTANTE:
        if (cont % PERIODO_MOSTRAR_ESTADISTICAS == 0) and (cont != 0):
          try:
            progreso = cont*100.0 / variacionesConRepeticion              # porcentaje hasta ahora
            finReloj = time() - inicioReloj                               # finReloj es lo que esta tardando el calculo
            velocidad = cont / finReloj                                   # palabras procesadas por segundo
            estimado = finReloj * variacionesConRepeticion / cont         # es lo que se estima en realizar todo el proceso
            restante = estimado - finReloj                                # es lo que se estima en realizar lo restante
            if restante > 60:
              restante = restante / 60                                    # lo pasamos a minutos
              if restante > 60:
                restante = restante / 60                                 # lo pasamos a horas
                unidad = "horas"
              else:
                unidad = "mins"
            else:
              unidad = "segs"
            sys.stderr.write("%.2fQuedan %.2f %s. La velocidad es de %.2f palabras/seg\n" % (progreso, restante, unidad, velocidad))
          except ZeroDivisionError:
            pass

      cont = cont + 1
      actual = LONGITUD - 1                                             # Pongo actual a la derecha del todo
      contadores[actual] = contadores[actual] + 1                       # Sumo 1 a las unidades

      while(contadores[actual] == len(ALFABETO)) and not fin:           # Propago el carry
        if(actual == 0):
          fin = True                                                    # FIN
        else:
          contadores[actual] = 0                                        # reinicia el actual contador
          actual = actual - 1                                           # avanza a la izquierda
          contadores[actual] = contadores[actual] + 1                   # y le sumo 1

    LONGITUD = LONGITUD + 1                                             # combinaciones para uno menos

  except KeyboardInterrupt:
    sys.stderr.write("Procesorrumpido\n")
    fin = True                                                          # Fuerzo las condiciones de salida
    LONGITUD = LONGITUD_MAXIMA+1

if cont == variacionesConRepeticion:
  sys.stderr.write("Terminado00%\n")
else:
  if CALCULAR_TIEMPO_RESTANTE:
    sys.stderr.write("Terminado.2f%%\n" % progreso)
  sys.stderr.write("Realizadasombinaciones de %d\n" % (cont, variacionesConRepeticion))

if GENERAR_FICHERO:
  f.close()


