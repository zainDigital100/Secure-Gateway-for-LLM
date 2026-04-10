from flask import Flask, request, jsonify
import time

from injection_detector import detect_injection
from presidio_utils import analyze_pii, mask_pii
from config import decide_policy

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "LLM Security Gateway Running"})


@app.route("/analyze", methods=["POST"])
def analyze():
    start_time = time.time()

    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({
            "error": "Invalid request format",
            "example": {"text": "Hello, my phone is 0300-1234567"}
        }), 400

    text = data["text"]

    injection_score = detect_injection(text)

    pii_results = analyze_pii(text)
    pii_count = len(pii_results)

    decision, reason = decide_policy(injection_score, pii_count, pii_results)

    output_text = text

    if decision == "BLOCK":
        output_text = f"Blocked: {reason}"
    elif decision == "MASK":
        output_text = mask_pii(text, pii_results)

    latency = round((time.time() - start_time) * 1000, 2)

    return jsonify({
        "input": text,
        "analysis": {
            "injection_score": round(injection_score, 3),
            "pii_detected_count": pii_count,
            "pii_entities_found": [r.entity_type for r in pii_results],
            "decision": decision,
            "reason": reason
        },
        "output": output_text,
        "metrics": {
            "latency_ms": latency,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
    })


if __name__ == "__main__":
    print("Gateway running at http://127.0.0.1:5000")
    app.run(debug=True, port=5000)