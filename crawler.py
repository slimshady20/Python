from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
import requests


class Model:
    def __init__(self):
        self._url = ''
        self._parser = ''
        self._path = ''
        self._api = ''

    @property
    def url(self) -> str: return self._url

    @url.setter
    def url(self, url): self._url = url

    @property
    def parser(self) -> str: return self._parser

    @parser.setter
    def parser(self, parser): self._parser = parser


class Service:
    def __init__(self):
        pass

    def bugs_music(self, payload):
        soup = BeautifulSoup(urlopen(payload.url), payload.parser)
        n_artists = 0
        n_title = 0
        for i in soup.find_all(name='p', attrs=({'class': 'title'})):  # 'class' : 'title' 튜플 tuple
            n_title += 1
            print(str(n_title) + '위')
            print('노래제목: {}'.format(i.text))


class Controller:
    def __init__(self):
        self.service = Service()
        self.model = Model()

    def bugs_music(self, url):
        self.model.url = url
        self.model.parser = 'lxml'
        self.service.bugs_music(self.model)


def print_menu():
    print('0. EXIT')
    print('1. 벅스 크롤링')
    print('2 영화 크롤링')
    return input("Menu\n")


app = Controller()
while 1:
    menu = print_menu()
    if menu == '0':
        break
    if menu == '1':
        app.bugs_music('https://music.bugs.co.kr/chart')
