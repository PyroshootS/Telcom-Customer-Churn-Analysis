import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_and_process_data(file_path):
    """Carga y procesa los datos para EXPLORACIÓN (valores originales)"""
    print("📂 Cargando datos para exploración...")
    df = pd.read_csv(file_path)
    
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

def load_and_process_data_ml(file_path):
    """Carga y procesa los datos para ML (one-hot encoding)"""
    print("📂 Cargando datos para ML...")
    df = pd.read_csv(file_path)
    
    # Convert TotalCharges to numeric
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce').fillna(0)
    
    # Replace redundant values
    df.replace({
        'No internet service': 'No',
        'No phone service': 'No'
    }, inplace=True)
    
    # Apply LabelEncoder to Churn column
    le = LabelEncoder()
    df['Churn'] = le.fit_transform(df['Churn'])
    
    # Identify categorical columns
    cat_cols = df.select_dtypes(include='object').columns
    cat_cols = cat_cols.drop('customerID') if 'customerID' in cat_cols else cat_cols
    
    # One-hot encoding
    df_encoded = pd.get_dummies(df, columns=cat_cols, drop_first=True)
    
    # Scale numerical features
    num_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
    num_cols = [col for col in num_cols if col in df_encoded.columns]
    
    if num_cols:
        scaler = StandardScaler()
        df_encoded[num_cols] = scaler.fit_transform(df_encoded[num_cols])
    
    print(f"✅ Datos listos para ML: {df_encoded.shape[0]} filas, {df_encoded.shape[1]} columnas")
    
    return df_encoded