from question_a import create_multiplication_table, display_multiplication_table

def main():
    while True:
        table = create_multiplication_table()
        display_multiplication_table(table)
        continue_choice = input("Do you want to display the table again? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()