#1
def deco(func):
    def wrapper(number):
        if isinstance(number, (int, float)):
            result = 2*number
            func(result)
        else:
            print("Not a number")
    return wrapper

@deco
def funk(a):
    print(a)

funk(4)
funk("w")


#2
def deco(func):
    def wrapper(username):
        if isinstance(username, str):
            text = f"Welcome {username}"
            func(text)
        else:
            print("Not a username")
    return wrapper

@deco
def funk(a):
    print(a)

funk("sdadsa")


#3
def deco(func):
    def wrapper(*args):
        lst = args
        is_negative = False
        i = 0
        while is_negative == False and i < len(lst):
            if lst[i] < 0:
                is_negative = True
            i += 1
        if is_negative == True:
            print("Negative number found")
        else:
            func(lst)


    return wrapper

@deco
def funk(a):
    print(a)

funk(2, 4, 9, 1)


#4
def deco(func):
    def wrapper(number):
        if isinstance(number, (int, float)):
            if number <10:
                 func()
            else:
                print("wrong number")
        else:
            print("not a number")
    return wrapper


@deco
def funk():
    print("accepted")

funk(10)


#5
def deco(func):
    def wrapper(radius):
        if isinstance(radius, (int, float)):
            if radius >= 0:
                result = 3.14 * (radius ** 2)
                func(result)
            else:
                print("wrong radius")
        else:
            print("not a number")

    return wrapper


@deco
def funk(Area):
    print(Area)


funk(1)


#6
def deco(func):
    def wrapper(username):
        if not isinstance(username, str):
            print("not a username")
            return
        if len(username) < 5:
            print("username is too short")
            return

        if not any(str(digit) in username for digit in range(10)):
            print("username should have a number in it")
            return

        func(username)
    return wrapper

@deco
def funk(a):
    print(a)

funk("ssadxcz1xs")


#7
import string
alphabet = list(string.ascii_lowercase)

def deco(func):
    def wrapper(args):
        result = []
        for i in range(alphabet.index(args[0])+1, alphabet.index(args[1])):
            result.append(alphabet[i])
        func(result)
    return wrapper

@deco
def funk(a):
    print(a)

funk(["d", "z"])

#8
def deco(func):
    def wrapper(filename):
        try:
            with open(filename, "r") as f:
                lines = f.readlines()
                for line in lines:
                    print(line)
        except FileNotFoundError:
            print("File not found")
        else:
            func(filename)
    return wrapper


@deco
def funk(filename):
    print("done")

funk("example.txt")


#9
def temple_strings(obj, feature): return f"{obj} are {feature}"

#10
def repeat_str(repeat, string):  return ''.join(string for i in range(repeat) if repeat > 0)

#11
def get_drink_by_profession(param):
    my_dict = {
        "Jabroni": "Patron Tequila",
        "School Counselor": "Anything with Alcohol",
        "Programmer": "Hipster Craft Beer",
        "Bike Gang Member": "Moonshine",
        "Politician": "Your tax dollars",
        "Rapper": "Cristal"
    }
    return my_dict.get(param.title(), "Beer")