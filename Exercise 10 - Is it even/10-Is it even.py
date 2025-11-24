# DEFINE FUNCTION 1: 'odd_or_even' checks if a number 'n' is even (remainder of n/2 is 0) or odd, and prints the result.    
def odd_or_even(n):
   # Check if 'n' is even.
    if n % 2 == 0:
        print(f"even")
    # Otherwise, it's odd.
    else:
        print(f"odd") 
# DEFINE FUNCTION 2: 'main' gets a number from the user.
def main():
    number = int(input("Input any number:"))
    # It calls the first function to check and print the result.
    odd_or_even (number)

# Run the entire process.
main()