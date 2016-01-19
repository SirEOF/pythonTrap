class PrivateClass(object):

    __p = 1
    p = 2

print PrivateClass.p
print PrivateClass._PrivateClass__p
print dir(PrivateClass)  # visible
