from my_package.calculator import *
#가지고 올 모듈을 하나하나 다 적어줘도 되지만 *의 기호를 사용하여 패키지의 모듈 안에 정의된 함수를 모두 import할 수도 있다.
#import한 함수(변수)의 불명확성, 가독성이 떨어진다. 비권장.

#모듈안에 정의되어져 있는 모든 함수들을 다이렉트로 호출할 수 있다.
print(plus(10, 5))
print(minus(10, 5))
print(multiply(10, 5))
print(divide(10, 5))