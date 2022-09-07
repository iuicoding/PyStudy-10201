while True:
string_input = input("정수 입력>")
if string_input.isdigit():
    number_input_a = int(string_input)
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2*3.14*number_input_a)
    print("원의 넓이:", 3.14*number_input_a * number_input_a)
else:
    print("정수를 입력해주세요!")


while True:
    try:
        print(float(input(">숫자를 입력해주세요:"))**2)
        break
    except:
        print("숫자를 입력해주새요")


while True:
    try:
        print(float(input(">숫자를 입력해주세요:"))**2)
        break
    except:
        pass


list_input_a = =["52", "273", "32", "스파이", "103"]
list_number=[]
for item in list_input_a:
    try:
        float(item)
        list_number.append(item)
    except:
        pass

print("{} 내부에 있는 숫자는".format(list_input_a))
print("{}입니다.".format(list_number))

number = [52, 273, 32, 103, 90, 10, 275]
print("요소 냐부에 없는 값 찾기")
number=10000

if number in numbers:
    print("-{}는 {} 위치에 있습니다.".format(number, numbers.index(number)))
else
    print("리스트 냐부에 없는 값입니다.)print()