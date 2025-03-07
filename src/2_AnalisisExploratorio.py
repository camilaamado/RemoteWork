#============================================================================================================
#                                               Análisis Exploratorio (EDA)
#============================================================================================================
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

# Llamamos a la función classify_columns para clasificar las variables del dataset
num_vars, cat_vars, ord_vars = classify_columns(dataset)
print("Variables Numéricas:", num_vars)
print("Variables Categóricas:", cat_vars)
print("Variables Ordinales:", ord_vars)
print("-" * 50)

#============================================
# 3. Exploración Grafica de los Datos
#============================================

# Función para graficar distribuciones
def plot_distributions(dataset, variables, plot_type, title, filename):
    num_vars = len(variables)
    cols = 3  
    rows = math.ceil(num_vars / cols)  
    
    fig, axes = plt.subplots(rows, cols, figsize=(16, rows * 4))
    fig.suptitle(title, fontsize=16, fontweight='bold')

    for i, var in enumerate(variables):
        ax = axes[i // cols, i % cols]  
        
        if plot_type == 'hist':  # Para variables numéricas
            sns.histplot(dataset[var], kde=True, bins=30, color='royalblue', ax=ax)
        elif plot_type == 'count':  # Para variables categóricas y ordinales
            sns.countplot(y=dataset[var], palette="Blues_r", ax=ax)
        
        ax.set_title(f'Distribución de {var}')
        ax.set_xlabel('')
        ax.set_ylabel('Frecuencia')

    for j in range(i + 1, rows * cols):
        fig.delaxes(axes.flatten()[j])

    plt.tight_layout(rect=[0, 0, 1, 0.96]) 
    plt.savefig(filename)
    plt.show()
   
   # Listas de variables
numeric_vars = ['Age', 'Years_of_Experience', 'Hours_Worked_Per_Week', 'Number_of_Virtual_Meetings']
categorical_vars = ['Gender', 'Job_Role', 'Industry', 'Work_Location', 'Mental_Health_Condition', 
                    'Access_to_Mental_Health_Resources', 'Productivity_Change', 'Region']
ordinal_vars = ['Stress_Level', 'Satisfaction_with_Remote_Work', 'Physical_Activity', 
                'Sleep_Quality', 'Work_Life_Balance_Rating', 'Social_Isolation_Rating', 'Company_Support_for_Remote_Work']

# Graficar variables numéricas
plot_distributions(dataset, numeric_vars, 'hist', "Distribución de Variables Numéricas", "/home/mario/Documents/RemoteWork/Results/distribucion_variables_numericas.png")

# Graficar variables categóricas
plot_distributions(dataset, categorical_vars, 'count', "Distribución de Variables Categóricas", "/home/mario/Documents/RemoteWork/Results/distribucion_variables_categoricas.png")

# Graficar variables ordinales
plot_distributions(dataset, ordinal_vars, 'count', "Distribución de Variables Ordinales", "/home/mario/Documents/RemoteWork/Results/distribucion_variables_ordinales.png")


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



# Guardar el dataset con variables transformadas y elimnar variables no necesarias
dataset_encoded = dataset.drop(columns=['Employee_ID'])
dataset_encoded.to_csv("/home/mario/Documents/RemoteWork/Data/CleanData/Remote_Work_TransformVars.csv", index=False)
print("Dataset con variables transformadas guardado en /home/mario/Documents/RemoteWork/Data/CleanData/Remote_Work_Encoded.csv")
print("-" * 50)

#=======================================================================================
# 5. Comprobación de la Transformación de Variables
#=======================================================================================

df = pd.read_csv("/home/mario/Documents/RemoteWork/Data/CleanData/Remote_Work_TransformVars.csv") 

print("Categorías presentes en variables categóricas y su frecuencia:")
for col in df.select_dtypes(include=['object', 'category']).columns:
    print(f"Frecuencia de categorías en {col}:")
    print(dataset[col].value_counts())
    print("-" * 50)

#==========================================================================================
# 6. Correlación entre Variables
#==========================================================================================
# Seleccionar solo columnas numéricas
numeric_df = df.select_dtypes(include=[float, int])

correlation = numeric_df.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title("Correlación entre Variables", fontsize=16, fontweight='bold')
plt.savefig("/home/mario/Documents/RemoteWork/Results/correlacion_variables.png")
plt.show()

# Filtrar correlaciones fuertes (mayores a 0.7 o menores a -0.7)
strong_correlations = correlation[(correlation > 0.2) | (correlation < -0.2)]
print("Variables con alta correlación:\n", strong_correlations)
#==========================================================================================

