import csv
with open("people.csv", "w", newline='') as file:
    writer=csv.writer(file)
    writer.writerow(["Name", "Age"])
    for _ in range(2): # Loop to get input twice
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        writer.writerow([name, age])
print("Data saved to people.csv")
    
