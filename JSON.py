#json - javascript object notation.
#Convert from JSON to Python = If you have a JSON string, you can parse it by using the json.loads() method = result in python dictionary
import json
'''
# JSON string:
json_var =  '{ "EmpName":"Tom", "EmpAge":29, "EmpDesignation":"Senior Developer"}'
# parse result :
result = json.loads(json_var)
print(result)
print(type(result))
'''
#Convert from Python to JSON
#If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x,indent=4)

# the result is a JSON string:
print(y)


print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
