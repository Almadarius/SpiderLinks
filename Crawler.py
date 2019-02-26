import requests
from bs4 import BeautifulSoup


class WebCrawler:

    def __init__(self, base_url):
        self.base_url = base_url
        self.current_links = []
        self.current_url = ''
        self.links = []
        self.visited_links = []

    def get_links(self):
        self.get_current_page_links(self.base_url)

    def get_current_page_links(self, url):
        page = requests.get(url)

        if page.status_code != 200:
            print("The URL provided is not reachable, does not exist, or you are not authorized")
            return
        else:
            soup = BeautifulSoup(page.content, 'html.parser')
            anchor_tags = soup.find_all('a')
            self.current_links = self.cleanup_links(anchor_tags)
            self.visit_link(url)
            self.insert_links()

            # for link in self.links:
            #     if len(self.links) > 0:
            #         self.get_current_page_links(link)
            #     else:
            #         return

    def cleanup_links(self, links):
        clean_links = [0] * len(links)
        count = 0

        for link in links:
            tag = str(link)
            href_index = tag.find('href')
            href = tag[href_index:]
            url_start = href.find('"') + 1
            url_end = href.rfind('"')
            new_url = href[url_start:url_end]
            has_quotes = new_url.find('"')

            if has_quotes != -1:
                new_url = new_url[:has_quotes]

            if new_url.find('http') == -1:
                if new_url.find('//') != -1:
                    new_url = "http:" + new_url
                else:
                    new_url = self.base_url + new_url

            clean_links[count] = new_url
            count += 1

        return clean_links

    def visit_link(self, url):
        if not self.find_link(url, self.visited_links):
            self.visited_links.append(url)
            #TODO: pop the item out of the self.links array

    def insert_links(self):
        for link in self.current_links:
            if link == self.base_url:
                continue
            if not self.find_link(link, self.links):
                self.links.append(link)

        self.current_links.clear()

    # noinspection PyMethodMayBeStatic
    def find_link(self, link, items):
        #TODO: implement a non-linear search
        for item in items:
            if item == link:
                return True
        return False
