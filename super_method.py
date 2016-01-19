class O(object):
    def method(self,):
        print 'O'   

class A(object):
    def method(self,):
        print 'A'

class B(object):
    def method(self,):
        print 'B'

class C(A):
    def method(self,):
        print super(C, self)
        print super(A, self)
        print dir(super(C, self))
        print dir(super(A, self))
        return super(A, self).method()

c = C()
c.method()