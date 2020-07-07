import pandas as pd


class Entity:
    context: str
    fname: str
    train: object
    test: object
    id: str
    label: str

    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def train(self) -> object: return self._train

    @train.setter
    def train(self, train): self._train = train

    @property
    def test(self) -> object: return self._test

    @test.setter
    def test(self, test): self._test = test

    @property
    def id(self) -> str: return self._id

    @id.setter
    def id(self, id): self._id = id

    @property
    def label(self) -> str: return self._label

    @label.setter
    def label(self, label): self._label = label


class Service:
    def __init__(self):
        self.entity = Entity()

    # def new_entity(self, payload):
    #     this = self.entity
    #     this.context = './data/'
    #     this.fname = payload
    #

    def new_model(self, payload):
        this = self.entity
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)


class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()

    # enitity 하고 service를 모아서 모델링에서 합친다.
    def modeling(self, train, test):
        service = self.service
        this = self.preprocess(train, test)
        this.label = service.create_label()
        this.train = service.create_train()
        return this

    def preprocess(self, train, test):
        service = self.service
        this = self.entity
        this.train = service.new_model(train)
        print(f'트레인의 컬럼 : {this.train.columns}')


def print_menu():
    print('0. Exit')
    print('1. 현재 처리 상태')
    return input("메뉴 선택\n")


app = Controller()
while 1:
    menu = print_menu()
    if menu == '1':
        app.preprocess('test.csv', 'train.csv')
        break;
