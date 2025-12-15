import pickle

# Load saved objects
model = pickle.load(open("models/email_model.pkl", "rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

def predict_email(text):
    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)[0]
    probability = model.predict_proba(text_vector)[0][prediction]

    if prediction == 1 and probability > 0.7:
        return "FRAUD"
    elif prediction == 1:
        return "SUSPICIOUS"
    else:
        return "SAFE"


if __name__ == "__main__":
    email = input("Enter email text: ")
    print("Prediction:", predict_email(email))

