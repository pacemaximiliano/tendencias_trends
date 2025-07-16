"""
logs.py

Módulo para la configuración de logging del programa.
Permite registrar acciones, errores y exportaciones en un archivo de log.
"""
import logging
import os
from datetime import datetime

os.makedirs("logs", exist_ok=True) # Crear carpeta de logs si no existe

# Configurar logging
logging.basicConfig(
    filename=f"logs/actividad.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_info(mensaje):
    """
    Registra un mensaje informativo en el log.
    Args:
        mensaje (str): Mensaje a registrar.
    """
    logging.info(mensaje)

def log_error(mensaje):
    """
    Registra un mensaje de error en el log.
    Args:
        mensaje (str): Mensaje a registrar.
    """
    logging.error(mensaje)

def log_export(nombre_archivo):
    """
    Registra la exportación de un archivo CSV en el log.
    Args:
        nombre_archivo (str): Nombre del archivo exportado
    """
    logging.info(f"Archivo CSV exportado: {nombre_archivo}")
