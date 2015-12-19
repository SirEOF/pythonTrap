# New Style Classes
class NA(object):
    pass

class NB(NA):
    pass

class NC(NB, NA):
    pass

# Old Style Classes
class OA:
    pass

class OB(OA):
    pass

class OC(OB, OA):
    pass

if __name__ == '__main__':
    na = NA()
    nb = NB()
    nc = NC()
    oa = OA()
    ob = OB()
    oc = OC()

    print 'isinstance(na, NA)', isinstance(na, NA)
    print 'isinstance(nb, NA)', isinstance(nb, NA)
    print 'isinstance(nc, NA)', isinstance(nc, NA)
    print 'isinstance(oa, OA)', isinstance(oa, OA)
    print 'isinstance(ob, OA)', isinstance(ob, OA)
    print 'isinstance(oc, OA)', isinstance(oc, OA)
    print 'isinstance(NB, NA)', isinstance(NB, NA)
    print 'isinstance(OB, OA)', isinstance(OB, OA)
