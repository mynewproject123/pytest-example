import sys
from myapp.app import multiply_by_two, divide_by_two, square_number

def main():
    num = int(input("Insert a number: "))
    print("The double of %d is %d" % (num, multiply_by_two(num)))
    print("The half of %d is %d" % (num, divide_by_two(num)))
    print("The square of %d is %d" % (num, square_number(num)))  # New line for squaring
    sys.exit(0)

if __name__ == "__main__":
    main()
