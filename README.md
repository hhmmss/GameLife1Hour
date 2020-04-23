# GameLife1Hour

Juego de la Vida programado en emnos de 1 hora, recogiendo el reto de @DotCSV.

# Dependencias
* Python 3.6
* pip install numpy
* pip install pygame

# Uso
* [Escape] Reinicia con un mapa vacio
* [R] Reinicia con un mapa aleatorio
* [Espace] Para o reinicia la simulación
* [mouse click] Pone o quita célula

# Generar un video
Dentro del directorio screenshots se guardan las imagenes de la simulación.

Para crear una película con estas imágenes:

 $ ffmpeg.exe -f image2 -i ./%4d.jpg gamelife1hour.mp4
