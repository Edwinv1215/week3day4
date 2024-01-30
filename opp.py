#campany name is bigger pockets
#calculate property ROI
#customer calculator




def calculate_ROI(investments, rent, loss, expenses):
    # Calculate net profit and ROI
    net_profit = rent * 12 - loss - expenses
    return (net_profit / investments) * 100

def main():
    investments = 400000
    rent = 2000
    loss = 1500
    expenses = 5000

    while True:
        # Display the menu
        print("\nRental Property ROI Calculator")
        print("1. Calculate ROI")
        print("2. Update Investment Amount")
        print("3. Update Monthly Rent")
        print("4. Update Yearly Loss")
        print("5. Update Expenses")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            roi = calculate_ROI(investments, rent, loss, expenses)
            print(f"\nThe ROI for your rental property is {roi:.2f}%\n")

        if choice == '2':
            investments = float(input("Enter the new investment amount: "))

        if choice == '3':
            rent = float(input("Enter the new monthly rent: "))

        if choice == '4':
            loss = float(input("Enter the new yearly loss: "))

        if choice == '5':
            expenses = float(input("Enter the new expenses amount: "))

        if choice == '6':
            print("Exiting the program.")
            break

        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid choice. try again.")

if __name__ == "__main__":
    main()
