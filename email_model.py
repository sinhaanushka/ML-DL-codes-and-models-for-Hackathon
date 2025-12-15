import pandas as pd
import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample training data (replace with real dataset later)
emails = [
    "Congratulations you won a lottery click now",
    "Urgent update verify your bank account",
    "Free gift card claim now",
    "Meeting scheduled tomorrow at 10am",
    "Please find the project report attached",
    "Team lunch tomorrow"
]

labels = [1, 1, 1, 0, 0, 0]  # 1 = FRAUD, 0 = SAFE

# Convert text to vectors
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(emails)

# Train model
model = MultinomialNB()
model.fit(X, labels)

# Create models folder
os.makedirs("models", exist_ok=True)

# Save model and vectorizer
pickle.dump(model, open("models/email_model.pkl", "wb"))
pickle.dump(vectorizer, open("models/vectorizer.pkl", "wb"))

print("✅ Email fraud model saved successfully")
