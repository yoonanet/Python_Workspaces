# Iterator와 순회 가능한 객체

''' 두 줄 이상의 아주 긴 문자열 -> 작은 따옴표 3개 (작은따옴표와 큰따옴표를 구분하지 않음)
R과 파이썬에서 동일하게 제공해주는 자료형으로써 두 줄 이상의 문자열 데이터를 문자열로 처리하는 키워드이다.
-> 변수를 선언해서 담아주고 필요할 때 불러서 사용하는 스킴
-> R이나 파이썬에서는 문자열을 실행하는 입장에서 변수를 선언하여 보관하고 있지 않으면
   메모리에 할당을 하고 난 다음에 실행이 되어도 가리키는 참조변수가 없기 때문에
   문자열에 접근할 수 없어서 바로 소멸을 시켜버리는 것이다. 그래서 이 기호를 주석의 용도로 상당수 활용된다!!
-> R이나 파이썬에서는 두라인이상의 텍스트형태를 주석처리할 문법적인 요소를 제공해주고 있지 않기 때문에 문자열 기호를 일반적으로 사용하는 것이다.

for i in range(0, 5): #range는 클래스로 정의를 해서 제공을 해주고 있는 참조 자료형이다.
    print(i)
'''

#위 range동작이 실질적으로 아래와 같은 코드로 내부에서 동작됨
iterator = range(5).__iter__()
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())

######################################################################################
class MyRange: #Renge()와 같은 일을 하는 클래스 정의
    def __init__(self, start, end):
        print('init')
        self.current = start
        self.end = end

    def __iter__(self): #파이썬은 인스턴스에 대한 생성을 요청할 때 생성자만 호출하는 것이 아니라 __iter__메소드도 자동 호출을 해주게끔 내부에서 처리가 되어진다.
                        # +) __next__메소드도 같이 호출이 되어진다. (반복문에서는 순차적으로 호출이 되어지는 구조임)
        print('iter')
        return self #입력으로 전달받은 self를 리턴해줌으로써 내 자신의 주소값을 반환하도록 함

    def __next__(self):
        #__next__가 호출이 되면 조건을 먼저 체크하는데 내부적으로 보면 하나씩 값을 누적해가면서 조건이 불만족할 때까지 반복해간다.
        print('next')
        if self.current < self.end: #시작하는 값이 작을 때,
            current = self.current #시작값을 담아주고
            self.current += 1 #시작값을 증가시킴
            return current #기존 시작값을 리턴시킴
            #current++를 붙여줬을 때 내부 기능이 위처럼 정의될 수 있다. ++current일 때는 self.current += 1을 리턴으로 넣어주게 됨
        else:
            raise StopIteration() #예외 발생 키워드 => raise : 파이썬이 정의하고 있는 예외처리 클래스의 인스턴스를 생성해주도록 함

if __name__ == '__main__':
    for i in MyRange(0, 5):
        print(i)
