class F:
    x = []
    @classmethod
    def add(cls, x):
        cls.x.append(x)

class C(F):
    # x = []
    pass

if __name__ == '__main__':
    i = C
    i.add(1)
    print F.x