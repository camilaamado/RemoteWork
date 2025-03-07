
# Funcion para clasificar las variables de un dataframe
import pandas as pd

def classify_columns(df):
    numerical_vars = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_vars = df.select_dtypes(include=['object', 'category']).columns.tolist()
    
    ordinal_vars = []
    ordinal_candidates = ['Stress_Level', 'Satisfaction_with_Remote_Work', 
                          'Physical_Activity', 'Sleep_Quality']
    
    for col in ordinal_candidates:
        if col in categorical_vars:
            ordinal_vars.append(col)
            categorical_vars.remove(col)  # Sacamos las ordinales de las categóricas

    return numerical_vars, categorical_vars, ordinal_vars


# Función para graficar distribuciones

import pandas as pd
import matplotlib.pyplot as plt
import seaborn
import pandas as pd
from utils import classify_columns 
import seaborn as sns
import math

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

