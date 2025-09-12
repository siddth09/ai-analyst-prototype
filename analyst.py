def analyze_startup(text):
    """
    Simple analysis to demo benchmarking, risk flags, and recommendations.
    """
    # Simple keyword-based "risk" detection
    risk_flags = []
    if "churn" in text.lower():
        if "5%" in text or "10%" in text:
            risk_flags.append("Moderate churn risk")
        elif "20%" in text or "30%" in text:
            risk_flags.append("High churn risk")
    
    if "market size" in text.lower():
        if "$5 billion" in text:
            risk_flags.append("Market size seems reasonable")
        elif "$100 billion" in text:
            risk_flags.append("Market size might be inflated")

    # Benchmarking demo
    benchmark = {
        "Revenue": "Above average" if "$20,000" in text else "Average",
        "Team size": "Small team" if "5 founders" in text else "Average team",
        "Traction": "Good traction" if "5000 merchants" in text else "Needs traction"
    }

    # Recommendation logic (demo)
    if "High churn risk" in risk_flags:
        recommendation = "Caution: Needs more traction or retention strategy."
    else:
        recommendation = "Potentially investable with moderate risk."

    return benchmark, risk_flags, recommendation
