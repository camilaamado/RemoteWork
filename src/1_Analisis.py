# ====================================================================================================================================
#                                                      Exploracion de datos 
# ====================================================================================================================================


# importar librerías
import pandas as pd

# cargar datos
dataset = pd.read_csv("/home/mario/Documents/RemoteWork/Data/Raw/Remote_Work.csv") 


#============================================
# 1. Exploración de los Datos
#============================================

# Ver la cantidad de filas y columnas del dataset
print(f"El dataset tiene {dataset.shape[0]} filas y {dataset.shape[1]} columnas.")

# Ver las primeras filas del dataset para obtener una visión general
print("Las primeras filas del dataset son:")
print(dataset.head())

# Obtener información general del dataset (tipos de datos, valores nulos, etc.)
print("Información general del dataset:")
print(dataset.info())

# Verificar los tipos de datos
print("Tipos de datos de las columnas:")
print(dataset.dtypes)

# Ver los valores nulos y el porcentaje de nulos por columna
print("Valores nulos y porcentaje de nulos por columna:")
missing_values = dataset.isnull().sum()
missing_percentage = (missing_values / len(dataset)) * 100
print(pd.DataFrame({'Missing Values': missing_values, 'Percentage': missing_percentage}))

# Asegurarte de que no hay valores nulos
print("Valores nulos por columna:")
print(dataset.isnull().sum())
if dataset.isnull().sum().sum() == 0:
    print("No hay valores nulos en el dataset.")
else:
    print("Hay valores nulos en el dataset.")   

# categorías presentes en cada variable categórica y su frecuencia
print("Categorías presentes en variables categóricas:")
for col in dataset.select_dtypes(include=['object', 'category']).columns:
    print(f"Frecuencia de categorías en {col}:")
    print(dataset[col].value_counts())
    print("-" * 50)



# ===============================
#  2. Limpieza de datos nulos
# ===============================

# Cambiar los valores nulos por valores más adecuados
dataset['Mental_Health_Condition'] = dataset['Mental_Health_Condition'].fillna('Absence')
dataset['Physical_Activity'] = dataset['Physical_Activity'].fillna('Non-activity')
print("Valores nulos reemplazados por 'Absence' en la variable 'Mental_Health_Condition' y por 'Non-activity' en la variable 'Physical_Activity'.")
print("-" * 50)

# Guardar el dataset limpio
dataset.to_csv("/home/mario/Documents/RemoteWork/Data/CleanData/Remote_Work_Clean.csv", index=False)
print("Dataset limpio guardado en /home/mario/Documents/RemoteWork/Data/CleanData/Remote_Work_Clean.csv")
print("-" * 50)

