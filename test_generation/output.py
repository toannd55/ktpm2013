#Ho va ten: Nguyen Duc Toan
#MSSV: 10020361
#output.py

import input
import math
import unittest
import itertools
import re

doc = input.main.__doc__

i=0
array = [] #luu cac gia tri kiem thu bien
arr = [] #luu cac bien de kiem tra lop tuong duong
count = -1
leng = len(doc)
test = 0 #kiem tra xem du 2 dau cua lop tuong duong
a = 0
b = 0
ix=0
iy=0

#luu du lieu input vao 2 mang
try:
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
        for ix in xrange(0, len(arr2)-1):
            if ix%2==1:
                if arr2[ix] >= arr2[ix+1]:
                    raise Exception("wrong input")
                    break
            if ix%2==0:
                if arr2[ix] >= arr2[ix+1]:
                    raise Exception("wrong input")
                    break

    class autoTest(unittest.TestCase):
        pass
    def testCase(*args):
        def test(self):
            self.assertEqual(input.main(*args),0)
        return test
		
    if __name__ == '__main__':
        for element in itertools.product(*array):
            name = 'test_' + str(element)
            test = testCase(*element)
            setattr(autoTest, name, test)
        unittest.main()
except Exception as ex:
    print "wrong input"
