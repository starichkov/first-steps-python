from random import randint as rai


def function_0():
    print("Function 0")


def function_1(arg):
    print("Function 1: " + arg)


def function_2(arg1, arg2):
    print("Function 2: " + arg1 + ", " + arg2)


def function_v(var):
    var += 1
    print(var)


# this is simple comment
def function_max(x, y):
    """
    And this is a documentary string!
    """
    assert x != y  # simple assert
    assert x != y, "X != Y"  # assert with message
    if x > y:
        return x
    elif y > x:
        return y
    else:
        raise ValueError("X and Y are equal!")


def function_pow(arg):
    return arg ** 2


def function_multi_max(fmax, fpow, x, y):
    print("Function Multi Max values: " + str(x) + ", " + str(y))
    return fmax(fpow(x), fpow(y))


function_0()
function_1("Foo, bar!")
function_2("Foo", "bar")
function_v(1)
get_max = function_max
get_powed_max = function_multi_max
print("Max is: " + str(get_max(1, 2)))
print("Powed max is: " + str(get_powed_max(get_max, function_pow, rai(1, 10), rai(1, 10))))
