from operations import add,subtract,multiply,divide 

print("--- CLI Calculator ---")
print("1. Add | 2. Subtract | 3. Multiply | 4. Divide | 5. Exit")



while True:
    choice = int(input("Select operation (1-5) : "))

    if choice == 5:
        print ("Exiting...")
        break


    if choice >= 6 or choice <= 0:
        print ("Invalid Choice")
        continue



    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print("Result: ", add(num1, num2))


    if choice == 2:
        print("Result: ", subtract(num1, num2))


    if choice == 3:
        print("Result: ", multiply(num1, num2))

    if choice == 4:
        print("Result: ", divide(num1, num2))        