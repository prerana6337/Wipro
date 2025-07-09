import argparse
parser=argparse.ArgumentParser(description="Add two numbers")
parser.add_argument("--x",type=int,required=True,help="First number:")
parser.add_argument("--y",type=int,required=True,help="Second number:")
parser.add_argument("--opt",type=str,required=True,choices=['add','sub','mul','div'],help="Operation")
args=parser.parse_args()
if args.opt == 'add':
    result = args.x + args.y
elif args.opt == 'sub':
    result = args.x - args.y    
elif args.opt == 'mul':
    result = args.x * args.y
elif args.opt == 'div':
    if args.y == 0:
        print("Error: Division by zero is not allowed.")
        exit(1)
    result = args.x / args.y
print("Result:", result)

'''import argparse
parser = argparse.ArgumentParser(description="Add two numbers")
parser.add_argument("--x", type=int, required=True, help="First number")
parser.add_argument("--y", type=int, required=True, help="Second number")
parser.add_argument("--opt", type=str, required=True, choices=['add', 'sub', 'mul', 'div'], help="Operation")  # Fixed 'choice' to 'choices'
args = parser.parse_args()

if args.opt == 'add':
    result = args.x + args.y
elif args.opt == 'sub':
    result = args.x - args.y
elif args.opt == 'mul':
    result = args.x * args.y
elif args.opt == 'div':
    if args.y == 0:
        print("Error: Division by zero is not allowed.")
        exit(1)
    result = args.x / args.y'''