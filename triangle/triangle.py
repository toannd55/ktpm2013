import math

e = 1e-09

def detect_triangle(a, b, c):
    if type(a) is float and type(b) is float and type(c) is float:
        if a > 0.0 and b > 0.0 and c > 0.0 and a < 2**32 and b < 2**32 and c < 2**32:
            if a+b > c and b+c > a and a+c > b and math.fabs(a-b) < c and math.fabs(b-c) < a and math.fabs(c-a) <b:
                if a==b and b==c:
                    return "Tam giac deu"
                elif (b==c and math.fabs(a*a - b*b - c*c) < e)\
                        or (a==c and math.fabs(b*b - a*a - c*c) < e)\
                        or (a==b and math.fabs(c*c - a*a - b*b) < e):
                    return "Tam giac vuong can"
                elif a==b or b==c or a==c:
                    return "Tam giac can"
                elif math.fabs(a*a - b*b - c*c) < e or math.fabs(b*b - a*a - c*c) < e or math.fabs(c*c - a*a - b*b) < e:
                    return "Tam giac vuong"
                else:
                    return "Tam giac thuong"
            else:
                return "Khong thoa man tam giac"
        else:
            return "Khong thuoc mien gia tri"
    else:
        return "Kieu du lieu sai"
