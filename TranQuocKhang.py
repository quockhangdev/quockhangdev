"""
    MSSV: B1913236
    Ho va ten: Tran Quoc Khang
    Lab 1, Ly thuyet thong tin
"""

def Cau1():
    yourName = input("Nhap ten cua ban: ")
    print("Hello" + yourName + ", Welcome to Python")

def Cau2():
    n = int(input("Nhap so nguyen n: "))
    while n < 0:
        print("Nhap lai so nguyen n: ")
        n = int(input())
    while n > 10:
        print("Nhap lai so nguyen n: ")
        n = int(input())
    print(n + n** 2 + n**3 + n**4)

def Cau3():
    a, b = map(int, input("Nhap 2 so nguyen a, b: ").split())
    while b == 0:
        print("Nhap lai so nguyen b: ")
        b = int(input())
    print("a + b = ", a + b)
    print("a - b = ", a - b)
    print("a * b = ", a * b)
    print("a / b = ", a / b)
    print("a // b = ", a // b)
    print("a % b = ", a % b)
    print("a ** b = ", a ** b)

def Cau4():
    r = float(input("Nhap ban kinh r: "))
    while r < 0:
        print("Nhap lai ban kinh r: ")
        r = float(input())
    print("Chu vi hinh tron la: ", 2 * 3.14 * r)
    print("Dien tich hinh tron la: ", 3.14 * r**2)

def Cau5():
    n = int(input("Nhap so nguyen n: "))
    while n < 0:
        print("Nhap lai so nguyen n: ")
        n = int(input())
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    print("Giai thua cua n la: ", factorial)

def Cau6():
    a, b, c = map(int, input("Nhap 3 so nguyen a, b, c: ").split())
    # a^2x + bx + c = 0
    delta = b**2 - 4 * a * c
    if delta < 0:
        print("Phuong trinh vo nghiem")
    elif delta == 0:
        print("Phuong trinh co nghiem kep x1 = x2 = ", -b / (2 * a))
    else:
        print("Phuong trinh co 2 nghiem phan biet: ")
        print("x1 = ", (-b + delta**0.5) / (2 * a))
        print("x2 = ", (-b - delta**0.5) / (2 * a))

def Cau7():
    for i in range(5000, 7000):
        if i % 7 == 0 and i % 5 != 0:
            print(i, end=" ")
    print()

def Cau8():
    n = int(input("Nhap so nguyen n: "))
    print(bin(n))

def Cau9():
    a, b = map(int, input("Nhap 2 so nguyen a, b: ").split())
    print("Uoc chung lon nhat cua a va b la: ", end="")
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    print(a)
    print("Boi chung nho nhat cua a va b la: ", end="")
    print(int(a * b / a))
    print()

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def Cau10():
    n = int(input("Nhap so nguyen n: "))

    for i in range(2, n):
        if isPrime(i):
            print(i, end=" ")
    print()

def Cau11():
    for i in range(1000, 10000):
        if isPrime(i):
            print(i, end=" ")
    print()

def Cau12():
    n = int(input("Nhap so nguyen n: "))
    while n < 0:
        print("Nhap lai so nguyen n: ")
        n = int(input())
    n = str(n)
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    print("Tong cac chu so cua n la: ", sum)

def Cau13():

    def isOddNumber(n):
        n = str(n)
        for i in range(len(n)):
            if int(n[i]) % 2 == 0:
                return False
        return True

    for i in range(1000, 2000):
        if isOddNumber(i):
            print(i, end=" ")

def Cau14():
    n = int(input("Nhap so nguyen n: "))
    while n < 0:
        print("Nhap lai so nguyen n: ")
        n = int(input())
    sum = 0
    for i in range(1, n + 1):
        sum += i / (i + 1)
    print("Tong cua day so la: ", sum)

import math
from typing import List

class Cau15():
    def calc_entropy(self, p: List[float]):
        entropy = 0
        for i in range(len(p)):
            entropy += (p[i] * math.log2(p[i]) if p[i] != 0 else 0)
        return -entropy

class Cau16():
    """
        Cho bộ bài tú lơ khơ 52 lá và 1 đồng xu đồng chát. Lấy từ bộ bài ra 4 quân K và 4 quân Át để chơi một trò chơi như sau:
        
        * Úp cả 8 quân bài xuống và lần lượt rút ra 2 lá bài và lật lên xem. 
        Nếu lá thứ nhất và lá thứ 2 cùng chất (cơ, rô, chuồn, bích) thì tung đồng xu 2 lần và đếm số đầu hình xuất hiện. 
        Nếu không cùng chất thì tung đồng xu 3 lần.

        * Tính lượng tin về 2 lá bài rút được (có cùng chất hay không) khi biết thông tin về số đầu hình thu được.
    """

    """

        X = {cùng chất, không cùng chất}
        P(X = không cùng chất) = 8/8 * 6/7 = 6/7
        P(X = cùng chất) = (2/8 * 1/7) * 4 = 1/7

        Y = {0 đầu, 1 đầu, 2 đầu, 3 đầu}
        P(X = không cùng chất, Y = 0 đầu) = 1/2 * 1/2 * 1/2 = 1/8
        P(X = không cùng chất, Y = 1 đầu) = (1/2 * 1/2 * 1/2) * 3 = 3/8
        P(X = không cùng chất, Y = 2 đầu) = (1/2 * 1/2 * 1/2) * 3 = 3/8
        P(X = không cùng chất, Y = 3 đầu) = 1/2 * 1/2 * 1/2 = 1/8

        P(X = cùng chất, Y = 0 đầu) = 1/2 * 1/2 = 1/4
        P(X = cùng chất, Y = 1 đầu) = (1/2 * 1/2) * 2 = 1/2
        P(X = cùng chất, Y = 2 đầu) = 1/2 * 1/2 = 1/4
        P(X = cùng chất, Y = 3 đầu) = 0

        P(Y = 0 đầu) = 1/8 * 6/7 + 1/4 * 1/7 = 1/7
        P(Y = 1 đầu) = 3/8 * 6/7 + 1/2 * 1/7 = 3/7
        P(Y = 2 đầu) = 3/8 * 6/7 + 1/4 * 1/7 = 1/7
        P(Y = 3 đầu) = 1/8 * 6/7 + 0 * 1/7 = 6/7

        H(X)    = -P(X = không cùng chất) * log2(P(X = không cùng chất)) - P(X = cùng chất) * log2(P(X = cùng chất)) 
        H(X)    = -[6/7 * log2(6/7) + 1/7 * log2(1/7)] = 0.5916727785823275

        H(Y)    = -P(Y = 0 đầu) * log2(P(Y = 0 đầu)) 
                - P(Y = 1 đầu) * log2(P(Y = 1 đầu)) 
                - P(Y = 2 đầu) * log2(P(Y = 2 đầu)) 
                - P(Y = 3 đầu) * log2(P(Y = 3 đầu))
        H(Y)    = -[1/7 * log2(1/7) + 3/7 * log2(3/7) + 1/7 * log2(1/7) + 6/7 * log2(6/7)] = 1.51660594802

        H(Y | X = không cùng chất) = -P(Y = 0 đầu | X = không cùng chất) * log2(P(Y = 0 đầu | X = không cùng chất))
                                    - P(Y = 1 đầu | X = không cùng chất) * log2(P(Y = 1 đầu | X = không cùng chất))
                                    - P(Y = 2 đầu | X = không cùng chất) * log2(P(Y = 2 đầu | X = không cùng chất))
                                    - P(Y = 3 đầu | X = không cùng chất) * log2(P(Y = 3 đầu | X = không cùng chất))
        H(Y | X = không cùng chất) = -[1/8 * log2(1/8) + 3/8 * log2(3/8) + 3/8 * log2(3/8) + 1/8 * log2(1/8)] = 1.81127812446

        * Define: log2(0) = 0
        
        H(Y | X = cùng chất) = -P(Y = 0 đầu | X = cùng chất) * log2(P(Y = 0 đầu | X = cùng chất))
                                 - P(Y = 1 đầu | X = cùng chất) * log2(P(Y = 1 đầu | X = cùng chất))
                                    - P(Y = 2 đầu | X = cùng chất) * log2(P(Y = 2 đầu | X = cùng chất)) 
                                    - P(Y = 3 đầu | X = cùng chất) * log2(P(Y = 3 đầu | X = cùng chất))
        H(Y | X = cùng chất) = -[1/4 * log2(1/4) + 1/2 * log2(1/2) + 1/4 * log2(1/4) + 0 * log2(0)] = 1.5

        H(Y, X) = P(X = không cùng chất) * H(Y | X = không cùng chất) + P(X = cùng chất) * H(Y | X = cùng chất)
        H(Y, X) = 6 / 7 * 1.811278124459133 + 1/7 * 1.5 = 1.76680982096

        H(X | Y) = H(Y, X) - H(Y)
        H(X | Y) = 1.76680982096 - 1.51660594802 = 0.25020387294

        I(X | Y) = H(X) - H(X | Y)
        I(X | Y) = 0.5916727785823275 - 0.25020387294 = 0.34146890564

    """

    def __init__(self):
        self.X = {
            "cùng chất": 1/7,
            "không cùng chất": 6/7
        }

        self.Y = {
            "0 đầu": 1/7,
            "1 đầu": 3/7,
            "2 đầu": 1/7,
            "3 đầu": 6/7
        }

        self.X_Y = {
            "cùng chất": {
                "0 đầu": 1/4,
                "1 đầu": 1/2,
                "2 đầu": 1/4,
                "3 đầu": 0
            },
            "không cùng chất": {
                "0 đầu": 1/8,
                "1 đầu": 3/8,
                "2 đầu": 3/8,
                "3 đầu": 1/8
            }
        }

    def solve(self):
        H_X = Cau15().calc_entropy([x for x in self.X.values()])
        H_Y = Cau15().calc_entropy([y for y in self.Y.values()])
        print("H(X) \t\t= {}".format(H_X))
        print("H(Y) \t\t= {}".format(H_Y))

        H_X_Y = self.X["không cùng chất"] * Cau15().calc_entropy([x_y for x_y in self.X_Y["không cùng chất"].values()]) + \
                self.X["cùng chất"] * Cau15().calc_entropy([x_y for x_y in self.X_Y["cùng chất"].values()])
        print("H(X, Y) \t= {}".format(H_X_Y))

        H_X_Y = H_X_Y - H_Y
        print("H(X | Y) \t= {}".format(H_X_Y))

        I_X_Y = H_X - H_X_Y
        print("I(X | Y) \t= {}".format(I_X_Y))

if __name__ == "__main__":
    Cau16().solve()