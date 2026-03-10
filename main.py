import sys

def limpiar_valor(valor):
    # regla 6: quitar los espacios
    valor = valor.strip()
    
    # regla 5: solo dejar numeros, puntos y el signo menos
    caracteres_validos = "0123456789.-"
    limpio = "".join(c for c in valor if c in caracteres_validos)
    
    # si despues de limpiar no queda nada entonces devolvemos "0"
    return limpio if limpio else "0"

def procesar_linea(linea):
    # regla 1: si la línea esta vacia o solo tiene espacios
    if not linea.strip():
        return 0
    
    # separamos con comas
    elementos = linea.split(",")
    suma_total = 0
    
    for item in elementos:
        texto_limpio = limpiar_valor(item)
        try:
            # regla 4: conrvrtir a float y truncar con el int
            numero = int(float(texto_limpio))
            suma_total += numero
        except ValueError:
            # si algo falla sumamos 0
            suma_total += 0
            
    return suma_total

def main():
    # leemos solo de la entrada estandar línea por línea
    for linea in sys.stdin:
        # quitamos el salto de linea del final (\n)
        linea = linea.replace("\n", "")
        resultado = procesar_linea(linea)
        # imprimimos solo el resultado
        print(resultado)

if __name__ == "__main__":
    main()