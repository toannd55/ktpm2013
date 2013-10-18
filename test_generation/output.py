#Output

import input
import math
import unittest
import itertools
import re

doc = input.main.__doc__

print doc

i=0
array = [] #luu cac gia tri kiem thu bien
arr = [] #luu cac bien de kiem tra lop tuong duong
count = -1
leng = len(doc)
test = 0 #kiem tra xem du 2 dau cua lop tuong duong
check = True
a = 0
b = 0
ix=0
iy=0

#luu du lieu input vao 2 mang
while i<leng:
    temp = ''
    if doc[i] == '[':
        for j in range(i+1, leng):
            if doc[j] != ';':
                temp += doc[j]
            else:
                break
        a = int(temp)
        arr[count].append(a)
        temp = ''
    if doc[i] == ';':
        for k in range(i+1, leng):
            if doc[k] != ']':
                temp += doc[k]
            else:
                break
        b = int(temp)
        arr[count].append(b)
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
        arr.append([])
        count += 1
    i += 1

#Sap xep theo dau mut trai cua tung khoang de kiem tra t/m lop tuong duong k?    
for arr2 in arr:
    for ix in xrange(0, len(arr2)):
        if ix%2==0:
            for iy in xrange(ix+2, len(arr2)):
                if iy%2==0:
                    if arr2[ix] > arr2[iy]:
                        numx = arr2[ix]
                        numy = arr2[ix+1]
                        arr2[ix] = arr2[iy]
                        arr2[ix+1] = arr2[iy+1]
                        arr2[iy] = numx
                        arr2[iy+1] = numy

#kiem tra lop tuong duong
for arr2 in arr:
    for ix in xrange(1, len(arr2)-1):
        if ix%2==1:
            if arr2[ix] >= arr2[ix+1]:
                check = False
                break


class autoTest(unittest.TestCase):
    def __init__(self, *args):
        super(autoTest, self).__init__()
        self.args = args
    def runTest(self):
        self.assertEqual(input.main(*self.args), 1)
    
if __name__ == '__main__':
    if(check == True):
        suite = unittest.TestSuite()
        suite.addTests(autoTest(*i) for i in itertools.product(*array))
        unittest.TextTestRunner().run(suite)
    else:
        print "wrong input"
