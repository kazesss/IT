class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return f"Значение радиуса: {self.radius}"

    def set_radius(self, new_radius):
        self.radius = new_radius


ball = Circle(15)
print(ball.get_radius(), ball.set_radius(13), ball.get_radius())
