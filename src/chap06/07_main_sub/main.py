import sub #같은 위치에 파일이 존재하면 모듈이름만 적어주면 된다.

#코드 실행 결과를 보면 import해온 sub.py가 먼저 실행되고 이후에 main에 있는 코드가 실행되고 있음
#sub.py를 main.py모듈에서 실행을 시켰을 때 __name__값이 모듈의 이름으로 바뀌어서 실행이 되고 있음.
#원래는 __name__필드는 __main__을 반환해준다. 하지만 자신의 모듈이 아닌 다른 모듈에서는 __name__필드의 값이 자신의 모듈 이름으로 셋팅이 되어진다!!! 이 구조 형식을 기억하고 있기.
print("=== main.py start ===")
print('name:{0}'.format(__name__)) # __main__
print("=== main.py end ===")