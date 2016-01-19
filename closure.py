def foo0():
    a = 1
    def bar():
          a = a +1
          return a
    return bar()

def foo1():
    a = 1
    def bar():
          x = a
          a = x + 1
          return a
    return bar()

def foo():
    a = [1]
    def bar():
          a[0] = a[0] + 1
          return a[0]
    return bar()

print foo()
print foo0()
print foo1()