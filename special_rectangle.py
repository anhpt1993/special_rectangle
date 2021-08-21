# special rectangle

def input_data():
    while True:
        try:
            num = int(input())
            if num > 0:
                return num
                break
            else:
                print("Enter a positive integer. Try again")
                print()
        except Exception:
            print("Input value shall be an integer, not a decimal or string")
            print()

def rectangle(length, width):
    for i in range(length):
        if i == 0 or i == length - 1:
            print("*" * width)
        else:
            print("{}{}{}".format("*"," " * (width-2),"*"))

print("Enter length of rectangle: ")
length = input_data()
print("Enter width of rectangle: ")
width = input_data()
rectangle(min(length,width),max(length,width))