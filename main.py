"""
MENÚ PRINCIPAL - Integra gestión y análisis
"""

from dataSetManage import loadData, showDatasetInfo, searchByColumn, searchByCustomerId, showChurnStats, showUniqueValues

def dataManageMenu(df):
    """Menú de Gestión de Datos"""
    while True:
        print("\n" + "="*60)
        print("📊 MENÚ GESTIÓN DE DATOS")
        print("="*60)
        print("1. 📋 Información general del dataset")
        print("2. 🔍 Buscar por columna específica")
        print("3. 👤 Buscar por CustomerID")
        print("4. 📈 Estadísticas de Churn")
        print("5. 🔎 Ver valores únicos de una columna")
        print("6. ↩️ Volver al menú principal")
        print("="*60)
        
        opcion = input("Selecciona una opción (1-6): ").strip()
        
        if opcion == '1':
            showDatasetInfo(df)
        elif opcion == '2':
            searchByColumn(df)
        elif opcion == '3':
            searchByCustomerId(df)
        elif opcion == '4':
            showChurnStats(df)
        elif opcion == '5':
            columna = input("Ingresa el nombre de la columna: ").strip()
            showUniqueValues(df, columna)
        elif opcion == '6':
            print("Volviendo al menú principal...")
            break
        else:
            print("❌ Opción inválida. Por favor elige 1-6.")
        
        input("\nPresiona Enter para continuar...")

def dataAnalysisMenu(df):
    """Menú de Análisis de Datos"""
    while True:
        print("\n" + "="*60)
        print("🔍 MENÚ ANÁLISIS DE DATOS")
        print("="*60)
        print("1. 📈 Análisis de segmentación por servicios")
        print("2. 💰 Análisis de precios y churn")
        print("3. ⏰ Análisis de antigüedad de clientes")
        print("4. 👥 Análisis demográfico")
        print("5. 💳 Análisis de métodos de pago")
        print("6. ↩️ Volver al menú principal")
        print("="*60)
        
        opcion = input("Selecciona una opción (1-6): ").strip()
        
        if opcion == '1':
            print("🔧 Función en desarrollo - Análisis de segmentación")
        elif opcion == '2':
            print("🔧 Función en desarrollo - Análisis de precios")
        elif opcion == '3':
            print("🔧 Función en desarrollo - Análisis de antigüedad")
        elif opcion == '4':
            print("🔧 Función en desarrollo - Análisis demográfico")
        elif opcion == '5':
            print("🔧 Función en desarrollo - Análisis de pagos")
        elif opcion == '6':
            print("Volviendo al menú principal...")
            break
        else:
            print("❌ Opción inválida. Por favor elige 1-6.")
        
        input("\nPresiona Enter para continuar...")

def mainMenu():
    filePath = r"C:\Users\Usuario\Documents\Proyectos Practicos DA\Telcom-Customer-Churn-Analysis\Docs\Data Set Telcom Customer Churn.csv"
    
    # Cargar datos
    df = loadData(filePath)
    
    while True:
        print("\n" + "="*60)
        print("🎯 MENÚ PRINCIPAL TELCO CHURN ANALYSIS")
        print("="*60)
        print("1. 📊 GESTIÓN DE DATOS (DataSetManage)")
        print("2. 🔍 ANÁLISIS AVANZADO (DataSetAnalysis)")
        print("3. 🚪 Salir")
        print("="*60)
        
        opcion = input("Selecciona módulo (1-3): ").strip()
        
        if opcion == '1':
            dataManageMenu(df)
        elif opcion == '2':
            dataAnalysisMenu(df)
        elif opcion == '3':
            print("¡Hasta luego! 👋")
            break
        else:
            print("❌ Opción inválida. Por favor elige 1-3.")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    mainMenu()