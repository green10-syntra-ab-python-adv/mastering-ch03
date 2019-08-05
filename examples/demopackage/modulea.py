
class Class_A:
    def __init__(self):
        print("We instantiated from Class_A")
    def func_a(self):
        print("Execution of func_a from Class_A")
        c = Class_C()

from .moduleb import Class_C

