Reto Semana 1: Calculadora de Sumas
Descripción
Este programa implementa el patrón fundamental de ciencia de datos (ETL) para procesar una pipeline de ventas. El programa lee líneas de la entrada estándar, limpia caracteres basura, trunca decimales a enteros y muestra la suma total por línea.

Instrucciones de uso
Para ejecutar el programa en su ThinkPad L14 y guardar los resultados:

Guardar la salida en un archivo (Requerido para evaluación):

# En Git Bash / Linux
python main.py < entrada.txt > salida.txt

# En Windows (PowerShell)
Get-Content entrada.txt | python main.py > salida.txt
Ver y guardar al mismo tiempo:

# Usa 'tee' para ver el resultado en pantalla y guardarlo a la vez
python main.py < entrada.txt | tee salida.txt
Ejemplo de entrada y salida
Entrada (entrada.txt):


1,2,3
1.9,2.1,3.7
1a2,3b,4
Salida (salida.txt):

6
6
19
Autor
Jose Roman Huitron Carranco