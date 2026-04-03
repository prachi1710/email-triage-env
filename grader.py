def normalize_category(cat):
    cat = cat.lower()

    if any(x in cat for x in ["support", "complaint", "order", "account", "refund"]):
        return "support"

    if any(x in cat for x in ["spam", "scam", "phishing"]):
        return "spam"

    if any(x in cat for x in ["promo", "offer", "marketing", "subscription"]):
        return "sales"

    if any(x in cat for x in ["personal", "invoice", "job", "meeting"]):
        return "personal"

    return cat

def normalize_priority(p):
    p = p.lower()

    if p in ["high", "urgent"]:
        return "high"

    if p in ["medium", "normal"]:
        return "medium"

    if p in ["low"]:
        return "low"

    return p

def grade(pred, actual):
    score = 0.0

    # Category (0.3)
    if normalize_category(pred["category"]) == actual["category"]:
        score += 0.3

    # Priority (0.2)
    if normalize_priority(pred["priority"]) == actual["priority"]:
        score += 0.2

    # Action (0.2) - loose match
    if any(word in pred["action"].lower() for word in actual["action"].split()):
        score += 0.2

    # Response (0.3) - length-based + intent
    if len(pred["response"]) > 20:
        score += 0.3

    return round(score, 2)