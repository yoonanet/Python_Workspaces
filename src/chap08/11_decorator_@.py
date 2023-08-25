# @decorator : 자바에서는 @로 시작되어지는 요소들을 어노테이션이라고 부르고 있었는데 파이썬에서는 데코레이터라고 불러주고 있음
# 데코레이터(파이썬만이 제공해주는 기능)의 역할: 파이썬 내부에서 자신들이 정의하고 있는 클래스의 __call__메소드를 함수로 정의하여 제공해주고 있는 개념이였고,
#                                        데코레이터로 연결시킨 함수에 이름으로 클래스에 정의되어져 있는 __call__메소드를 호출시키도록 한 것이다.

class MyDecorator:
    def __init__(self, f):
        print("MyDecorator 생성자 호출()")
        self.func = f  

    def __call__(self):
        # print("Begin:{}".format(self.func.__name__))

        print(f"Begin:{self.func.__name__}")
        self.func()  
        print(f"End:{self.func.__name__}")

@MyDecorator #MyDecorator자료형을 연결하도록 함
def print_hello():
    print("Hello.")

if __name__ == "__main__":
    # print_hello = MyDecorator(print_hello) 데코레이터가 이 코드를 실행해주는 기능이였음

    print_hello()