class A(object):
    def method(self, x):
        print x

class B(A):
    _method = A.method

    def fake_method(self, x):
        x = -x
        return self._method(x)

    def method(self, x):
        return self.fake_method(x)

b = B()
b.method(3)