# def deco(func):
#     def wrapper(*args):
#         result = []
#         for i in args:
#             if i > 0:
#                 result.append(i)
#             else:
#                 result.append(False)
#         func(result)
#     return wrapper
#
# @deco
# def salom(a):
#     print(a)
#
# salom(-2, 4, 9, -1)



users = ['shaxriyor6', 'javohir456', "fefe2342", "fewfs"]

def deco(func):
    def wrapper(username):
        if username in users:
            func(username)
        else:
            print("Username not found")
    return wrapper


@deco
def funk(username):
    print("Hello " + username)


funk("shaxriyor61")