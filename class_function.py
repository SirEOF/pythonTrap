class func(object):

    def __init__(self, x):
        self.x = x

    def __call__(self, y):
        return self.x * y

f = func(2)
print f(3)
