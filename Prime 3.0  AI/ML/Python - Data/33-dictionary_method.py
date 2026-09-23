info = {
    "Name" : "Rahul",
    "Subjects" :["Maths","English","Python","Dsa","Java"] ,
    "Marks" : [94,95,90,87,98],
    "Cgpa" : 9.5
}
# info["Cgpa"] = 9.6
# print(info)
# print(info["Marks"])
# print(type(info))

# print(info.keys())
# print(info.values())
# print(info.items())
# print(info.get("Name"))
# print(info.get("Namme"))

info.update({
    "City" : "New York"
})
print(info)