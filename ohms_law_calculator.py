# Introduction
print("\033[93m\033[1m---------------------------OHM'S LAW CALCULATOR-----------------------------\033[0m")
print("- Calculation Types: Getting Voltage (V), Current (C), and Resistance (R)  -")
print("----------------------------------------------------------------------------")
print()


# Function to handle Ohm's Law calculations
def ohms_law_calculator():
    # Loop to keep the program running until the user chooses to exit
    while True:
        # Display the menu options for different calculations
        print("\033[93m\033[1mWhat do you want to calculate?\033[0m")
        print("\033[92m1. Voltage (V)\033[0m")  # Option to calculate voltage
        print("\033[94m2. Current (I)\033[0m")  # Option to calculate current
        print("\033[95m3. Resistance (R)\033[0m")  # Option to calculate resistance
        print("\033[31m4. Exit\033[0m")  # Option to exit the program
        print("-------------------------------------------------------------")

        # Get the user's choice of calculation
        choice = input("Enter the number of your choice: ")
        print("-------------------------------------------------------------")
        # Exit the program if the user selects '4'
        if choice == '4':
            print("End of program. Thank you.")
            break
        # Check if the user selected a valid option (1, 2, or 3)
        if choice in ['1', '2', '3']:
            # Loop to handle exceptions and ensure valid numerical input
            while True:
                try:
                    # Calculate voltage
                    if choice == '1':
                        print("Getting the Voltage...")
                        print()
                        # Ask for current (I) and resistance (R)
                        current = float(input("\033[94mEnter the current (I) in amperes: \033[0m"))
                        resistance = float(input("\033[95mEnter the resistance (R) in ohms: \033[0m"))
                        print("-------------------------------------------------------------")
                        # Calculate voltage using Ohm's Law
                        voltage = current * resistance
                        # Display the result
                        print(f"The \033[92mvoltage (V)\033[0m is \033[92m\033[4m{voltage} volts.\033[0m")
                        print("-------------------------------------------------------------")
                    # Calculate current
                    elif choice == '2':
                        print("Getting the Current...")
                        print()
                        # Ask for voltage (V) and resistance (R)
                        voltage = float(input("\033[92mEnter the voltage (V) in volts: \033[0m"))
                        resistance = float(input("\033[95mEnter the resistance (R) in ohms: \033[0m"))
                        print("-------------------------------------------------------------")
                        if resistance == 0:
                            print("\033[91mResistance cannot be zero.")
                            print("Enter the correct values below:\033[0m ")
                            print("-------------------------------------------------------------")
                            continue
                        # Calculate current using Ohm's Law
                        current = voltage / resistance
                        # Display the result
                        print(f"The \033[94mcurrent (I)\033[0m is \033[94m\033[4m{current} amperes.\033[0m")
                        print("-------------------------------------------------------------")
                    # Calculate resistance
                    elif choice == '3':
                        print("Getting the Resistance...")
                        print()
                        # Ask for voltage (V) and current (I)
                        voltage = float(input("\033[92mEnter the voltage (V) in volts: \033[0m"))
                        current = float(input("\033[94mEnter the current (I) in amperes: \033[0m"))
                        print("-------------------------------------------------------------")
                        if current == 0:
                            print("\033[91mCurrent cannot be zero.\033[0m")
                            print("-------------------------------------------------------------")
                            print("Enter the correct values below: ")
                            print()
                            continue
                        # Calculate resistance using Ohm's Law
                        resistance = voltage / current
                        # Display the result
                        print(f"The \033[95mresistance (R)\033[0m is \033[95m\033[4m{resistance} ohms.\033[0m")
                        print("-------------------------------------------------------------")
                    break
                except ValueError:
                    print("\033[91mInvalid input. Please enter numerical values.\033[0m")
                    print("-------------------------------------------------------------")
        else:
            print("\033[91mInvalid choice. Please select 1, 2, 3, or 4.\033[0m")
            print("-------------------------------------------------------------")

        # Ask if the user wants to perform another calculation
        another = input("Do you want to perform another calculation? (y/n): ").lower()
        print("-------------------------------------------------------------")
        print()
        # Exit the program if the user enters 'n'
        if another == 'n':
            print()
            print("-------------------------------------------------------------")
            print("End of program. Thank you.")
            break
        elif another != 'y':
            print("-------------------------------------------------------------")
            print("\033[91mInvalid input. Please enter only 'y' or 'n'.\033[0m")
            print()


# Run the calculator
ohms_law_calculator()
