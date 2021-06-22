class A:

    def show(self):
        print("ini adalah show a")


class B:

    def show(self):
        print("ini adalah show b")


class C(A, B):

    def show(self):
        print("ini adalah show c")


c = C()
c.show()  # urutan C - A - B tergantung inheritance C(A,B)
help(c)
