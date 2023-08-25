# 데코레이터 사용 용도(생성자)

class MyDecorator:
    def __init__(self, f):
        print("MyDecorator 생성자 호출()")
        self.func = f #함수를 입력으로 전달해주려고 한다는 것을 캐치할 수 있음

    def __call__(self):
        #print("Begin:{}".format(self.func.__name__))

        #***format메소드가 메세지 출력으로 많이 사용이 되다 보니까 약식으로 작성하여 쉽게 사용할 수 있는 형태도 지원을 해주고 있다.
        print(f"Begin:{self.func.__name__}")
        self.func() #변수에 ()를 해주고 있음 => 이때는 함수의 호출이 될 것이다!!!
        print(f"End:{self.func.__name__}")

def print_hello():
    print("Hello.")

if __name__ == "__main__":
    print_hello = MyDecorator(print_hello) #생성자에 함수를 전달하고 주소값을 변수에 담아주도록 한다. => 이때, 외부에서 정의한 함수명과 동일하게 담아줬음.
    
    print_hello() #***참조변수인데 함수처럼 호출하는 코드를 본다면 __call__메소드를 떠올리도록 한다.
    #데코레이터에 의해서 실제로는 클래스에 정의되어져 있는 __call__메소드가 호출되어진다.
    #print_hello를 함수 호출하듯이 호출해주게 된다면 내부에서는 print_hello가 참조 변수화 되어지면서 MyDecorator의 객체를 가리키고 있기 때문에 __call__의 메소드가 호출이 되어질 것이다.
    #즉, 함수를 호출하기 전과 후로 작업을 해야할 사항이 있다면 __call__메소드를 활용하면 된다. 