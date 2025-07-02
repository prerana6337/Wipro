#json module
import json
name=input("Enter your name:")
age=int(input("Enter your age:"))
data={"name":name,"age":age}
stringifyed_data=json.dumps(data)
print("Stringified data:", stringifyed_data)
