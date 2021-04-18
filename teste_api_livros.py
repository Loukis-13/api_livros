import requests
  
url = f"http://0.0.0.0:5000/api/books/id=2"

r = requests.get(url) 
if r:
    tudo = r.json()

    print(tudo)
else:
    print(r)