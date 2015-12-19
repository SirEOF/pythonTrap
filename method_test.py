class MethodsTest(object):

    @staticmethod
    def st():
        return

    @classmethod
    def cl(cls):
        return

    def sl(self):
        return

mt = MethodsTest()

def pc(method):
    print method.__name__, method.__class__, method

pc(mt.st)
pc(mt.cl)
pc(mt.sl)
print '-------'
pc(MethodsTest.st)
pc(MethodsTest.cl)
pc(MethodsTest.sl)

