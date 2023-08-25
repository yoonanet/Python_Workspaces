
class ClassVar:
    text_list = []     # 클래스 변수(field/멤버변수)
    #생성자를 생성할 때 위에 필드를 초기화하는 방식을 사용해도 됨

    def add(self, text):     # 멤버 메소드
        #호출이 되어지는 시점에 이 메소드 안에서 사용할 데이터를 전달받을 수 있어야 한다. 그때는 self뒤에 파라메타만 추가해주면 된다.
        #내 클래스 안에 정의된 변수라고 하더라도 단독으로 접근할 수 없음! 무조건 self.을 통해 접근을 하도록 해야한다.
        self.text_list.append(text) #값들을 계속해서 누적하는 것임

    def print_list(self): # 출력 기능
        print(self.text_list)

if __name__ == '__main__':
    x = ClassVar()
    x.add('a')
    x.add('b')
    x.add('c')
    x.print_list()

    y = ClassVar()
    y.add('x')
    y.print_list() #새롭게 메모리 할당을 요청해서 값들을 추가했는데 기존값에 누적돼서 출력되고 있음!!
    #자바에서는 static이라는 키워드를 사용한 필드를 떠올리기. => static은 method영역에 살아나면서 global화 되어짐
    #static이름이 붙어있으면 메모리에 무조건 할당이 되어졌었음. 한번만 메모리에 할당이 돼서 모든 인스턴스들이 공유하게 된다.
    #별도의 키워드를 파이썬에서 제공해주고 있지 않음. 클래스를 정의할 때 생성자가 아닌 필드로 선언하면 static이라는 변수처럼 처리가 되어지는 것이다.
