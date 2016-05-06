def function_varargs(*args):
    print(args)


def function_with_default_value(arg1, arg2="No value"):
    print("{}, {}".format(arg1, arg2))


def function_keyword_args(**kwargs):
    print(kwargs)


function_varargs(1, 2, 3, 4, 5)
function_with_default_value(1)
function_with_default_value(1, "Actual value")
function_keyword_args(a=1, b="B")
