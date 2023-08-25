
#파이썬, R, 자바스크립트는 내부에서 다 클래스화해서 데이터들을 객체로 처리해주고 있음 -> 그렇기 때문에 기본자료형과 참조자료형의 개념이 등장하지 않는 것임
#참조자료형 선언 키워드 => 자바와 동일하게 class임 (우리가 정의한 자료형이라는 인폼을 이름으로 확실하게 할 수 있게끔 첫글자를 대문자로 권고)
#자바에서는 필드를 먼저 생성하고 그 다음에 생성자를 따로 정의했었지만 파이썬에서는 따로 구분짓는 것이 아니라 생성자를 정의하면서 필드를 정의함
#파이썬에서는 생성자 이름을 통일 시켜서 __init__(self)로 고정을 시켜놨음!!!
#필드를 생성자 안에다가 정의를 하자는 것임 / 자바에서 this(나 자신의 메모리 주소값을 가리킴)에 해당하는 것이 self임. 파이썬에서는 입력으로 self를 전달받아서 처리할 수 있도록 명료함을 제공
#객체라는 대상의 특징만을 담아주고 있는 특화된 기능이라는 의미로 메소드라는 용어를 사용하는 것임. (바라보는 대상에 국한된 것)
#파이썬에서 변수나 함수명에 __를 붙이고 있는데 그 이유가 사용자가 정의한 이름과 시각적으로 구분할 수 있게끔 하는 의도가 포함되어져 있는 것이다.
class Car:
    #자바에서는 필드를 초기화할 필요가 없었음!! -> 그이유는 필드만 선언하고 디폴트값으로 초기화시키지 않더라도 내부적으로 자동 초기화를 해주고 있었음
    #파이썬에서는 자료형을 따로 지정해주지 않기 때문에 선언만 하면 에러가 나는 것이다. 그렇기 때문에 반드시 초기화를 시켜주는 코드가 작성이 되어져야 한다.
    #파이썬은 생성자를 통해서 초기화 값들을 지정해주기 때문에 자바의 필드처럼 따로 꺼내서 초기화를 할 필요가 없다.
    #***또한, 생성자 안에 필드 데이터를 클래스로 감싸서 객체로 처리하기 때문에, 리턴하는 순간 주소값으로 리턴을 해준다!!

    #생성자 목적: 필드값의 초기화
    def __init__(self): #파이참이라는 툴을 사용하면 self라고 자동완성이 되어짐 -> 다른 툴을 사용할 때 자동완성이 되지 않을 수 있기 때문에 입력의 매개변수로 꼭 넣어줘야 한다.
        self.color = 0xFF0000 # 차량 색상 - 헥사코드색상을 출력하면 10진수로 변환하여 출력됨 (직관적이지 못함)
        self.wheel_size = 16 # 바퀴의 크기
        self.displacement = 2000 # 엔진 배기량
    
    #클래스 안에 정의되는 함수는 대상에 국한된 기능이기 때문에 메소드라고 불러준다. (대상에 특화된 기능이라는 의미로 메소드)
    #메소드를 선언하는 방법은 함수 선언하는 방법과 동일하다. 하지만 메소드를 정의할 때, 첫번째 매개변수 자리에 self를 정의하는 것이 문법적으로 강제되어져 있음!!
    def forward(self): # method(전진)
        print("주행중입니다.")

    def backward(self): # 후진
        pass

    def turn_left(self): # 좌회전
        pass

    def turn_right(self): # 우회전
        pass


#객체지향은 데이터를 객체중심적으로 바라보겠다는 것이였음. 바로 연결지어서 생각하려면 테이블을 떠올리면 됨
if __name__ == '__main__': #main시작점의 구조를 잡아주도록 함
    print("= start =")

    print(type(Car)) # <class 'type'>

    my_car = Car() #파이썬에서는 클래스를 정의하는 순간 인스턴스화 되어졌을 때 self가 존재가 드러나는 의미이기 때문에 생성할 때 별도로 self를 지정하지 않게끔 문법적인 사항을 정의하고 있다.
    #별도로 new의 키워드 상관없이 위와 같은 형식으로 요청하면 되는 것임 / 함수호출의 형식과 다를바가 없음.
    #만약 car의 소문자로 정의를 했다고 한다면 함수를 호출하는 것인지 인스턴스를 생성하는 것인지 구별을 할 수가 없다.
    #그렇기 때문에 함수를 정의할 때는 첫글자를 소문자로, 클래스를 정의할 때는 첫글자를 대문자로 정의하는 것을 권고한다.
    #파이썬에서 인스턴스를 요청하면 4가지의 동작을 함 => 생성을 요청한 인스턴스의 메모리 공간 할당, self에 시작주소값 저장, 생성자 호출, 복귀하면서 self값 리턴
    #시작 주소값을 리턴하는 이유는? 데이터를 필요로 할 때, 메모리에 접근하기 위함이다.
    #메모리에 할당된 필드와 메소드를 인스턴스필드, 인스턴스메소드라고 불러줌!!
    #메모리에 접근할 때는 .연산자로 접근할 수 있게끔 자바와 동일하게 문법 요소를 제공해주고 있음

    print(my_car.color)  # 인스턴스 변수에 접근
    print('0x{:02X}'.format(my_car.color))
    #16진수로 출력을 하고 싶을 때는 :X로 지정을 해주면 헥사코드로 출력을 해준다.
    #16진수의 자리가 두자리씩 표현을 하고 있을 때 :2X로 표현할 수 있고, 한자리의 숫자값일 때 0의 값을 채워달라고 :02X로 지정해주면 된다.
    #즉, 두자리가 아닐때 0의 값으로 채워달라는 의미인 것이다.

    my_car.forward()     # 인스턴스 메소드에 접근
    my_car.backward()
    my_car.turn_left()
    my_car.turn_right()

