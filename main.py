import sys

def limpiar_valor(valor):
    # Regla 6: Quitar espacios
    valor = valor.strip()
    
    # Regla 5: Solo dejar números, puntos y el signo menos
    caracteres_validos = "0123456789.-"
    limpio = "".join(c for c in valor if c in caracteres_validos)
    
    # Si después de limpiar no queda nada (ej: "abc"), devolvemos "0"
    return limpio if limpio else "0"

def procesar_linea(linea):
    # Regla 1: Si la línea está vacía o solo tiene espacios
    if not linea.strip():
        return 0
    
    # Separar por comas
    elementos = linea.split(",")
    suma_total = 0
    
    for item in elementos:
        texto_limpio = limpiar_valor(item)
        try:
            # Regla 4: Convertir a float y TRUNCAR con int()
            numero = int(float(texto_limpio))
            suma_total += numero
        except ValueError:
            # Si algo falla (ej: "1.2.3"), sumamos 0
            suma_total += 0
            
    return suma_total

def main():
    # Leer de la entrada estándar línea por línea
    for linea in sys.stdin:
        # Quitar el salto de línea del final (\n)
        linea = linea.replace("\n", "")
        resultado = procesar_linea(linea)
        # Imprimir solo el resultado
        print(resultado)

if __name__ == "__main__":
    main()