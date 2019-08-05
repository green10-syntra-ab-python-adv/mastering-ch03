from .modulea import Class_A

class Class_B(Class_A):
    def __init__(self):
        print("We instantiated from Class_B")
        self.func_a()

class Class_C():
    def __init__(self):
        print("We instantiated from Class_C")
