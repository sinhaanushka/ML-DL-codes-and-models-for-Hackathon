import numpy as np
import pickle
import os
from sklearn.ensemble import RandomForestClassifier

# ---------------------------
# SAMPLE TRAINING DATA
# ---------------------------
# Features:
# [login_time, failed_logins, files_accessed, usb_usage]
# login_time: hour (0–23)
# usb_usage: 0 = No, 1 = Yes

X = np.array([
    [9, 0, 5, 0],     # Normal employee
    [10, 1, 8, 0],    # Normal
    [11, 0, 6, 0],    # Normal
    [2, 4, 40, 1],    # Insider threat
    [1, 5, 50, 1],    # Insider threat
    [3, 3, 35, 1],    # Insider threat
    [14, 0, 7, 0],    # Normal
    [22, 2, 20, 1],   # Suspicious / threat
])

# Labels:
# 0 = NORMAL
# 1 = HIGH RISK
y = np.array([0, 0, 0, 1, 1, 1, 0, 1])


# TRAIN MODEL

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)


# SAVE MODEL

os.makedirs("models", exist_ok=True)

with open("models/insider_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ insider_model.pkl created successfully")
