#from my_package.calculator import plus
#from my_package.calculator import minus
from my_package.calculator import plus, minus
#from을 통해서 다른 위치에 있는 모듈을 지정해주고, 특정 함수만 지정해줄 수 있는 것임. => 하지만 이때, 제약사항이 발생함. 세세하게 살펴보는 것을 지양.
#from import 구문을 활용하게 되면 바로 함수의 이름만으로 바로 접근이 가능하다. / 같은 모듈에 있는 함수를 여러 개 가지고 와야 한다면 ,콤마를 이용해서 지정하여 한꺼번에 가져올 수 있다.

print(plus(10, 5))
print(minus(10, 5))
#print(multiply(10, 5)) #모듈에서 함수를 가지고 오지 않았기 때문에 에러를 내고 있다.

