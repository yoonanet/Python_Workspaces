#실질적인 부모의 생성자 호출 방법에 대한 실습
class A:
    def __init__(self):
        print("A 생성자 호출()")
        self.message = "Hello"


class B(A):
    def __init__(self): #원래 생성자 호출은 프로그래밍 주체인 자바, 파이썬만이 가능하게끔 처리해주는 것이 타당하지만 super를 통해 접근하는 것이 가능하다.
        super().__init__() #부모클래스이름에서 super().을 통해 생성자를 호출해주고 있음
        # super().__init__(self): 호출하면서 두 개의 아규먼트가 전달되고 있다고 에러남.
        # 즉, super() 내부에서 부모의 객체를 전달하고 있기 때문에 self를 따로 전달해주지 않아도 되는 것임!! -> 주의하도록 해야함!!
        # ***현재 진행한 super()를 통해 생성자에 접근하는 것을 전통적으로 권고하는 사항이다.
        print("B 생성자 호출()")


if __name__ == '__main__':
    obj = B()

    print(obj.message)
