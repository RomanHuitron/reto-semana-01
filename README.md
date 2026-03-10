# Reto Semana 1: Calculadora de Sumas

## Descripcion
Este programa lee datos desde la entrada estandar. El programa realiza la limpieza de caracteres no numericos, trunca los valores decimales a enteros y calcula la suma total por cada linea procesada.

## Instrucciones de uso
Para ejecutar el programa y procesar un archivo de entrada, utilice los siguientes comandos en su terminal:

### Ejecucion basica
python main.py < entrada.txt

### Ejecucion con redireccion a un archivo de salida
python main.py < entrada.txt > salida.txt

### Verificacion de resultados
Si cuenta con un archivo de resultados esperados, puede compararlos usando:
diff salida.txt salida_esperada.txt

## Ejemplo de entrada y salida

**Entrada (entrada.txt):**
1,2,3
1.9,2.1,3.7
1a2,3b,4

**Salida (salida.txt):**
6
6
19

## Autor
Jose Roman Huitron Carranco