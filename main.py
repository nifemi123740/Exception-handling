try:
    number=int(input("enter a number: "))
    print(f"the number  entered is {number} ")
except ValueError as ex:
    print(f"Exception: {ex}")