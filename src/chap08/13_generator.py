def generator():
    yield 0
    yield 1
    yield 2
    yield 3
    #리턴값을 지정하지 않음

def YourRange(start, end):
    current = start

    while current < end:
        yield current
        current += 1

if __name__ == '__main__':
    iterator = generator() #변수의 값을 담아주고 있음

    print(iterator.__next__()) #next메소드를 호출해주도록 함.
    print(iterator.__next__())
    print(iterator.__next__())
    print(iterator.__next__())
    #yield를 통해서 값을 지정하고 .을 통해 __next__함수를 호출하면 지정했던 값들이 순차적으로 출력되는 것을 확인할 수 있음

    #yield키워드의 기능은 넣어준 값을 가지고 있다가 내부에서는 yield가 현재의 값을 리턴하는 형태로 반환을 해주는데 여기서 동작이 끝나는 것이 아니라
    #반환의 값을 증가하면서 반복문으로 와서 대기하고 있는 형태로 동작이 되어지는 키워드이다.
    print('\n')

    for i in YourRange(0, 4):
        print(i)

