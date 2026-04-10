import requests
import json
import time

URL = "http://127.0.0.1:5000/analyze"

def send_prompt(text):
    print(f"{'-'*60}")
    print(f"Input: {text}")
    
    payload = {"text": text}
    headers = {"Content-Type": "application/json"}
    
    try:
        start_time = time.time()
        response = requests.post(URL, json=payload, headers=headers)
        end_time = time.time()
        
        if response.status_code == 200:
            result = response.json()
            print(f"Decision:  {result['analysis']['decision']}")
            print(f"Reason:    {result['analysis']['reason']}")
            print(f"Output:    {result['output']}")
            print(f"Latency:   {result['metrics']['latency_ms']}ms (Server-side)")
            print(f"RTT:       {round((end_time - start_time)*1000, 2)}ms (Round-trip)")
        else:
            print(f"ERROR: Received status code {response.status_code}")
            try:
                print(json.dumps(response.json(), indent=2))
            except:
                print(response.text)
            
    except requests.exceptions.ConnectionError:
        print("CRITICAL ERROR: Could not connect to the server. Make sure main.py is running!")

if __name__ == "__main__":
    print("LLM Security Gateway")
    user_input = input("Enter Prompt: ")
    send_prompt(user_input)