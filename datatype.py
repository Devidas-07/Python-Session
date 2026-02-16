"""datatype"""
num = 34
print(type(num))
list_datatype = [23,"hetero",8.8]
print(type(list_datatype))
tuple_datatype = (43, 56, "hellotuple")
print(tuple_datatype)
set_datatype = set(["acb", "pqr"])

##print(set_datatype)
for value in set_datatype:
    print(value, end=" first ")

dictionary_datatype = {"anagar":"nagar", "pune": "pcmc"}
print(dictionary_datatype)
for key, value in dictionary_datatype.items():
    print(f"key is {key}")
    print(f"value is {value}")