
def foo():
    a = 1
    b = 0
    if b == 0:
        raise ZeroDivisionError("b is zero")

    try:
        # number = input()
        # if str(number).isalpha():
        #     raise ZeroDivisionError()
        # raise AccountDoesNotExistError()
        int("a")  # 1
    except ZeroDivisionError as e:
        print("divide by zero " + str(e))
    except Exception as e:
        print("********** unknown error " + str(e))
    finally:
        print("will always happen")  # 4

try:
    print("************** set_more.py *****************")
    file = open("set_more.py", "r")
    file_content = file.read()
    print(file_content)
except Exception as e:
    print("File access error.")
finally:
    file.close()

# ===========================================
# with in python executes try-finally(close)
    with open("set_more.py", "r") as file:
        file_content = file.read()
        print(file_content)
# ===========================================
try:
    file = open("set_more.py", "r")
    file_content = file.read()
    print(file_content)
finally:
    file.close()
# ===========================================
