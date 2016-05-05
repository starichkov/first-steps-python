try:
    num = 7 / 0
except ZeroDivisionError:
    print("Catch exact exception")
    raise  # rethrow exception
except (ValueError, TypeError):  # multi-catch
    print("Multi-catch block")
except:  # catch all possible exceptions
    print("Catch all block")
finally:
    print("Finally block")
