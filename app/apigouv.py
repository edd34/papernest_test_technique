import requests

class AdresseDataGouv:
    def search(self, query: str):
        try:
            url = f"https://api-adresse.data.gouv.fr/search/?q={query}"
            response = requests.get(url)
            data = response.json()
        except Exception as e:
            print(e)
            return None
        return data
