class Person:
    def __init__(self, person=None):
        if person:
            import copy
            # self is a local variable, change it can't change real instance.
            self = copy.deepcopy(person)
            print person.haha, '>>><<<<'
        else:
            self.haha = 'haha'

if __name__ == '__main__':
    p = Person()
    p2 = Person(p)
    print dir(p2)
    print p2.haha