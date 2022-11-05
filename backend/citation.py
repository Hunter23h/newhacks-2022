from bs4 import BeautifulSoup
from urllib.request import urlopen
from htmldate import find_date
from datetime import datetime

class Citation():
    def __init__(self, url):
        self.url = url
    def main(self):
        date_accessed = datetime.today().strftime('%Y-%m-%d')

        title, publisher = self.title_finder()
        date_updated = self.date_finder()

        citation = '"' + title + '" ' + publisher + ', ' + date_updated + ', ' + self.url
        print(citation)
    def date_finder(self):
        try:
            date = find_date(self.url)
            return date
        except: 
            return None

    def title_finder(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        
        # displaying the title
        data = soup.title.get_text()
        title = data.rsplit(' ', 2)[0]
        publisher = data.rsplit(' ', 1)[1]
        return title, publisher