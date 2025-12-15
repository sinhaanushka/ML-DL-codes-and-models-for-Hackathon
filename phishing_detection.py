
import re
import pickle
from sklearn.ensemble import RandomForestClassifier

with open("models/phishing_model.pkl", "rb") as f:
    model = pickle.load(f)

def extract_features(url):
    return [
        len(url),
        url.count('-'),
        url.count('@'),
        url.count('https'),
        url.count('.'),
        int(bool(re.search(r'\d', url)))
    ]

def predict_phishing(url):
    features = [extract_features(url)]
    prediction = model.predict(features)
    return "PHISHING" if prediction[0] == 1 else "SAFE"
if __name__ == "__main__":
    url = input("Enter website URL: ")
    result = predict_phishing(url)
    print("Prediction Result:", result)
