def risk_signal(phishing, email, insider):
    score = 0

    if phishing == "PHISHING":
        score += 40
    if email == "FRAUD":
        score += 40
    elif email == "SUSPICIOUS":
        score += 20
    if insider == "HIGH RISK":
        score += 30

    if score >= 60:
        return "🔴 RED – BLOCK IMMEDIATELY"
    elif score >= 30:
        return "🟡 YELLOW – VERIFY"
    else:
        return "🟢 GREEN – SAFE"
