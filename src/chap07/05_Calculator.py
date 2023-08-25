class Calculator:

    # 파이썬만이 제공해주는 기능 중에 메소드를 정의하는데 메소드 위에 @staticmethod(파이썬 내부에 탑제된 기능임)를 지정해줄 수 있음
    # 파이썬에서는 @를 장식이라는 의미로 데코레이터 메소드라고 불러준다. => 자바에서 @는 어노테이션
    # 함수 위에 @staticmethod를 정의하게 되면 그때는 self를 쓰면 안되고 필요가 없어진다.(static메소드는 인스턴스 생성 전에 만들어지기 때문에 self가 생성하기도 전이라 필요없는 것)
    # @staticmethod는 클래스 메소드임!!
    @staticmethod
    def plus(x, y):
        return x + y

    @staticmethod
    def minus(x, y):
        return x - y


if __name__ == '__main__':
    #static메소드는 method메모리영역에 딱 한번만 할당이 되어진다는 특징을 가짐
    #=> 인스턴스생성을 하지 않고도 클래스의 이름으로 다이렉트 접근 가능
    #   static method는 클래스의 이름만 보면 바로 메모리를 생성하기 때문에 직접적인 호출이 가능한 것이다.
    print('{0} + {1} = {2}'.format(7, 4, Calculator.plus(7, 4)))
    print('{0} - {1} = {2}'.format(7, 4, Calculator.minus(7, 4)))