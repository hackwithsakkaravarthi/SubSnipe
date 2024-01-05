from .base import DataSourceBase
import socket
import multiprocessing

class BruteForceDataSource(DataSourceBase):
    def __init__(self, wordlist_file='default_wordlist.txt'):
        self.wordlist = self.load_wordlist(wordlist_file)

    def load_wordlist(self, file_path):
        try:
            with open(file_path, 'r') as file:
                return [line.strip() for line in file]
        except FileNotFoundError:
            print(f"Wordlist file {file_path} not found.")
            return []

    def check_subdomain(self, domain, subdomain):
        full_domain = f"{subdomain}.{domain}"
        try:
            socket.gethostbyname(full_domain)
            return full_domain
        except socket.gaierror:
            return None

    def enumerate(self, domain):
        pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
        tasks = [(domain, subdomain) for subdomain in self.wordlist]
        results = pool.starmap(self.check_subdomain, tasks)
        pool.close()
        pool.join()
        return [result for result in results if result is not None]

