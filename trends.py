from pytrends.request import TrendReq
import pandas as pd
import os
from logs import log_info, log_error, log_export

#Genero una instancia del obj TrendReq - Interacción con Google Trends (mediante pytrends)
pytrends = TrendReq(hl='es-ES', tz=180)

def interes_por_palabra(clave, pais='AR'):
    """
    Consulta el interés a lo largo del tiempo para una palabra clave en un país específico
    Args:
        clave (str): Palabra clave a buscar
        pais (str): Código del país (ej. 'AR', 'US','WORLD')
    Returns:
        pd.DataFrame: Datos de interés a lo largo del tiempo
    """
    log_info(f"Búsqueda de interés por palabra: '{clave}' en país '{pais}'")
    pytrends.build_payload([clave], geo=pais.upper())
    try:
        return pytrends.interest_over_time()
    except Exception as e:
        log_error(f"Error al obtener interés por palabra: {e}")
        return pd.DataFrame()

def comparar_claves(clave1, clave2, pais='AR'):
    """
    Compara el interés a lo largo del tiempo entre dos palabras clave.
    Args:
        clave1 (str): Primera palabra
        clave2 (str): Segunda palabra
        pais (str): Código del país
    Returns:
        pd.DataFrame: Datos comparativos de ambas palabras
    """
    claves = [clave1, clave2]
    pytrends.build_payload(claves, geo=pais.upper())
    try:
        return pytrends.interest_over_time()
    except Exception as e:
        print(f"Error: {e}")
        return pd.DataFrame()

def interes_por_region(clave, pais='AR'):
    """
    Devuelve un DataFrame con el interés por región (provincia o país).
    Args:
        clave (str): Palabra
        pais (str): Código del país (ej. 'AR', 'US').
    Returns:
        pd.DataFrame: Datos ordenados por regiones con interés mayor a 0
    """
    log_info(f"Consulta de interés por región para '{clave}' en país '{pais}'")
    try:
        pytrends.build_payload([clave], geo=pais.upper())
        df = pytrends.interest_by_region()
        df = df[df[clave] > 0]  # Elimina regiones con cero interés
        df_ordenado = df.sort_values(by=clave, ascending=False)
        return df_ordenado
    except Exception as e:
        log_error(f"Error en interes_por_region: {e}")
        return pd.DataFrame()

def exportar_resultado_csv(clave, pais='AR'):
    """
    Exporta el interés por palabra clave a un archivo CSV
    Args:
        clave (str): Palabra a consultar
        pais (str): Código del país
    """
    df = interes_por_palabra(clave, pais)
    if not df.empty:
        os.makedirs("csv", exist_ok=True)
        nombre_archivo = f"interes_{clave}_{pais}.csv".replace(" ", "_").lower()
        df.to_csv(nombre_archivo, index=True)
        log_export(nombre_archivo)
        print(f"Archivo exportado como: {nombre_archivo}")
    else:
        log_info(f"No se exportó CSV para '{clave}' en '{pais}' (DataFrame vacío)")
        print("No hay datos para exportar")