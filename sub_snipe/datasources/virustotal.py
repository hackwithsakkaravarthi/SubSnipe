import requests
from .base import DataSourceBase

class VirusTotalDataSource(DataSourceBase):
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.virustotal.com/vtapi/v2/domain/report"
    
    def enumerate(self, domain):
        params = {'apikey': self.api_key, 'domain': domain}
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            json_response = response.json()
            subdomains = json_response.get('subdomains', [])
            return subdomains
        else:
            return []
