import requests

text = "Naku ee movie chala baga nachindi"

response = requests.get(f"http://localhost:8000/sentiment_analysis?text={text}")
result = response.json()["result"]

print(f"The result of adding  is: {result}")
    