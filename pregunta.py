"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import re
import pandas as pd
from datetime import datetime

df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col = 0)

def clean_data():
    df.dropna(axis = 0, inplace = True)
    df.drop_duplicates(inplace = True)

    for columna in ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'línea_credito', 'barrio']:
        df[columna] = df[columna].str.lower()
        
    for columna in ['idea_negocio', 'línea_credito', 'barrio']:
        df[columna] = df[columna].apply(lambda x: x.replace('_', ' '))
        df[columna] = df[columna].apply(lambda x: x.replace('-', ' '))

    for i in ["\$[\s*]",",","\.00"]:
        df['monto_del_credito'] = df['monto_del_credito'].str.replace(i, "")

    df['monto_del_credito'] = df['monto_del_credito'].astype(int)
    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(float)

    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(lambda x: datetime.strptime(x, "%Y/%m/%d") if (len(re.findall("^\d+/", x)[0]) - 1) == 4 else datetime.strptime(x, "%d/%m/%Y"))

    df.drop_duplicates(inplace = True)

    return df