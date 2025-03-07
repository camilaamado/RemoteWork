# Análisis de Datos sobre Trabajo Remoto

## Descripción
Este proyecto analiza datos sobre el trabajo remoto, explorando la distribución de variables, transformaciones de datos y correlaciones entre variables. Se utilizan herramientas de procesamiento de datos, visualización y transformación para obtener insights significativos.

## Estructura del Proyecto
```
RemoteWork/
│── Data/
│   ├── Raw/  # Datos originales
│   ├── CleanData/  # Datos limpios y transformados
│── Results/  # Resultados de análisis y visualizaciones
│── Scripts/
│   ├── analisis_1.py  # Exploración y limpieza de datos
│   ├── analisis_2.py  # Análisis exploratorio y transformación de variables
│── utils.py  # Funciones auxiliares
│── README.md  # Documentación del proyecto
```

## Requisitos
Para ejecutar este proyecto, necesitas instalar las siguientes librerías:
```bash
pip install pandas numpy seaborn matplotlib scikit-learn
```

## Uso
### 1. Exploración y Limpieza de Datos (`analisis_1.py`)
- Carga los datos crudos desde `Remote_Work.csv`
- Realiza un análisis exploratorio básico (tamaño del dataset, tipos de datos, valores nulos, distribución de variables categóricas)
- Realiza limpieza de datos (imputación de valores nulos)
- Guarda los datos limpios en `Remote_Work_Clean.csv`

### 2. Análisis Exploratorio y Transformación (`analisis_2.py`)
- Carga los datos limpios desde `Remote_Work_Clean.csv`
- Clasifica variables en numéricas, categóricas y ordinales
- Visualiza distribuciones de variables numéricas, categóricas y ordinales
- Transforma variables categóricas (One-Hot Encoding) y ordinales (Label Encoding)
- Guarda los datos transformados en `Remote_Work_TransformVars.csv`
- Genera una matriz de correlación y visualiza las relaciones entre variables

## Resultados
Los resultados incluyen:
- Visualizaciones de distribución de datos (`Results/`)
- Dataset limpio y transformado (`CleanData/`)
- Matriz de correlación de variables



