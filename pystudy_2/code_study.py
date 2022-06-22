a=float(input("삼각형의 하나의 변의 길이를 쓰시오"))
b=float(input("삼각형의 하나의 변의 길이를 쓰시오"))
c=float(input("삼각형의 하나의 변의 길이를 쓰시오"))
if a>b and a>c:
    if a<(b+c):
        print("상각형 성립가능")
    else:
        print("상각형 성립 불가능")
if b>a and b>c:
    if b<(a+c):
        print("상각형 성립가능")
    else:
        print("상각형 성립 불가능")
if c>b and c>a:
    if c<(b+a):
        print("상각형 성립가능")
    else:
        print("상각형 성립 불가능")


