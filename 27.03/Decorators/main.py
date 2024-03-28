def custom_decorator(func):
    def wrapper(a):
        print("Before")
        val = func(a)
        print("After")
        return val

    return wrapper


@custom_decorator
def func(a: int):
    print("Inside")
    return a**2


print(func(5))
