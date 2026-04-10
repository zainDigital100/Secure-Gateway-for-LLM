# 🛡️ LLM Security Gateway

A **security middleware for Large Language Model (LLM) applications**, designed to act as a *"Firewall for AI"* between users and LLMs. It protects applications from **prompt injection attacks** and **data leakage (PII exposure)** using rule-based detection and NLP-powered analysis.

---

## 📌 Overview

The **LLM Security Gateway** sits between the user and the LLM and analyzes every incoming request to:

- 🚨 Detect and prevent **Prompt Injection / Jailbreak attempts**
- 🔒 Identify and mask **Personally Identifiable Information (PII)**
- ⚖️ Apply a configurable **security policy engine**
- 📊 Track request risk scores and latency metrics

---

## 🚀 Key Features

### 🔐 Prompt Injection Detection
- Weighted keyword-based scoring system
- Detects jailbreak patterns like:
  - "ignore previous instructions"
  - "developer mode"
  - "bypass security"
- Risk scoring system for decision-making

---

### 🕵️ PII Detection & Masking
- Powered by **Microsoft Presidio**
- Detects sensitive data such as:
  - Phone numbers
  - Emails
  - API keys
- Automatically masks sensitive information before forwarding

---

### 🇵🇰 Custom Local Recognizers
- Pakistani phone number detection (`+92`, `03XX` formats)
- Custom identifiers (e.g., internal CUI/student IDs)

---

### ⚙️ Policy Engine
Configurable decision logic in `config.py`:
- `ALLOW` → Safe request
- `MASK` → Redact sensitive data
- `BLOCK` → Reject dangerous input

---

### 📊 Performance Monitoring
- Real-time request latency tracking
- Injection risk scoring
- PII detection logs

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Framework:** Flask
- **NLP:** Microsoft Presidio
- **Security Engine:** Custom regex + keyword scoring
- **Architecture:** Middleware / API Gateway

---

## 📂 Project Structure
llm-security-gateway/
│
├── main.py                  # Flask API entry point (routes /analyze)
├── config.py               # Policy engine (ALLOW / MASK / BLOCK rules)
├── test.py                 # CLI testing script for gateway
│
├── injection_detector.py   # Prompt injection detection logic
│                           # - keyword patterns
│                           # - weighted risk scoring
│
├── presidio_utils.py       # PII detection & masking layer
│                           # - Microsoft Presidio integration
│                           # - custom recognizers (PK phone, API keys)
│
├── requirements.txt        # Python dependencies
│
├── README.md               # Project documentation
