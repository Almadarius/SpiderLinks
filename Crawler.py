import requests
from bs4 import BeautifulSoup


class WebCrawler:

    def __init__(self, base_url):
        self.base_url = base_url
        self.links = []
        self.current_url = ''

    def get_links(self):
        page = requests.get(self.base_url)

        if page.status_code != 200:
            print("The URL provided is not reachable or does not exist")
            return
        else:
            soup = BeautifulSoup(page.content, 'html.parser')
            self.links = soup.find_all('a')

            return self.links
