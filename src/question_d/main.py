from question_d import get_assessment_value, get_tax_assessed


def main():
	while True:
		user_input = input("Enter the actual value of the property (or 'q' to quit): ")
		if user_input.lower() == 'q':
			print("Goodbye!")
			break
		try:
			actual_value = float(user_input)
			assessment_value = get_assessment_value(actual_value)
			tax = get_tax_assessed(assessment_value)
			print(f"Assessment value: ${assessment_value:,.2f}")
			print(f"Property tax: ${tax:,.2f}")
		except ValueError:
			print("Invalid input. Please enter a numeric value or 'q' to quit.")


if __name__ == "__main__":
	main()