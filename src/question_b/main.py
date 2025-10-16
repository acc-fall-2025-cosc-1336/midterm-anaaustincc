#add import
from question_b import get_fahrenheit


def main():
    print("Celsius to Fahrenheit Conversion Table")
    print("=" * 40)
    print(f"{'Celsius':<15}{'Fahrenheit':<15}")
    print("-" * 40)
    
    for celsius in range(0, 21):
        fahrenheit = get_fahrenheit(celsius)
        print(f"{celsius:<15}{fahrenheit:<15.2f}")


if __name__ == "__main__":
    main()
