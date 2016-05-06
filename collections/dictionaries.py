# get values by keys
def print_dictionary(d):
    print("=====")
    print(d["key1"])
    try:
        print(d["key2"])
    except KeyError:
        print("Exception!")
    print(d.get("key2", "No such key in dictionary"))


dictionary = {"key1": "value1", 2: 2}
print_dictionary(dictionary)

# add keys
dictionary["key2"] = "value2"
print_dictionary(dictionary)
