import sys #파이썬이 제공해주는 sys패키지를 import하도록 함

print(sys.builtin_module_names) #파이썬 인터프리터 내장 모듈
#builtin_module_names: 파이썬이 제공해주고 있는 탑제된 모듈의 이름을 확인할 수 있음
#파이썬은 '_'를 앞에 붙여서 일반 개발자들이 붙여주는 모듈과 구분이 지어지게끔 이름을 지어서 제공을 해주고 있다.

for path in sys.path:
    print(path) #안에 정보들을 출력하도록 함

#자바의 프로그램은 시작점이 어딘지 분명하게 파악할 수 있었음. (java.exe에서 실행을 하는데 클래스명이 있어야 했고, 클래스 안에 main이 있어야 했음)
#인터프리터 방식의 프로그래밍 언어들은 어디에서 실행을 하던지 상관없이 바로 실행하면서 결과를 확인할 수 있는 구조로 동작되는 언어였음
#이러한 언어의 맹점은 규모있는 프로젝트같은 경우 시작점이 어딘지를 알 수 없음!! 그렇다고 한 파일 안에 모든 소스코드들을 전부 다 작성할 수 없음
#그렇기 때문에 자바처럼 시작점의 개념이 존재해야 한다. 그래서 규모가 있는 프로젝트들은 자바와 마찬가지로 프로그램의 시작점부터 동작이 되어지는
#흐름으로 작성이 되어져야 하는데 그 구조를 메인모듈의 개념으로 구현을 해서 제공을 해주고 있다.

