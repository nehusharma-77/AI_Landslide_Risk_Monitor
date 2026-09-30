import joblib

#Trained AI model load karo
model=joblib.load("landslide_model.pkl")

#Sensor/input values
rainfall=float(input("Rainfall:"))
soil_moisture=float(input("Soil Moisture:"))
temperature=float(input("Temperature:"))
humidity=float(input("Humidity:"))
soil_tilt=float(input("Soil Tilt:"))

#Prediction
prediction=model.predict([[
    rainfall,
    soil_moisture,
    temperature,
    humidity,
    soil_tilt
]])
print("Landslide Risk:",prediction[0])