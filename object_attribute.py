class X(object):
    pass

x = X()
x.x = 1
print x.x

x = object()
x.x = 1
print x.x