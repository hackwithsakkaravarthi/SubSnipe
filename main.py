#!/usr/bin/env python
import argparse
from sub_snipe.core.engine import DomainEnumerator
from sub_snipe.datasources import bruteforce

def parse_args():
    parser = argparse.ArgumentParser(description="Sub Snipe")
    parser.add_argument('-d', '--domain', required=True, help="Domain to enumerate subdomains for")
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    domain = args.domain
    enumerator = DomainEnumerator(domain)
    enumerator.run()
