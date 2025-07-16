# Proyecto Final: Tendencias de Google en Python

Este proyecto permite consultar y analizar el interés en palabras clave utilizando **Google Trends**, a través de `pytrends`, una librería no oficial de Python.

Se trata de una aplicación interactiva por consola que permite:
- Visualizar la evolución del interés de una palabra en el tiempo
- Comparar dos palabras clave
- Ver términos relacionados
- Exportar datos en formato CSV

---

## Archivo de salida (csv)
Se exporta un archivo con datos en formato CSV
Columnas
    - date
        fecha correspondiente al punto temporal de la consulta
    - término de búsqueda (palabra a buscar)
        Es el valor de popularidad para esa palabra clave en la fecha correspondiente
        Rango de 0 a 100:
            100 = momento de mayor interés.
            0 = bajo o nulo interés relativo (no absoluto).
        No es número absoluto de búsquedas, sino normalizado por Google
    - isPartial
        Indica si el dato es parcial/incompleto
            True = el dato está en curso (por ejemplo, la semana aún no terminó).
            False = dato cerrado y confirmado.


## Requisitos

- Python 3.8 o superior
- Entorno virtual (recomendado)

### Dependencias (instalación automática)

```bash
pip install -r requirements.txt