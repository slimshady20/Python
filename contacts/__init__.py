from contacts.controller import Controller
if __name__ == '__main__':
    def print_menu():
        print('0. Exit')
        print('1. 연락처추가')
        print('2. 연락처 이름 검색')
        print('3. 연락처 전체 목록')
        print('4. 연락처 이름 삭제')
        return input('Menu\n')

    app = Controller()
    while 1:
        menu = print_menu()
        if menu == '1':
            app.register(input('이름\n'),
                         input('전화번호\n'),
                         input('이메일\n'),
                         input('주소\n'))

        if menu == '2':
            result = app.search(input('입력할 이름 검색\n'))
            print(str(result))
        if menu == '3':
            result= app.list()
            print('\n'.join(str(i) for i in result))
        if menu == '4':
            pass
        if menu == '4':
            pass
        if menu == '0':
            pass

