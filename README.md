# Network Operator Coverage API 

This project is an API that provides network operators coverage based on address given in parameters.

## Installation
### Via Python virtualenv
Instructions on how to install the project :

```bash
git clone https://github.com/user/project.git
cd project
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 -m uvicorn main:app
```

### Via Docker
In order to run the project using Docker
```
docker compose build
docker compose up
```

Application will be available in port 8888.

## Usage

Example usage :

* cURL :
```bash
curl --request GET \
  --url 'http://127.0.0.1:8000/coverage?address=paris'
```

* python :
```python
import requests

url = "http://127.0.0.1:8000/coverage"

querystring = {"address":"paris"}

response = requests.get(url, params=querystring)

print(response.json())
```

NB : if you might need to escape some characters, see : https://www.werockyourweb.com/url-escape-characters/