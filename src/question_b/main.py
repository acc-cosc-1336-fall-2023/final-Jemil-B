#add import
from question_b import Stock, get_stock_list

def display_stock_history(stock_list):
    for stock in stock_list:
        print(f"Company: {stock.get_company_name()}, Symbol: {stock.get_symbol()}")

def main():
    while True:
        stock_list = get_stock_list()

        print("Menu:")
        print("1. Display stock purchase history")
        print("2. Exit")

        option = input("Choose an option: ").strip()

        if option == "1":
            display_stock_history(stock_list)
        elif option == "2":
            print("Exiting program...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()