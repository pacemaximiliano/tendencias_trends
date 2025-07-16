import matplotlib.pyplot as plt
from logs import log_info


def graficar_interes(df, clave):
    """
    Genera un gráfico de línea con la evolución del interés por la palabra clave
    Args:
        df (pd.DataFrame): DataFrame con los datos
        clave (str): Palabra a graficar
    """
    log_info(f"Graficando interés por '{clave}'")
    df[clave].plot(figsize=(10, 5), title=f"Interés por: {clave}", ylabel='Interés', xlabel='Fecha')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def graficar_comparacion(df):
    """
    Genera un gráfico de líneas para comparar el interés entre varias palabras clave
    Args:
        df (pd.DataFrame): DataFrame con múltiples columnas de palabras
    """
    log_info(f"Graficando comparación múltiple")
    df.drop(columns='isPartial', errors='ignore').plot(figsize=(10, 5))
    plt.title("Comparación de interés")
    plt.ylabel("Nivel de interés")
    plt.xlabel("Fecha")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def graficar_region(df, clave):
    """
    Grafica el top 10 de regiones con más interés por la palabra clave
    Args:
        df (pd.DataFrame): DataFrame con datos por región
        clave (str): Palabra
    """
    log_info(f"Graficando interés regional para '{clave}'")
    top_10 = df.sort_values(by=clave, ascending=False).head(10)
    top_10[clave].plot(kind='barh', figsize=(10, 6), title=f"Top regiones para '{clave}'")
    plt.xlabel("Interés (0-100)")
    plt.ylabel("Región")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()