import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

#Dataset load karo
data = pd.read_csv("../Datasets/landslide_data.csv")

#input features
X=data[
    [
        "rainfall",
        "soil_moisture",
        "temperature",
        "humidity",
        "soil_tilt"
    ]
]
# Target /answer
y=data["risk"]

#AI model
model=RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

#Model train karo
model.fit(X,y)

#Model save kro
joblib.dump(model,"landslide_model.pkl")

print("AI model sucessfully trained!")
print("Model saved as landslide_model.pkl")