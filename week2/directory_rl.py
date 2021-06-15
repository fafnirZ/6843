import requests
import urllib
from bs4 import BeautifulSoup
import re
import sys

'''
argv_1 = domain
argv_2 = wordlist
'''


def create_request(domain, path):
	host = 'https://'+domain
	print(host)
	

domain = sys.argv[1]
word = 'abc'

create_request(domain, word)







