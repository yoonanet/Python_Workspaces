class ConstructorInit:

    def __init__(self, name, email): #값을 전달받아서 초기화 가능!
        self.name = name
        self.email = email

    def print_info(self):
        print('{0} : {1}'.format(self.name, self.email))

if __name__ == '__main__':
    hong = ConstructorInit('홍길동', 'abc@company.com')
    lee = ConstructorInit('이순신', 'xyz@company.com')

    hong.print_info()
    lee.print_info()