try:
    num1,num2=eval(input("enter two numbers separated by comma: "))
    result=num1/num2
    print(f"the result is {result} ")
except ZeroDivisionError:
    print("Zero Division Error!")
except SyntaxError:
    print("comma is missing!")
except:
    print("wrong input!")
else:
    print("no exception")
finally:
    print("The code execution either way")
    