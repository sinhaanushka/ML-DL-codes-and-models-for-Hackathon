from phishing_detection import predict_phishing
from email_fraud_detection import predict_email
from insider_threat import detect_insider
from risk_engine import risk_signal

def main_api(url, email_text, user_activity):
    
    phishing = predict_phishing(url)
    email = predict_email(email_text)
    insider = detect_insider(user_activity)

    final_decision = risk_signal(phishing, email, insider)

    return final_decision

if __name__ == "__main__":

    url = input("Enter website URL: ")

    email_text = input("Enter email/message text: ")

    user_activity = {
        "login_time": int(input("Login time (0-23): ")),
        "failed_logins": int(input("Number of failed logins: ")),
        "files_accessed": int(input("Number of files accessed: ")),
        "usb_usage": int(input("USB used? (1=Yes, 0=No): "))
    }

    output = main_api(url, email_text, user_activity)


    print("\nFINAL CYBERSHIELD DECISION:", output)