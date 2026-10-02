import json

# json_str =  '{ "Name" : "Rahul", "isTeacher" : false}'

# obj_py = json.loads(json_str)

# obj_py =  {
#     "Name" : "Rahul", 
#     "isTeacher" : False , 
#     "Age" : None
#     }

# json_str = json.dumps(obj_py)

# print(type(json_str), json_str)

# json load

# with open("data.json", "r") as f:
#     obj_py = json.load(f)
#     print(type(obj_py), obj_py)

# json dump

d = {
    "Name" : "Rahul",
    "Isteacher" : False,
    "Age" : None
}
with open("data.json", "w") as f:
    json.dump(d , f , indent = 4 , sort_keys = True)
    