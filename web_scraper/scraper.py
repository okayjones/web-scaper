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
        entries.append(c.find_parents('p')[0].text.strip())
    result = '\n\n'.join(entries)
    return result


if __name__ == '__main__':
    count = get_citations_needed_count('https://en.wikipedia.org/wiki/History_of_Mexico')
    citations = get_citations_needed_report('https://en.wikipedia.org/wiki/History_of_Mexico')

    print(f"{count} citations needed: \n\n")
    print(citations)
