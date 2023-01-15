# import machine, time, framebuf, pyb


# scl = machine.Pin("X9")
# sda = machine.Pin("X10")

# i2c = machine.I2C("X")

# lista = i2c.scan()
# print("Dirección empleada:", lista[0])

# y4= machine.Pin("Y4")
# adc = pyb.ADC(y4)
# print(adc)



# lcd = framebuf.FrameBuffer(bytearray(64 * 32 // 8), 64, 32, framebuf.MONO_HLSB)
# print("Lcd =>>",lcd)
# # buf pelota
# pelota = framebuf.FrameBuffer(bytearray(4*4//8),4,4,framebuf.MONO_HLSB)

# x1 = 11
# y1 = 0
# x2 = 52
# y2 = 0
# ancho = 1
# alto = 32



# # pelota
# pelota.fill(0)
# # fill_rect(x,y,ancho,alto,color)
# pelota.fill_rect(0,0,4,4,1)  # rectángulo al que le quitamos las esquinas

# la x la determinaremos segun la posicion del adc
# borde izquierdo 60
# derecho = 255
# 255/60 = 4.25
# x=19
# lcd.blit(pelota,x,25)
# i2c.writeto(8,lcd)

# bucle plara movimiento
# lista = []
# for i in range(255,4):
#     print("esto es i: ",i)
#     if i>59:
#         lista.append[i]

lista = list(range(60, 256, 4))
print(lista)

# anterior = 0
# while not pyb.Switch().value():
#     lectura = adc.read()
#     # aqui vemos la pocicion del adc
#     if lectura != anterior:
#         # cambiamos la posicion para igualarla a la de adc
#         anterior = lectura
#         # 4.47 = maximo adc(255)/tope de la cara 57(64-7pixeles de la cara)
#         x = int(lectura/4.25)
#         print("- Lectura adc:",lectura,"x",x)
#         lcd.fill(0)
        
        
#         # linea izquierda
#         lcd.rect(x1,y1,ancho,alto,1)
#         i2c.writeto(8,lcd)
#         # linea derecha
#         lcd.rect(x2,y2,ancho,alto,1)
#         i2c.writeto(8,lcd)
        
        
#         # Dibuja otro FrameBuffer encima del actual
#         # blit(buf,x,y,clave)
#         lcd.blit(pelota,x,14)
#         # dibuja el objeto el la pantalla
#         i2c.writeto(8,lcd)
#     time.sleep_ms(300)


