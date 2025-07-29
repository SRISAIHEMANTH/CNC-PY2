# calculator.py

import argparse

def main():
    parser = argparse.ArgumentParser(description="Basic CLI Calculator")
    parser.add_argument("num1", type=float, help="First number")
    parser.add_argument("operation", choices=["add", "sub", "mul", "div"], help="Operation to perform")
    parser.add_argument("num2", type=float, help="Second number")

    args = parser.parse_args()

    if args.operation == "add":
        result = args.num1 + args.num2
    elif args.operation == "sub":
        result = args.num1 - args.num2
    elif args.operation == "mul":
        result = args.num1 * args.num2
    elif args.operation == "div":
        if args.num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = args.num1 / args.num2

    print("Result:", result)

if __name__ == "__main__":
    main()
