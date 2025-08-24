#Por Ahora el codigo corre bien pero falta Chequear que todos los valores si fueron cambiados correctamente
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

# Load data
df = pd.read_csv(r"C:\Users\Usuario\Documents\Proyectos Practicos DA\Telcom-Customer-Churn-Analysis\Docs\Data Set Telcom Customer Churn.csv")

print("Original columns:", df.columns.tolist())
print("DataFrame shape:", df.shape)

# Convert TotalCharges to numeric
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce').fillna(0)

# Replace redundant values
df.replace({
    'No Internet service': 'No',
    'No phone service': 'No'
}, inplace=True)

# Check if Churn column exists before encoding
print("Churn column exists:", 'Churn' in df.columns)
print("Churn values:", df['Churn'].unique())

# Apply LabelEncoder to Churn column FIRST
le = LabelEncoder()
df['Churn'] = le.fit_transform(df['Churn'])  # Yes=1, No=0
print("Churn after encoding:", df['Churn'].unique())

# Identify categorical columns (excluding customerID and Churn)
cat_cols = df.select_dtypes(include='object').columns
cat_cols = cat_cols.drop('customerID') if 'customerID' in cat_cols else cat_cols
print("Categorical columns:", cat_cols.tolist())

# One-hot encoding (excluding Churn column from this process)
df_encoded = pd.get_dummies(df, columns=cat_cols, drop_first=True)

print("Columns after encoding:", df_encoded.columns.tolist())
print("DataFrame shape after encoding:", df_encoded.shape)

# Check if Churn column still exists
print("Churn in encoded DataFrame:", 'Churn' in df_encoded.columns)

# Scale numerical features
num_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
# Make sure these columns exist
num_cols = [col for col in num_cols if col in df_encoded.columns]
print("Numerical columns to scale:", num_cols)

if num_cols:
    scaler = StandardScaler()
    df_encoded[num_cols] = scaler.fit_transform(df_encoded[num_cols])

# Separate features and target
if 'Churn' in df_encoded.columns:
    x = df_encoded.drop(['customerID', 'Churn'], axis=1)
    y = df_encoded['Churn']
    
    print("Final feature columns:", x.columns.tolist())
    print("Target shape:", y.shape)
    
    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    print("Training set shape:", X_train.shape)
    print("Test set shape:", X_test.shape)
else:
    print("ERROR: Churn column was lost during processing")