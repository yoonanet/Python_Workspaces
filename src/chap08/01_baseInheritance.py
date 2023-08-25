class Base:
    def __init__(self):
        print(self)
        self.message = "Hello, World"

    def print_message(self):
        print(self.message)

class Derived(Base): #파이썬은 상속을 정의할 때 클래스 이름 옆에 괄호로 부모클래스를 지정해주면 된다.
    pass

if __name__ == '__main__':
    base = Base()
    base.print_message()

    derived = Derived()
    #상속에 관계일 때는 부모클래스에 가서 부모 크기 만큼의 영역을 할당을 하고, 할당이 끝나면 복귀해서 자식클래스의 크기만큼을 계산해서 영역을 할당해줄 것이다.
    #즉, 부모와 자식의 모든 클래스 크기를 계산해서 메모리를 할당할 것임. 그 할당된 메모리의 시작 주소값을 리턴해줄 것이다.
    derived.print_message() #부모에 정의된 메소드이지만 자식 메모리에 할당이 되어졌기 때문에 내가 가지고 있는 메소드인 것처럼 호출 가능