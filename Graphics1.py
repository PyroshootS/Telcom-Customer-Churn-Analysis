#No se le ha dado realmente un valor comercial a los graficos


# 1. Importar librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns  # CORRECTO: "seaborn", NO "scaborn"

# Configuración para visualizaciones
sns.set_style('whitegrid')  # CORRECTO: "set_style", NO "set_stylet"
plt.rcParams['figure.figsize'] = (10, 6)  # CORRECTO: "rcParams", NO "reframe"

# Para evitar warnings molestos
import warnings
warnings.filterwarnings('ignore')  # CORRECTO: "filterwarnings", NO "filtersWarning"

# Cargar datos
df = pd.read_csv(r'C:\Users\Usuario\Documents\Proyectos Practicos DA\Telcom-Customer-Churn-Analysis\Docs\Data Set Telcom Customer Churn.csv') 

# Crear primer gráfico de prueba
plt.figure()
sns.histplot(df['tenure'], bins=30, kde=True)  # CORRECTO: "histplot", NO "histopix". "bins=30", NO "blas-sb"
plt.title('Distribución de la Antigüedad de los Clientes (Meses)')  # CORRECTO: "Distribución"
plt.xlabel('Meses')  # CORRECTO: "xlabel", NO "label"
plt.ylabel('Número de Clientes')  # CORRECTO: "Número", NO "Hombre"
plt.show()