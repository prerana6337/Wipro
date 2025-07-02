import json
name=input("Enter your name:")
age=int(input("Enter your age:"))
user={"name":name,"age":age}

with open ('user.json', "w") as file:
    json.dump(user, file)
print("User data saved to user.json")
with open("user.json", "r") as file:
    loaded=json.load(file)
print("Loaded user data:", loaded)