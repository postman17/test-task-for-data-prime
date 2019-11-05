import requests
from bs4 import BeautifulSoup


class Parser:
    def __init__(self, url, page_num, main_tag, tag_class, main_tag_article, main_tag_article_class):
        self.url = url
        self.page_num = int(page_num)
        self.main_tag = main_tag
        self.tag_class = tag_class
        self.tag_article = main_tag_article
        self.tag_article_class = main_tag_article_class
        self.response = self._num_pages()
        self.clean_data = self._clean_news()

    def _num_pages(self):
        pages_list = []
        for num in range(1, self.page_num + 1):
            pages_list.append(self._request(self.url + str(num)))
        return pages_list

    def _request(self, url):
        response = requests.get(url)
        return response.text

    def _clean_news(self):
        data = []
        for html_reponse in self.response:
            num_list = []
            bs = BeautifulSoup(html_reponse, 'html.parser')
            raw_data = bs.find_all(self.main_tag, self.tag_class)
            for item in raw_data:
                article = {}
                article['title'] = item.a.text
                article['link'] = item.a['href']
                article['text'], article['img'] = self._get_article(item.a['href'])
                num_list.append(article)
            data.extend(num_list)
        return data

    def _get_article(self, link):
        response = self._request(link)
        bs = BeautifulSoup(response, 'html.parser')
        raw_data = bs.find_all(self.tag_article, self.tag_article_class)
        raw_text = raw_data[0].find_all('p')
        img = raw_data[0].find('img')
        text = ''
        for item in raw_text:
            text += item.text
        return text, img['src']

