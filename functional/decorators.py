def printer_decorator(print_func):
    def wrap():
        print("Wrapper begin")
        print_func()
        print("Wrapper end")

    return wrap


def print_text():
    print("Text")


p = printer_decorator(print_text)
p()


@printer_decorator
def print_text():
    print("Text")


print_text()
