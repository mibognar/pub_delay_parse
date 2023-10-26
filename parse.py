import bz2
import collections
import datetime
import gzip
import os
import time
import json

import pandas
import requests


def esearch_query(payload, retmax = 10000, sleep=0.34):
    """
    Return identifiers using the ESearch E-utility.
    """
    url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'
    payload['retmax'] = retmax
    payload['retmode'] = 'json'
    payload['retstart'] = 0
    ids = list()
    count = 1
    response = requests.get(url, params=payload)
        
    return response.text

mydict={'database':'hello','mylist':[1,2,3,4,5,6]}

print(mydict['mylist'])

# Run esearch queries
payload = {'db': 'pubmed', 'term': 'journal article[pt] AND 2020:2020[pdat]'}
#pubmed_ids = esearch_query(payload)
#print(pubmed_ids)


def esummary_query(article_id):
	url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi'
	payload['retmode'] = 'json'
	payload['retmax'] = 10000
	payload['retstart'] = 0
	payload['id'] = article_id
	payload['db'] = 'pubmed'
	response = requests.get(url, params=payload)
	metadata = json.loads(response.text)
	#print(metadata)

	#print(response.text)
	print(metadata["result"][article_id]['history'])
	#print(metadata["result"][article_id]['fulljournalname'])


id_list = ["34150566","34150565","34150564","34150562","34150561","34150560","34150559"]
for i in id_list:
	esummary_query(i)




