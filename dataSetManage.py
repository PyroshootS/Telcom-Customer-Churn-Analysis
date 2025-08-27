"""
MÓDULO DE GESTIÓN DE DATOS - Versión Simplificada
- Carga de datos
- Exploración básica
- Visualización simple
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder

def loadData(filePath):
    """Carga y limpia los datos para exploración"""
    print("📂 Cargando datos para exploración...")
    df = pd.read_csv(filePath)
    
    print(f"✅ Datos cargados: {df.shape[0]} filas, {df.shape[1]} columnas")
    
    # Convert TotalCharges to numeric (mantenemos para análisis)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce').fillna(0)
    
    # Replace redundant values para consistencia
    df.replace({
        'No internet service': 'No Internet Service',
        'No phone service': 'No Phone Service'
    }, inplace=True)
    
    # Apply LabelEncoder solo a Churn para mantenerlo binario
    le = LabelEncoder()
    df['Churn'] = le.fit_transform(df['Churn'])
    
    print(f"✅ Datos listos para exploración: {df.shape[0]} filas, {df.shape[1]} columnas")
    
    return df

def showDatasetInfo(df):
    """Muestra información general del DataFrame"""
    print("\n" + "="*60)
    print("📊 INFORMACIÓN GENERAL DEL DATASET")
    print("="*60)
    print(f"Shape del DataFrame: {df.shape}")
    print(f"Número de columnas: {len(df.columns)}")
    print(f"Total clientes: {len(df):,}")
    print(f"Primeros 5 customerIDs: {df['customerID'].head(5).tolist()}")
    
    # Mostrar tipos de datos
    print("\n📋 TIPOS DE DATOS:")
    print(df.dtypes.value_counts())

def showColumnSamples(df):
    """Muestra 20 ejemplos aleatorios de una columna específica con customerID"""
    print("\n" + "="*60)
    print("🔍 MOSTRAR MUESTRAS DE COLUMNA")
    print("="*60)
    
    # Columnas disponibles (excluyendo customerID)
    columnasDisponibles = [col for col in df.columns if col != 'customerID']
    
    # Mostrar columnas disponibles
    print("Columnas disponibles:")
    for i, col in enumerate(columnasDisponibles, 1):
        print(f"{i:2d}. {col}")
    
    try:
        opcion = int(input("\nSelecciona el número de la columna: "))
        if 1 <= opcion <= len(columnasDisponibles):
            columnaSeleccionada = columnasDisponibles[opcion-1]
            
            # Mostrar información de la columna
            print(f"\n🎯 Columna seleccionada: {columnaSeleccionada}")
            print(f"📊 Tipo de dato: {df[columnaSeleccionada].dtype}")
            print(f"🔢 Valores únicos: {df[columnaSeleccionada].nunique()}")
            
            # Mostrar 20 ejemplos aleatorios con customerID
            print(f"\n📋 20 ejemplos aleatorios:")
            muestras = df[['customerID', columnaSeleccionada]].sample(n=20, random_state=42)
            print(muestras.to_string(index=False))
                
        else:
            print("❌ Opción inválida")
    except ValueError:
        print("❌ Por favor ingresa un número válido")

def showChurnStats(df):
    """Muestra estadísticas del Churn"""
    print("\n" + "="*60)
    print("📈 ESTADÍSTICAS DE CHURN")
    print("="*60)
    
    if 'Churn' in df.columns:
        # Mapear valores numéricos a texto para mejor comprensión
        churnCounts = df['Churn'].value_counts()
        churnPercent = df['Churn'].value_counts(normalize=True) * 100
        
        print(f"Clientes que NO se fueron: {churnCounts[0]:,} ({churnPercent[0]:.1f}%)")
        print(f"Clientes que SÍ se fueron: {churnCounts[1]:,} ({churnPercent[1]:.1f}%)")
        print(f"Total clientes: {len(df):,}")
        
        # Información adicional útil
        print(f"\n📊 Tasa de churn general: {churnPercent[1]:.1f}%")
        
    else:
        print("❌ Columna 'Churn' no encontrada")