import sys
if len(sys.argv) != 3:
    print("Usage: python area.py <length> <width>")
else:
    l=float(sys.argv[1])
    w=float(sys.argv[2])    
    area = l * w
    print("Area of rectangle:", area)