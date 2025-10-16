#add import
from question_a import get_sum_of_evens


def main():
    while True:
        user_input = input("Enter a number (or 'q' to quit): ")
        
        if user_input.lower() == 'q':
            print("Goodbye!")
            break
        
        try:
            num = int(user_input)
            result = get_sum_of_evens(num)
            print(f"The sum of even numbers up to {num} is: {result}")
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")


if __name__ == "__main__":
    main()