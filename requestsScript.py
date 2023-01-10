import requests
print(requests.__version__)
print(requests.get("https://www.google.com"))
print(requests.get("https://raw.githubusercontent.com/sihaaan/CMPUT404-lab1/master/requestsScript.py").text)