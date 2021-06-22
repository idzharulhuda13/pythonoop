class A:
    def method_A(self):
        print("Ini adalah method A")


class B:
    def method_B(self):
        print("ini adalah method B")


class C(A, B):
    pass


c = C()

c.method_A()
c.method_B()
