class Shapes:
    def __init__(self, name, shape):
        self.name = name
        self.shape = shape
    
    def speak(self):
        print("Hello, my name is", self.name, "and I am a", self.shape)

p1 = Shapes("kellie","circle")
p1.speak()