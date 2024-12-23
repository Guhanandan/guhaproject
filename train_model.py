from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pickle
import pandas as pd

df = pd.read_csv("crop_data.csv")
X = df.drop("Crop", axis=1)  # Features
y = df["Crop"]              # Labels

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
mx = MinMaxScaler()
sc = StandardScaler()

X_train_mx = mx.fit_transform(X_train)
X_train_scaled = sc.fit_transform(X_train_mx)

# Train the model
model = DecisionTreeClassifier()
model.fit(X_train_scaled, y_train)

# Save the model and scalers
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(mx, open("minmaxscaler.pkl", "wb"))
pickle.dump(sc, open("standscaler.pkl", "wb"))
