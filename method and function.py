def x():
    pass

print hasattr(x, 'im_func')
print hasattr(x, 'im_self')
print dir(x)
print '-' * 20

######## instance method ##########
class C(object):
    def x(self):
        pass

x = C.x

print hasattr(x, 'im_func')
print hasattr(x, 'im_self')
print dir(x)
print '-' * 20

########## class method ###########
class C(object):
    @classmethod
    def x(cls):
        pass

x = C.x

print hasattr(x, 'im_func')
print hasattr(x, 'im_self')
print dir(x)
print '-' * 20

######## static method ##########
class C(object):
    @staticmethod
    def x():
        pass

x = C.x

print hasattr(x, 'im_func')
print hasattr(x, 'im_self')
print dir(x)
print '-' * 20