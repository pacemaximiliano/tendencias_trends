"""
main.py

Script principal para comparar tendencias en Google y visualizar resultados.
Incluye logging de todas las acciones.
"""

from trends import (
    interes_por_palabra,
    comparar_claves,
    interes_por_region,
    exportar_resultado_csv
)
from visuales import(
    graficar_interes,
    graficar_comparacion,
    graficar_region
)
from logs import log_info, log_error


def main():
    """
    Ejecuta el menú principal de la aplicación.
    Permite al usuario elegir entre distintas opciones para consultar datos y visualizarlos
    """
    log_info("Programa iniciado")
    print("\n--- Proyecto de análisis de tendencias en Google Trends ---")
    print("1. Consultar trends por una palabra clave")
    print("2. Comparar dos palabras clave")
    print("3. Ver trends por región")
    print("4. Exportar trends a CSV")

    opcion = input("\nSeleccione una opción (1 a 4): ").strip()
    log_info(f"Opción seleccionada por el usuario: {opcion}")
    
    if opcion == "1":
        clave = input("Ingrese la palabra clave: ").strip()
        pais = input("Código del país (ej: AR, US): ").strip().upper()
        log_info(f"Ingreso palabra clave: '{clave}', país: '{pais}'")
        df = interes_por_palabra(clave, pais)
        if df.empty:
            log_info(f"Resultado vacío para '{clave}' en '{pais}'")
            print("No se encontraron datos")
        else:
            #print(df.tail())
            graficar_interes(df, clave)

    elif opcion == "2":
        clave1 = input("Primera palabra clave: ").strip()
        clave2 = input("Segunda palabra clave: ").strip()
        pais = input("Código del país (ej: AR, US): ").strip().upper()
        log_info(f"Comparación entre '{clave1}' y '{clave2}' en país '{pais}'")
        df = comparar_claves(clave1, clave2, pais)
        if df.empty:
            log_info("Comparación no devolvió resultados")
            print("No se encontraron datos")
        else:
            #print(df.tail())
            graficar_comparacion(df)

    elif opcion == "3":
        clave = input("Palabra clave para ver interés por región: ").strip()
        pais = input("Código del país (ej: AR, US): ").strip().upper()
        log_info(f"Consulta de interés por región: '{clave}' en '{pais}'")
        df = interes_por_region(clave, pais)
        if df.empty:
            log_info("No se encontraron datos regionales")
            print("Resultado vacío en interés por región")
        else:
            print("\n Top regiones con mayor interés:")
            #print(df.head(5))
            graficar_region(df, clave)

    elif opcion == "4":
        clave = input("Palabra clave para exportar interés a CSV: ").strip()
        pais = input("Código del país (ej: AR, US): ").strip().upper()
        log_info(f"Exportar a CSV: palabra='{clave}' país='{pais}'")
        exportar_resultado_csv(clave, pais)
    
    else:
        log_error(f"Opción inválida seleccionada: {opcion}")
        print("Opción no válida")

if __name__ == "__main__":
    main()