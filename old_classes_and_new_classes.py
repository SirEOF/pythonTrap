class A:
    pass

class B(object):
    pass

a = A()
b = B()

print dir(a)
print dir(b)

print a.__class__, type(a)
print b.__class__, type(b)
print object.__class__, type(object)
print type.__bases__, type.__class__, type(type)