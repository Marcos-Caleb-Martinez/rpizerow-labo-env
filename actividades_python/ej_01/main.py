
from gpiozero import LED, Button
from signal import pause

# Configuración del LED en el pin GPIO 26 y del botón en el pin GPIO 18
led = LED(26)
button = Button(18)

# Asignación de las funciones de devolución de llamada a los eventos del botón
button.when_pressed = led.on
button.when_released = led.off

# Mantener el programa en ejecución hasta recibir una señal 
pause ()
