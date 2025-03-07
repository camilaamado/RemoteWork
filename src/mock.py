import pandas as pd
import matplotlib.pyplot as plt
import seaborn
import pandas as pd
from utils import classify_columns 
import seaborn as sns
import math
from sklearn.preprocessing import LabelEncoder

# cargar datos limpios
dataset = pd.read_csv("/home/mario/Documents/RemoteWork/Data/CleanData/Remote_Work_Clean.csv") 


 # Listas de variables
numeric_vars = ['Age', 'Years_of_Experience', 'Hours_Worked_Per_Week', 'Number_of_Virtual_Meetings']
categorical_vars = ['Gender', 'Job_Role', 'Industry', 'Work_Location', 'Mental_Health_Condition', 
                    'Access_to_Mental_Health_Resources', 'Productivity_Change', 'Region']
ordinal_vars = ['Stress_Level', 'Satisfaction_with_Remote_Work', 'Physical_Activity', 
                'Sleep_Quality', 'Work_Life_Balance_Rating', 'Social_Isolation_Rating', 'Company_Support_for_Remote_Work']



#=========================================================================
# 4. Transformación de Variables: De categoricas / ordinales a numericas. 
#=========================================================================

# Transformar variables categóricas a numéricas utilizando One-Hot Encoding: Convierte variables categóricas en variables binarias (0/1).

dataset_encoded = pd.get_dummies(dataset, columns=categorical_vars, drop_first=True)
print("Dataset con variables categóricas transformadas:")
print(dataset_encoded.head())
print("-" * 50) 

################################################################################################################################

# Transformar variables ordinales a numéricas utilizando Label Encoding: Convierte variables ordinales en valores numéricos.

# Diccionarios de mapeo para variables ordinales
stress_mapping = {'Low': 0, 'Medium': 1, 'High': 2}
satisfaction_mapping = {'Unsatisfied': 0, 'Neutral': 1, 'Satisfied': 2}
physical_activity_mapping = {'Non-activity': 0, 'Weekly': 1, 'Daily': 2}
sleep_quality_mapping = {'Poor': 0, 'Average': 1, 'Good': 2}  

# Convertir variables numéricas en formato string a enteros
rating_vars = ['Work_Life_Balance_Rating', 'Social_Isolation_Rating', 'Company_Support_for_Remote_Work']

# Aplicar los mapeos a las variables ordinales
dataset['Stress_Level'] = dataset['Stress_Level'].map(stress_mapping)
dataset['Satisfaction_with_Remote_Work'] = dataset['Satisfaction_with_Remote_Work'].map(satisfaction_mapping)
dataset['Physical_Activity'] = dataset['Physical_Activity'].map(physical_activity_mapping)
dataset['Sleep_Quality'] = dataset['Sleep_Quality'].map(sleep_quality_mapping)

# Convertir variables numéricas en formato string a enteros
for var in rating_vars:
    dataset[var] = dataset[var].astype(int)

# Mostrar las primeras filas del dataset transformado
print("Dataset con variables ordinales transformadas:")
print(dataset[ordinal_vars].head())
print("-" * 50)

print("Primeras filas del dataset transformado:")
print(dataset_encoded.head())

print("\nResumen estadístico del dataset transformado:")
print(dataset_encoded.describe(include='all'))
print("-" * 50)

print("Categorías presentes en variables categóricas y su frecuencia:")
for col in dataset_encoded.select_dtypes(include=['object', 'category']).columns:
    print(f"Frecuencia de categorías en {col}:")
    print(dataset[col].value_counts())
    print("-" * 50)




import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar datos
dataset_encoded = pd.read_csv("/home/mario/Documents/RemoteWork/Data/CleanData/Remote_Work_TransformVars.csv")

# Eliminar columna 'Employee_ID' si existe
if 'Employee_ID' in dataset_encoded.columns:
    dataset_encoded = dataset_encoded.drop(columns=['Employee_ID'])

# Seleccionar solo columnas numéricas
numeric_dataset_encoded = dataset_encoded.select_dtypes(include=[float, int])

# Resumen estadístico del dataset transformado
print("\nResumen estadístico del dataset transformado:")
print(dataset_encoded.describe(include='all'))
print("-" * 50)

# Categorías presentes en variables categóricas y su frecuencia
print("Categorías presentes en variables categóricas y su frecuencia:")
for col in dataset_encoded.select_dtypes(include=['object', 'category']).columns:
    print(f"Frecuencia de categorías en {col}:")
    print(dataset_encoded[col].value_counts())
    print("-" * 50)

# Calcular la correlación
correlation = numeric_dataset_encoded.corr()

# Graficar el mapa de calor de la correlación
plt.figure(figsize=(12, 8))
sns.heatmap(correlation, cmap="coolwarm", annot=False)
plt.title("Correlación entre Variables", fontsize=16, fontweight='bold')
plt.savefig("/home/mario/Documents/RemoteWork/Results/correlacion_variables.png")
plt.show()


# Filtrar correlaciones fuertes (mayores a 0.7 o menores a -0.7)
# Calcular la matriz de correlación
correlation_matrix = dataset_encoded.corr()
strong_correlations = correlation_matrix[(correlation_matrix > 0.7) | (correlation_matrix < -0.7)]
print("Variables con alta correlación:\n", strong_correlations)
