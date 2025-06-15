import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
import pickle

# Load your data
df = pd.read_csv("telco.csv")  # make sure this file is available

# Re-apply your encodings
label_cols = [
    'City', 'Gender', 'Married', 'Offer', 'Phone Service', 'Multiple Lines',
    'Internet Service', 'Internet Type', 'Online Security', 'Online Backup',
    'Device Protection Plan', 'Premium Tech Support', 'Streaming TV',
    'Streaming Movies', 'Streaming Music', 'Unlimited Data', 'Contract',
    'Paperless Billing', 'Payment Method', 'Customer Status',
    'Churn Label'
]

for col in label_cols:
    df[col + "_encoded"] = LabelEncoder().fit_transform(df[col])

X = df[[col + "_encoded" for col in label_cols if col != "Churn Label"]]
y = df["Churn Label_encoded"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
with open("model_clean.pkl", "wb") as f:
    pickle.dump(model, f)