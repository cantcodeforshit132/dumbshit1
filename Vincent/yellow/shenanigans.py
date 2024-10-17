#made vincet
#date sept 16 2024
#function print hello world
try:
    print("hello this is a calculator to help you find the area of a triangle please input the required peraminters")
    base = float(input("enter base: "))
    height = float(input("enter height: "))
    answer = base*height/2
    print(f"the answer is {answer}")
except: print("numbers only ")