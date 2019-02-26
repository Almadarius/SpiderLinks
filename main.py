from Crawler import WebCrawler

url = 'http://www.cnn.com'
spider = WebCrawler(url)
links = spider.get_links()

for anchor in links:
    # print(anchor)

    tag_string = str(anchor)
    href_index = tag_string.find('href')
    href = tag_string[href_index:]
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
            new_url = url + new_url

    print(new_url)



