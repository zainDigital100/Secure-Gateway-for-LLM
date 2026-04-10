def decide_policy(injection_score, pii_count, pii_results):
    if injection_score >= 0.8:
        return "BLOCK", "High-confidence prompt injection attack detected."

    detected_entities = []
    for i in pii_results:
            detected_entities.append(i.entity_type)
    
    if ("API_KEY" in detected_entities) or ("INTERNAL_ID" in detected_entities):
        return "BLOCK", "Prevention of critical sensitive data leak."

    if injection_score >= 0.5 or pii_count > 0:
        return "MASK", "PII detected or suspicious activity masked."

    return "ALLOW", "No significant risk detected."