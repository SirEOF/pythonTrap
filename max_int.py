x = 1
for i in range(512):
    x = int(x << 1)
    print x

print '---------'

import sys
print sys.maxint

# long 精度无上限
print type(x)