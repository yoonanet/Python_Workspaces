#객체지향에서 가장 중요한 것이 정보은닉임. 정보은닉을 하는 수단에서 접근제어지시자가 있음
#파이썬에서의 접근제어지시자는 2종류를 제공해주고 있음 -> private, public : 파이썬에서는 키워드가 존재하지 않음. 어떻게 구분해서 작성할 수 있을까?
# 필드의 이름을 지정할 때, __의 작성을 통해 구분하여 작성할 수 있음.

class HasPrivate:
    def __init__(self):
        self.public1 = "public1" #기본적으로 public 선언이 됨. -> 따라서 클래스 밖이든 어디서든 접근이 가능했었던 것이다. (전형적인 public 선언 방법)
        self.__private1 = "private1" #필드 이름을 지정할 때 __를 붙이면 자동 private로 인식되어진다. 이름으로 private와 public을 구분짓는 것임!!
        self.__private2_ = "private2" #앞에 _ 두개, 뒤에 _ 한개를 필드이름에 붙여도 private로 인식됨!!
        self.__public2__ = "public2" #앞뒤로 _를 두개씩 붙이게 되면 public으로 인식이 됨!!

    def print_from_internal(self): #클래스 영역내에서는 접근제어지시자에 상관없이 직접적인 호출 가능
        print(self.public1)
        print(self.__private1)
        print(self.__private2_)
        print(self.__public2__)
        #우리가 정의하는 필드와 파이썬이 정의하는 필드를 구분짓기 위해서
        #파이썬이 선언하는 필드의 이름을 세번째와 네번째의 방법을 사용하고 있다.
        #따라서 개발자들이 작성한 필드라는 의미로 첫번째와 두번째로 선언하는 방법을 꼭 사용하도록 해야한다.

if __name__ == '__main__':
    obj = HasPrivate()

    obj.print_from_internal()

    print("=" * 10)

    print(obj.public1)
    #print(obj.__private1) #자동완성기능은 이용할 수 없음 / 실행을 하면 속성을 가지고 있지 않다는 에러로 결과를 보여줌!! / error -private
    #print(obj.__private2_) #동일하게 안된다는 에러메시지가 출력됨 / error -private
    print(obj.__public2__)
    
#상속: 부모클래스의 속성이나 기능을 그대로 가지고와서 사용할 수 있게끔 새로운 자식 클래스를 정의해서 그 자식클래스 안에 부모클래스의 모든 필드나 메소드들을
#     그대로 상속받아서 사용할 수 있게끔 제공되어지는 문법요소 => 중복되어지는 기능을 부모클래스로 정의해놓고 자식들이 부모클래스를 상속받는 구조
#중복의 코드를 최소화하겠다는 것이 문법적인 측면에서의 개념임.
#가장 중요한 개념은 상속의 조건하에 다형성, 메소드오버라이딩의 기능이다.
