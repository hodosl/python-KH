from cmath import pi


class Circle:
    def __init__(self, radius: float):
        self.radius = radius
            
    def get_radius(self) -> float:
        return self.radius
    
    def calculate_circle_area(self) -> float:
        return self.radius**2*pi

    def __str__(self): # print(circle) alapaértelmezést valami sokkal értelmezhetőbbre írja át
        return f"Kor {self.radius} sugaru."
    
    def __eq__(self, other):
        if not isinstance(other, Circle):
            return False
        else:
            return self.radius == other.radius

circle = Circle(10)
print(circle.get_radius())
print(circle.calculate_circle_area())

print(circle)

another_circle = Circle(10)

print(circle == another_circle) # azt hasonlítja össze hogy ugyyanazon a memória címen vannak e? de nem így false mert két külön objektumról van szó, kivéve ha van __eq__


