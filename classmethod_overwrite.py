class test(object):

    @classmethod
    def haha(cls,):
        print 'haha cls'

    def haha(self,):
        print 'haha self'


if __name__ == '__main__':
    t = test()
    t.haha()
    test.haha()