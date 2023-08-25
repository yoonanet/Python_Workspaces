
if __name__ != '__main__': #만약 sub모듈에서 실행을 한다면 아무 동작이 되지 않을 것이다.
    print("*** sub.py start ***")
    print('name:{0}'.format(__name__))  # __main__
    print("*** sub.py end ***")
    #그러므로 메인으로 동작하지 않는 모든 sub모듈들에 이에 대한 if문을 넣어서 실행이 되지 않도록 구조를 잡아주도록 하는 것이다.
    #main이 아니라는 인폼을 동작과 코드로 파악할 수 있는 것임!!