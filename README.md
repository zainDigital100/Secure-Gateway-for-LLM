LLM Security Gateway

📌 Project Overview

The LLM Security Gateway is a security middleware designed to protect Large Language Model (LLM) applications. It acts as a "Firewall for AI," sitting between the user and the model to mitigate two primary risks:

Prompt Injection: Preventing adversarial attacks that try to bypass AI safety guidelines or hijack the model's logic.

Data Leakage: Detecting and masking Personally Identifiable Information (PII) such as phone numbers, emails, and sensitive API keys.

🚀 Key Features

Injection Scoring: A weighted keyword-based detection engine for identifying "jailbreak" attempts.

PII Sanitization: Integration with Microsoft Presidio for high-accuracy entity recognition.

Custom Local Recognizers: Specialized patterns for Pakistani phone numbers (+92) and internal CUI identifiers.

Policy Engine: Customizable logic in config.py to decide whether to Allow, Mask, or Block requests.

Performance Metrics: Real-time tracking of analysis latency and risk scores.

🛠️ Tech Stack

Language: Python 3.x

Framework: Flask (Web API)

NLP Engines: Microsoft Presidio & spaCy

Security: Custom Regex & Keyword Scoring

📂 Project Structure

main.py: The core Flask application handling API requests.

injection_detector.py: Contains attack keywords and scoring logic.

presidio_utils.py: PII detection and masking configurations.

config.py: Security policy thresholds and decision logic.

test.py: CLI tool for testing the gateway.

⚙️ Setup & Installation

Install Dependencies:

pip install -r requirements.txt


Download NLP Model:

python -m spacy download en_core_web_lg


Run the Gateway:

python main.py


Test the Gateway:

python test.py


📊 API Example

Endpoint: POST /analyze

Payload:

{
  "text": "Call me at 0300-1234567 or use key sk-abcdef1234567890"
}


Response:

Decision: BLOCK (if API key is present)

Decision: MASK (if only phone number is present)
