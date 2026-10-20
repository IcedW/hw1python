def calculator():
    print("calculator")

    while True:
        print("1 +")
        print("2 -")
        print("3 *")
        print("4 /")
        print("5 Exit")

        choice = input("(1/2/3/4/5): ")
        if choice == '5':
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("num1: "))
                num2 = float(input("num2: "))
            except ValueError:
                print("wrong")
                continue

            if choice == '1':
                print(f"result: {num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"result: {num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"result: {num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 == 0:
                    break
                else:
                    print(f"result: {num1} / {num2} = {num1 / num2}")
        else:
            print("wrong")

if __name__ == "__main__":
    calculator()
