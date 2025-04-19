import os
# Example: Make a request using the proxy (requires the `requests` library)
import requests

# Set the proxy environment variables
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:7890'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'

#test connection

try:
    response = requests.get('https://www.google.com')
    print(response.text)
except Exception as e:
    print(f"An error occurred: {e}")