import sys
if len(sys.argv) <2:
    print("Usage: python sample.py <arg1> <arg2> ...")
    sys.exit()
num=[int(arg) for arg in sys.argv[1:]]
total=sum(num)
print("Number:", num)
print("Sum of arguments:", total)

