import unittest
import math
import triangle

class test(unittest.TestCase):
        
    #test tam giac deu
    def test_triangleDeu1(self):
        self.assertEquals(triangle.detect_triangle(1.0, 1.0, 1.0), "Tam giac deu")
    def test_triangleDeu2(self):
        self.assertEquals(triangle.detect_triangle(2**32.0-1, 2**32.0-1, 2**32.0-1), "Tam giac deu")
    def test_triangleDeu3(self):
        self.assertEquals(triangle.detect_triangle(0.00000000001, 0.00000000001, 0.00000000001), "Tam giac deu")

    #test tam giac vuong can
    def test_triangleVuongCan(self):
        self.assertEquals(triangle.detect_triangle(1.0, 1.0, math.sqrt(2.0)), "Tam giac vuong can")
    def test_triangleVuongCan2(self):
        self.assertEquals(triangle.detect_triangle(1.0, math.sqrt(2.0), 1.0), "Tam giac vuong can")
    def test_triangleVuongCan3(self):
        self.assertEquals(triangle.detect_triangle (math.sqrt(2.0), 1.0, 1.0), "Tam giac vuong can")

    #test tam giac vuong
    def test_triangleVuong(self):
        self.assertEquals(triangle.detect_triangle(5.0, 3.0, 4.0), "Tam giac vuong")
    def test_triangleVuong2(self):
        self.assertEquals(triangle.detect_triangle(4.0, 5.0, 3.0), "Tam giac vuong")
    def test_triangleVuong3(self):
        self.assertEquals(triangle.detect_triangle(3.0, 4.0, 5.0), "Tam giac vuong")
    def test_triangleVuong4(self):
        self.assertEquals(triangle.detect_triangle(math.sqrt(2.0), math.sqrt(1.0), math.sqrt(3.0)), "Tam giac vuong")

    #test tam giac can
    def test_triangleCan(self):
        self.assertEquals(triangle.detect_triangle(1.0, 3.0, 3.0), "Tam giac can")
    def test_triangleCan2(self):
        self.assertEquals(triangle.detect_triangle(3.0, 1.0, 3.0), "Tam giac can")
    def test_triangleCan3(self):
        self.assertEquals(triangle.detect_triangle(3.0, 3.0, 1.0), "Tam giac can")
    def test_triangleCan4(self):
        self.assertEquals(triangle.detect_triangle(2**31.0, 2**31.0, 0.0001), "Tam giac can")
    def test_triangleCan5(self):
        self.assertEquals(triangle.detect_triangle(2**32.0-1, 1.0, 2**32.0-1), "Tam giac can")

    #test tam giac thuong
    def test_triangleThuong(self):
        self.assertEquals(triangle.detect_triangle(2.0, 4.0, 3.0), "Tam giac thuong")
    def test_triangleThuong2(self):
        self.assertEquals(triangle.detect_triangle(2**32.0-1, 4.0, 2**32.0-2), "Tam giac thuong")
    def test_triangleThuong3(self):
        self.assertEquals(triangle.detect_triangle(0.0001, 0.00012, 0.00011), "Tam giac thuong")
    def test_triangleThuong4(self):
        self.assertEquals(triangle.detect_triangle(2**32.0-1, 2**32.0-1.1, 2**32.0-2), "Tam giac thuong")    

    #test khong phai tam giac
    def test_KhongPhaitriangle(self):
        self.assertEquals(triangle.detect_triangle(1.0, 1.0, 3.0), "Khong thoa man tam giac")
    def test_KhongPhaitriangle2(self):
        self.assertEquals(triangle.detect_triangle(1.0, 3.0, 1.0), "Khong thoa man tam giac")
    def test_KhongPhaitriangle3(self):
        self.assertEquals(triangle.detect_triangle(3.0, 1.0, 1.0), "Khong thoa man tam giac")
    def test_KhongPhaitriangle4(self):
        self.assertEquals(triangle.detect_triangle(2**32.0-1, 1.0, 3.0), "Khong thoa man tam giac")

    #test ngoai mien gia tri
    def test_MienGiaTri(self):
        self.assertEquals(triangle.detect_triangle(-1.0, 1.0, 1.0), "Khong thuoc mien gia tri")
    def test_MienGiaTri2(self):
        self.assertEquals(triangle.detect_triangle(-1.0, -1.0, -1.0), "Khong thuoc mien gia tri")    
    def test_MienGiaTri3(self):
        self.assertEquals(triangle.detect_triangle(2**32.0, 1.0, -1.0), "Khong thuoc mien gia tri")
    def test_MienGiaTri4(self):
        self.assertEquals(triangle.detect_triangle(2**32.0, 2**32.0, 2**32.0), "Khong thuoc mien gia tri")    

    #test sai kieu gia tri dau vao Float
    def test_KieuGiaTri(self):
        self.assertEquals(triangle.detect_triangle('a', 'b', 'c'), "Kieu du lieu sai")
    def test_KieuGiaTri2(self):
        self.assertEquals(triangle.detect_triangle('a', 'b', 5), "Kieu du lieu sai")
    def test_KieuGiaTri3(self):
        self.assertEquals(triangle.detect_triangle(1.0, 'b', 'c'), "Kieu du lieu sai")    


if __name__ == '__main__':
    unittest.main()
