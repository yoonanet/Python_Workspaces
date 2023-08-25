
class InstanceVar:

    def __init__(self):
        self.text_list = []     # instance 변수 (메모리에 할당된 변수를 말함)

    def add(self, text):     # 멤버 메소드
        self.text_list.append(text)

    def print_list(self): # 출력 기능
        print(self.text_list)

if __name__ == '__main__':
    x = InstanceVar()
    x.add('a')
    x.add('b')
    x.add('c')
    x.print_list()

    y = InstanceVar()
    y.add('x')
    y.print_list()
    #결과를 확인해보면 생성된 인스턴스에 따라서 데이터가 저장되어져 있는 것을 확인할 수 있다. (개별적인 메모리할당 -> 그때 인스턴스 변수로 잡히게 되는 것임)
    #생성자함수에서 선언되어지는 변수는 필드의 개념으로 선언되어지는 것이다.