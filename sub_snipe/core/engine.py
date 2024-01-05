from sub_snipe.datasources.base import DataSourceBase

class DomainEnumerator:
    def __init__(self, domain):
        self.domain = domain
        # Initialize data sources
        self.data_sources = [cls() for cls in DataSourceBase.__subclasses__()]

    def run(self):
        # Main method to start enumeration
        for data_source in self.data_sources:
            subdomains = data_source.enumerate(self.domain)
            for subdomain in subdomains:
                print(subdomain)

