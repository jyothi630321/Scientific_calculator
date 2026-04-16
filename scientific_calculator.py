import math
print("=== Scientific Calculator ===")
while True:
    print("\n1. Square Root")
    print("2. Power")
    print("3. Factorial")
    print("4. Sine")
    print("5. Cosine")
    print("6. Show Pi")
    print("7. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        num = float(input("Enter number: "))
        print("Result:", math.sqrt(num))
    elif choice == "2":
        a = float(input("Enter base: "))
        b = float(input("Enter power: "))
        print("Result:", math.pow(a, b))
    elif choice == "3":
        num = int(input("Enter number: "))
        print("Result:", math.factorial(num))
    elif choice == "4":
        num = float(input("Enter angle in radians: "))
        print("Result:", math.sin(num))
    elif choice == "5":
        num = float(input("Enter angle in radians: "))
        print("Result:", math.cos(num))
    elif choice == "6":
        print("Pi Value:", math.pi)
    elif choice == "7":
        print("Thank you!")
        break
    else:
        print("Invalid Choice")