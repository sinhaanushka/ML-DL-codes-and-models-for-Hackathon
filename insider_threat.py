import pickle
import numpy as np

def detect_insider(activity):
    model = pickle.load(open("models/insider_model.pkl", "rb"))

    features = np.array([[
        activity["login_time"],
        activity["failed_logins"],
        activity["files_accessed"],
        activity["usb_usage"]
    ]])

    risk = model.predict(features)[0]
    return "HIGH RISK" if risk == 1 else "NORMAL"

if __name__ == "__main__":
    sample_activity = {
        "login_time": 2,
        "failed_logins": 4,
        "files_accessed": 40,
        "usb_usage": 1
    }

    print("Result:", detect_insider(sample_activity))