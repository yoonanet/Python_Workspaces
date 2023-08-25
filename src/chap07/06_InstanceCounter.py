#파이썬에서 추가적으로 제공해주는 데코레이터!!
class InstanceCounter:
    count = 0 #클래스 변수로 선언되어진 것

    def __init__(self): #self는 인스턴스를 생성하는 순간 메모리가 할당되고 메모리의 시작주소값을 self에 담아주는 스킴이다.
        self.count += 1 #맴버변수 / 인스턴스 변수임. => 인스턴스가 생성됐을 때 생성되는 변수
        InstanceCounter.count += 1 #클래스 변수이기 때문에 생성자 안에 필드와 상관없이 할당되기 때문에 접근이 되는 것임.

    @classmethod #classmethod데코레이션: 클래스메소드의 데코레이터를 이용할 때 입력에 self가 아닌 class의 약자로 cls를 붙여줘야 한다.
    def print_instance_count(cls): #class의 이름으로 이 메소드를 호출하게끔 기능을 부여하겠다라는 의미인 것이다. 마치 static메소드처럼 클래스 이름으로 호출이 가능하게끔 메소드를 정의하는 것임
        print(cls.count)



if __name__ == '__main__':
    InstanceCounter.count = 10 #클래스변수의 특징 -> 인스턴스 생성에 상관없이 언제든지 메모리에 접근해갈 수 있는 것
    # InstanceCounter.print_instance_count() #error - 이 메소드는 static메소드가 아니기 때문이다.

    x = InstanceCounter()
    #x.print_instance_count() # 11 ==> self.count 인스턴스가 생성되면서 +1
    InstanceCounter.print_instance_count() #클래스 이름으로 static메소드가 아닌 메소드를 호출하도록 하는 것임.

    y = InstanceCounter()
    y.print_instance_count() # 12
    #주의) self.count로 누적을 하면 count를 누적을 하는 것이 아니다. self.count와 count는 다른 변수임!!
    #     self.count는 인스턴스 변수이고, count는 클래스 변수인 것이다.
    # 클래스 변수와 인스턴스 변수는 서로 다른 변수이기 때문에, 각각 독립적으로 값을 변경하고 유지할 수 있다.
    # 따라서 클래스 변수와 인스턴스 변수에 동시에 +1을 해줬을 때, 서로 다른 값이 출력되는 것이다.