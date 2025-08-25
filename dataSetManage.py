"""
MÓDULO DE GESTIÓN DE DATOS
- Carga de datos
- Limpieza básica
- Exploración inicial
- Búsquedas y filtros
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

def searchByColumn(df):
    """Busca por columna y valores específicos"""
    print("\n" + "="*60)
    print("🔍 BUSCAR POR COLUMNA")
    print("="*60)
    
    # Columnas disponibles (excluyendo customerID)
    columnasDisponibles = [col for col in df.columns if col != 'customerID']
    
    # Mostrar columnas disponibles
    print("Columnas disponibles para filtrar:")
    for i, col in enumerate(columnasDisponibles, 1):
        print(f"{i:2d}. {col}")
    
    try:
        opcion = int(input("\nSelecciona el número de la columna: "))
        if 1 <= opcion <= len(columnasDisponibles):
            columnaSeleccionada = columnasDisponibles[opcion-1]
            
            # Mostrar valores únicos de la columna
            valoresUnicos = df[columnaSeleccionada].unique()
            print(f"\n🎯 Columna seleccionada: {columnaSeleccionada}")
            print(f"📊 Valores únicos: {valoresUnicos}")
            print(f"🔢 Número de valores únicos: {len(valoresUnicos)}")
            
            # Preguntar valor para filtrar
            valorFiltro = input("\nValor a filtrar (dejar vacío para ver todos): ").strip()
            
            if valorFiltro:
                # Convertir a número si la columna es numérica
                if df[columnaSeleccionada].dtype in ['int64', 'float64']:
                    try:
                        valorFiltro = float(valorFiltro) if '.' in valorFiltro else int(valorFiltro)
                    except:
                        pass
                
                # Filtrar
                resultado = df[df[columnaSeleccionada] == valorFiltro]
                print(f"\n✅ Resultados encontrados: {len(resultado)}")
                
                if not resultado.empty:
                    # Mostrar solo columnas importantes
                    columnasMostrar = ['customerID', columnaSeleccionada]
                    # Agregar algunas columnas adicionales útiles
                    columnasUtiles = ['Churn', 'tenure', 'MonthlyCharges', 'TotalCharges']
                    for col in columnasUtiles:
                        if col in df.columns and col != columnaSeleccionada:
                            columnasMostrar.append(col)
                    
                    print(resultado[columnasMostrar].head(20))
                else:
                    print("❌ No se encontraron resultados con ese filtro")
            else:
                # Mostrar muestras aleatorias
                print(f"\n📋 Mostrando 10 muestras aleatorias:")
                muestras = df[['customerID', columnaSeleccionada]].sample(n=10, random_state=42)
                print(muestras)
                
        else:
            print("❌ Opción inválida")
    except ValueError:
        print("❌ Por favor ingresa un número válido")

def searchByCustomerId(df):
    """Busca información por customerID específico"""
    print("\n" + "="*60)
    print("👤 BUSCAR POR CUSTOMER ID")
    print("="*60)
    
    customerId = input("Ingresa el customerID: ").strip()
    
    if customerId in df['customerID'].values:
        resultado = df[df['customerID'] == customerId]
        print(f"\n✅ CustomerID encontrado!")
        print("="*40)
        
        # Mostrar toda la información en formato vertical
        for columna in df.columns:
            valor = resultado[columna].values[0]
            print(f"{columna:25}: {valor}")
        
    else:
        print("❌ CustomerID no encontrado")
        print("Algunos customerIDs de ejemplo:")
        print(df['customerID'].head(5).tolist())

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
        
    else:
        print("❌ Columna 'Churn' no encontrada")

def showUniqueValues(df, columnName):
    """Muestra valores únicos y su distribución para una columna"""
    if columnName in df.columns:
        print(f"\n🎯 Valores únicos en {columnName}:")
        distribucion = df[columnName].value_counts()
        for valor, count in distribucion.items():
            porcentaje = (count / len(df)) * 100
            print(f"  {valor:25}: {count:>5} ({porcentaje:.1f}%)")
    else:
        print(f"❌ Columna '{columnName}' no encontrada")