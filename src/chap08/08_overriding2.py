class Car:
    def ride(self):
        print("Run")

class FlyingCar(Car):
    def ride(self):
        # ride() 내 자신에 있는 메소드를 바라봐서 무한 반복됨
        super().ride() #주의) super에서 ()가 있어야 함!! # 부모 클래스에 정의된 메소드 호출.
        print("Fly")

if __name__ == '__main__':
    car = Car()
    #car.ride()  # Run

    fly = FlyingCar()
    fly.ride() # Fly

    #클래스 밖에 영역에서는 FlyingCar로 인스턴스를 생성하고 오버라이딩 되어져 있는 메소드의 부모 메소드를 호출할 수 있는 방법은 아예 없다.
    #하지만 자식에서는 부모에 정의된 메소드 호출이 가능함!! -> super(부모의 생성자 호출뿐만 아니라 부모에 정의된 메소드 호출도 가능했었음)를 활용하도록 한다.