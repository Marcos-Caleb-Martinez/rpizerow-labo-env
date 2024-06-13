from gpiozero import LED
from time import sleep

ledVerde = LED(13)
ledRojo = LED(19)
ledAzul = LED(26)

while True:
	sleep(0.25)
	ledVerde.on()
# enciende el led verde por un cuarto de segundo
	sleep(0.25)
	ledVerde.off()
	ledAzul.on()
# luego de medio segundo se apaga el led verde y se enciende el led azul
	sleep(0.25)
	ledVerde.on()
	sleep(0.25)
	ledVerde.off()
	ledAzul.off()
	ledRojo.on()
# luego pasa un segundo y se apagan el led azul y verde y se enciende el rojo
	sleep(0.25)
	ledVerde.on()
	sleep(0.25)
	ledVerde.off()
	ledAzul.on()
	sleep(0.25)
	ledVerde.on()
	sleep(0.25)
# se apagan todos los led
	ledVerde.off()
	ledAzul.off()
	ledRojo.off()



