from modulea import ClassA

class ClassC:
    def __init__(self):
        print("We instantiated from ClassC")

    def func_c(self, message):
        print("func_c ", message)
        ClassA.static_func_a("from ClassC")

