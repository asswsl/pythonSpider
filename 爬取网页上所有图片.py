from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import random
import time


class ImgSpider():
    def __init__(self, url, path):
        ua = UserAgent()
        self.url = url
        self.path = path
        self.headers = {'User-Agent': ua.random}

    def get_html(self):
        req = requests.get(url=self.url, headers=self.headers)
        html = req.text
        self.parse_html(html)

    def parse_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        imglinks = soup.find_all('img', src=True)  # 选择具有src的所有图片
        self.download_img(imglinks)

    def download_img(self, links):
        i=0
        for link in links:
            res = requests.get(link['src'])

            # print(link['src'])
            with open(self.path + '\{}.png'.format(i + 1), 'wb') as f:
                f.write(res.content)
            i+=1
        f.close()


    def run(self):
        self.get_html()
        time.sleep(random.randint(1, 2))


if __name__ == '__main__':
    url = input('请输入要爬取的网站url：')
    path = input('请输入图片保存地址：')
    spider = ImgSpider(url, path)
    spider.run()
