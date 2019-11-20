class A:
    def func(self):
        print('A.func')

class B(A):
    def func(self):
        print('B.func')
    
class C(A):
    def func(self):
        super().func()
        print('C.func')
    
class D(C, B):
    pass