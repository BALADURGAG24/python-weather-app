import requests
from .config import GEO_IP_URL

def get_location_city():
    try:
        res = requests.get(GEO_IP_URL)
        data = res.json()
        return data.get("city")
    except Exception:
        return None
