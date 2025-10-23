import sys, importlib
import pandas as pd
import os
# ruta absoluta de la carpeta donde esta el script (../scripts)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# ruta absoluta de la carpeta data donde se encuntra el dataset (../data)
EXCEL_PATH = os.path.join(SCRIPT_DIR, "..",".", "data","Sample - Superstore.xls")

# creacion de la funcion para cargar los datos
def cargar_datos(path, lista_hojas):
    """
    Carga el dataset de movilidad urbana desde un archivo CSV.

    Args:
        path (str): Ruta al archivo CSV del dataset.

    Returns:
        pd.DataFrame: DataFrame de pandas que contiene los datos cargados.
    """
    print(f"Cargando datos desde: {path}")
    
    dataframe_cargados = {}
    
    try:
        for hoja in lista_hojas:
            print(f"Cargando datos de la hoja: {hoja}")
            df_temporal = pd.read_excel(path, sheet_name=hoja, engine="xlrd")
            dataframe_cargados[hoja] = df_temporal
            print(f"Datos de la hoja '{hoja}' cargados exitosamente.")
        
        print("Datos cargados exitosamente.")
        return dataframe_cargados
    except FileNotFoundError:
        print(f"El archivo no se encontró en la ruta especificada: {path}")
        print(f"segurate de tener el archivo en la carpeta 'data'.")
        return None
    except pd.errors.EmptyDataError:
        print("El archivo está vacío.")
        return None
    except pd.errors.ParserError:
        print("Error al parsear el archivo excel.")
        return None
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

# Este acrchivo se esta ejecuntando directamente por el uuario o esta siendo importada pr otro script 
if __name__ == "__main__":
    # indica en donde esta el archivo de datos
    print(f"Ejecutando el script desde: {os.path.abspath(__file__)}")
    hojas_a_cargar = ['Orders', 'Returns','People']
    diccionario_dataframes = cargar_datos(EXCEL_PATH, hojas_a_cargar)   
    
    # Mostrar las primeras filas del DataFrame cargado
    if diccionario_dataframes is not None:
        for hoja, df in diccionario_dataframes.items():
            print(f"\n===Primeras 5 filas del DataFrame de la hoja: {hoja} ======")
            print(df.head())
            
            print(f"\n=======Información del DataFrame de la hoja: {hoja} ======")
            df.info()
        
