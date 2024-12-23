import pandas as pd

# Create synthetic dataset
data = {
    "Nitrogen": [90, 50, 40, 70, 60, 45],
    "Phosphorus": [40, 30, 20, 60, 50, 25],
    "Potassium": [40, 20, 30, 50, 60, 35],
    "Temperature": [22.5, 18.0, 25.0, 28.0, 30.0, 24.0],
    "Humidity": [80, 60, 70, 50, 85, 75],
    "pH": [6.5, 7.0, 5.5, 6.8, 6.0, 6.2],
    "Rainfall": [200, 150, 180, 120, 250, 170],
    "Crop": [1, 2, 3, 4, 5, 6]  # Labels for crops
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save as CSV
df.to_csv("crop_data.csv", index=False)

print("Dataset saved as crop_data.csv")
