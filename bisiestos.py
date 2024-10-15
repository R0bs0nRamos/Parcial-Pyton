'''
Un año bisiesto es un año solar en el que se produce la intercalación periódica de un día adicional en el propio año, 
recurso utilizado en casi todos los calendarios solares (como el juliano y el gregoriano) para evitar el cambio de estaciones. 
Para corregir este cambio, se intercalan años «normales» de 365 días (cada cuatro años) con años «bisiestos» de 366: 
el día extra se inserta en el mes de febrero, el más corto del año, que en los años bisiestos llega a contar 29 días en lugar de 28. 
De esta forma es posible obtener una duración media del año igual a un número no entero de días.

Cualquier año divisible por 4 es un año bisiesto: por ejemplo, 1988, 1992 y 1996 son años bisiestos.
Sin embargo, hay un pequeño error de cálculo que debe tenerse en cuenta. Para eliminar este error, el calendario gregoriano estipula que 
un año que es divisible por 100 (por ejemplo, 1900) es un año bisiesto solo si también es divisible por 400.
'''

'''
Descripción general del programa:

Solicite al usuario que ingrese dos años.
Valide las entradas para asegurarse de que sean números enteros y que el primer año no sea mayor que el segundo.
Calcula cuántos años bisiestos hay entre los dos años (inclusive).
Muestra el número y la lista de años bisiestos encontrados.
Ofrecer al usuario la opción de realizar otra consulta o cerrar el programa.
'''

'''
Recuperatorio de parcial: 
Escribir un programa que pida 2 años y escriba cuántos años bisiestos hay entre esas 2 fechas (incluidos los 2 años). 
Al finalizar debería indicar cuáles son los bisiestos.
'''


def es_bisiesto(anio):
    """Determina si un año es bisiesto."""
    return (anio % 4 == 0) and (anio % 100 != 0 or anio % 400 == 0)

def obtener_años_bisiestos(inicio, fin):
    """Retorna una lista de años bisiestos entre inicio y fin (inclusive)."""
    return [anio for anio in range(inicio, fin + 1) if es_bisiesto(anio)]

def solicitar_años():
    """Solicita al usuario ingresar dos años y los valida."""
    while True:
        try:
            anio1 = int(input("Ingrese el primer año: "))
            anio2 = int(input("Ingrese el segundo año: "))
            if anio1 > anio2:
                print("Error: El primer año debe ser menor o igual al segundo año. Inténtelo de nuevo.")
                continue
            return anio1, anio2
        except ValueError:
            print("Error: Por favor, ingrese un número válido para los años.")

def realizar_consulta():
    """Realiza una consulta de años bisiestos según la entrada del usuario."""
    anio_inicio, anio_fin = solicitar_años()
    bisiestos = obtener_años_bisiestos(anio_inicio, anio_fin)
    cantidad = len(bisiestos)
    
    print(f"\nEntre los años {anio_inicio} y {anio_fin} hay {cantidad} año(s) bisiesto(s).")
    if cantidad > 0:
        print("Años bisiestos encontrados:")
        print(", ".join(map(str, bisiestos)))
    print()

#Función principal del programa.
def main():
    print("Bienvenido al contador de años bisiestos.")
    while True:
        realizar_consulta()
        while True:
            respuesta = input("¿Desea realizar otra consulta? (s/n): ").strip().lower()
            if respuesta == 's':
                print()
                break
            elif respuesta == 'n':
                print("\nGracias por usar el programa. ¡Hasta luego!")
                return
            else:
                print("Respuesta inválida. Por favor, ingrese 's' para sí o 'n' para no.")

#if __name__ == "__main__": comprueba si el script se está ejecutando directamente.
if __name__ == "__main__":
    main()
'''
Cómo funciona:

__nombre__:
En Python, cuando se ejecuta un script directamente, la variable especial __name__ se establece en "__main__".
Si el script se importa como un módulo en otro script, __name__ es el nombre del módulo.
Condición:
if __name__ == "__main__": comprueba si el script se está ejecutando directamente.
Acción:
Si es verdadero, llame a la función main() para iniciar el programa.
Esto permite reutilizar el código como módulo sin ejecutar el programa principal automáticamente.
'''


