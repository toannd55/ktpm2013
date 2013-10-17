#Output

import input
import math
import unittest
import itertools

doc = input.main.__doc__

#print doc

i=0
array = []
count = -1
leng = len(doc)
test = 0 #kiem tra xem du 2 dau cua lop tuong duong
a = 0
b = 0

while i<leng:
    temp = ''
    if doc[i] == '[':
        for j in range(i+1, leng):
            if doc[j] != ';':
                temp += doc[j]
            else:
                break
        a = int(temp)
        temp = ''
    if doc[i] == ';':
        for k in range(i+1, leng):
            if doc[k] != ']':
                temp += doc[k]
            else:
                break
        b = int(temp)
        temp = ''
        test = 1
    if test == 1:
        mid = (a+b)/2 #gia tri trung binh cua moi khoang
        #array[count].append(a)
        #array[count].append(a-1)
        #array[count].append(b)
        #array[count].append(b+1)
        array[count].append(mid)
        test = 0
    if doc[i] == ':':
        array.append([])
        count += 1
    i += 1

#print array

#x = float('1.0')
#print x

class autoTest(unittest.TestCase):
    def __init__(self, *args):
        super(autoTest, self).__init__()
        self.args = args
    def runTest(self):
        self.assertEqual(input.main(*self.args), 1)
    
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(autoTest(*i) for i in itertools.product(*array))
    unittest.TextTestRunner().run(suite)
