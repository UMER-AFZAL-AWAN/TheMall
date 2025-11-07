def somewrapper(func):
    def inner(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return inner

@somewrapper
def sample_function(x, y):
    return x + y

print(sample_function(5, 10))