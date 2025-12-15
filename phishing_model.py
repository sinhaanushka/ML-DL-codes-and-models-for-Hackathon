import pickle
from sklearn.ensemble import RandomForestClassifier

# Simple training data
X = [
    [50, 0, 0, 1, 2, 0],   # SAFE
    [120, 2, 1, 0, 5, 1], # PHISHING
    [60, 1, 0, 1, 3, 0],  # SAFE
    [150, 3, 1, 0, 6, 1]  # PHISHING
]

y = [0, 1, 0, 1]  # 0 = SAFE, 1 = PHISHING

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Create folder
import os
os.makedirs("models", exist_ok=True)

# Save model
with open("models/phishing_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ phishing_model.pkl CREATED successfully")
