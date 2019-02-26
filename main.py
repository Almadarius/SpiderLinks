from Crawler import WebCrawler

url = input("Input the URL: ")
spider = WebCrawler(url)
spider.get_links()

for link in spider.current_links:
    print(link)
