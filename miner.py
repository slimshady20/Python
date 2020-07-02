from dataclasses import dataclass
import re

import nltk
from nltk.tokenize import word_tokenize
from konlpy.tag import Okt
import pandas as pd
from nltk import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt


@dataclass
class Entity:
    context: str
    fname: str
    target: str

    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def target(self) -> str: return self._target

    @target.setter
    def target(self, target): self._target = target


class Service:
    def __init__(self):
        self.texts = []
        self.tokens = []
        self.noun_tokens = []
        self.okt = Okt()
        self.stopwords = []
        self.freqtxt = []

    def extract_texts(self, payload):
        print('>>corpus 에서 token 추출')
        filename = payload.context = payload.fname
        with open(filename, 'r', encoding='utf-8') as f:
            self.texts = f.read()
        print(f'1단계 결과물 : {self.texts[:300]}')

    def tokenize(self):
        print('1. corpus에서 한글 추출')
        texts = self.texts.replace('\n',' ')
        tokenizer = re.compile(r'[^ㄱ-힣]')
        # ^는 not 과 start 두가지 개념이 있음
        # [^]는 not, ^[]은 start 의미로 표현됨
        self.texts = tokenizer.sub(' ', texts)  # 한글이 아닌것은 ' ' 처리해서 한글만 남겨라.
        print(f' 2단계 결과물: {self.texts[:300]}')

    def conversion_token(self):
        print('3. 한글 token 변환')
        self.tokens = word_tokenize(self.texts)
        print(f' 3단계 결과물: {self.texts[:300]}')

    def compound_noun(self):
        print(' 4. 복합 명사화')
        arr_ = []
        for token in self.tokens:
            token_pos = self.okt.pos(token)
            _ = [txt_tags[0] for txt_tags in token_pos
                 if txt_tags[1] == 'Noun']
            if len("".join(_)) > 1:
                self.noun_tokens.append("".join(_))
            self.noun_tokens = "".join(arr_)
            print(f'4단계 결과물 : {self.noun_tokens[:300]}')

    def extract_stopword(self):
        print('5. 노이즈 코퍼스에서 token 추출')

    def filtering_text_with_stopword(self):
        print('6. 노이즈 필터링 후 시그널 추출')

    def frequent_text(self):
        print('7. 시그널 중에 사용빈도 정렬')

    def wordcloud(self):
        print('8. 시각화')


class Controller:
    def __init__(self):
        pass

    def download_dictionary(self):
        nltk.download('all')

    def data_analysis(self):
        entity = Entity()
        service = Service()
        entity.context = './data/'
        entity.fname = 'kr-Report_2018.txt'
        service.extract_texts(entity)
        service.tokenize()
        service.conversion_token()
        service.compound_noun()
        service.extract_stopword()
        service.filtering_text_with_stopword()
        service.frequent_text()
        service.wordcloud()


def print_menu():
    print('0.Exit')
    print('1. 사전 다운로드\n')
    print('2. 데이터 분석')
    return input('메뉴선택\n')


app = Controller()
while 1:
    menu = print_menu()
    if menu == '1':
        app.download_dictionary()
    if menu == '2':
        app.data_analysis()
    if menu == '0':
        break
