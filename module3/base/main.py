from module3.base.vehicle import Vehicle

class Car(Vehicle):
    def run(self):
        return 20


if __name__ == "__main__":
    car = Car()
    print(car.setColor("#111"))
    print(car.getColor())
