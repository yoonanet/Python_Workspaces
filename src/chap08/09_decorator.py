# 데코레이터(Decorator)

class Callable: #가변인자는 여러 데이터를 전달받을 수 있는데 *은 튜플로 데이터를 관리하고, **는 딕셔너리로 데이터를 관리함
    def __call__(self): #(self, *args, **kwargs)에서 *args, **kwargs는 NULL로 초기화가 되어져 있어서 함수 호출 시에 생략이 가능함.
        print("I am called.")

if __name__ == '__main__':
    obj = Callable()

    obj() #참조변수인데 함수를 호출하는 형태로 호출 -> 결과적으로 __call__함수가 호출됨!!
