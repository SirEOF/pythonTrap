class test:
    haha = 'haha'
    def get_func(self):
        return self.func

    def func(self):
        print self.haha

class another_test:
    haha = 'haha'
    def func(self):
        print self.haha
    @classmethod
    def func2(self):
        print self.haha

if __name__ == '__main__':
    t = test()

    func = t.get_func()
    func()

    func = another_test().func
    func()

    func = another_test.func2
    func()

    # wrong!!
    func = another_test.func
    func()