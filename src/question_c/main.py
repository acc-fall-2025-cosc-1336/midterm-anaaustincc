#add import
from question_c import is_prime


def main():
    while True:
        user_input = input("Enter a number (or 'q' to quit): ")
        
        if user_input.lower() == 'q':
            print("Goodbye!")
            break
        
        try:
            num = int(user_input)
            if is_prime(num):
                print(f"{num} is a prime number.")
            else:
                print(f"{num} is not a prime number.")
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")


if __name__ == "__main__":
    main()
