# 기존 모듈에 새이름 부여 사용 가능 -> 가장 선호하는 방법
import my_package.calculator as c
#import하여 함수를 호출할 때 패키지와 모듈명까지 전부 적어줬어야 했기 때문에 코드가 너무 길어짐 => 그렇기 때문에 위치를 별칭으로 지정해주도록 한다. 
# !!as가 별칭키워드!!

print(c.plus(10, 5))
print(c.minus(10, 5))
print(c.multiply(10, 5))
print(c.divide(10, 5))
