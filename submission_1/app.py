from flask import Flask, render_template, request, jsonify
import requests
import tldextract

app = Flask(__name__)

# Google Safe Browsing API Key
GOOGLE_API_KEY = "AIzaSyBiL58vVMYIldCuZXV0I-yIbzP_PL0IMto"

def extract_domain(url):
    extracted = tldextract.extract(url)
    domain = f"{extracted.domain}.{extracted.suffix}"
    return domain

def check_google_safe_browsing(url):
    api_url = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={GOOGLE_API_KEY}"
    payload = {
        "client": {"clientId": "phishing-scanner", "clientVersion": "1.0"},
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE", "POTENTIALLY_HARMFUL_APPLICATION"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }
    
    response = requests.post(api_url, json=payload)
    result = response.json()
    
    if "matches" in result:
        return True, "This url is not safe for browsing !!! "
    return False, "No threats detected you can continue."

@app.route("/")  # Route for home page
def home():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    data = request.json
    url = data.get("url")

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    phishing, message = check_google_safe_browsing(url)
    return jsonify({"phishing": phishing, "message": message})

if __name__ == "__main__":
    app.run(debug=True)
