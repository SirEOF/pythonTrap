import inspect

class Base(type):

    @staticmethod
    def func(self):
        return globals()[inspect.currentframe().f_code.co_name].__name__

    def __new__(cls, name, bases, dct):
        # print name, bases, dct, Base.func
        Base.func.__name__ = 'haha'
        dct['haha'] = Base.func
        return super(Base, cls).__new__(cls, name, bases, dct)


class Haha(object):
    __metaclass__ = Base

    a = 1

print '-----------------------------------------------'
# ['__call__', '__class__', '__cmp__', '__delattr__', '__doc__',
# '__format__', '__func__', '__get__', '__getattribute__', '__hash__', 
# '__init__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
# '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
# 'im_class', 'im_func', 'im_self']

print Haha().haha.__func__.func_name
print Haha().haha()
