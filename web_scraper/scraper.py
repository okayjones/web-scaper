import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(url):
    URL = url
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    citations = len(soup.find_all('a', text='citation needed'))
    return citations


def get_citations_needed_report(url):
    URL = url
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    citations = soup.find_all('a', text='citation needed')
    entries = []
    for c in citations:
        entries.append(str(c.find_parents('p')[0].text))
    result = str('\n'.join(entries)).strip()
    return result


