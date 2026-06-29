from num_to_language.converter import num_to_language


def main():
    print("Number to Language")
    print()

    while True:
        value = input("Enter a decimal number (q to quit): ")

        if value.lower() == "q":
            break

        try:
            print(num_to_language(value))
        except ValueError as error:
            print(error)

        print()


if __name__ == "__main__":
    main()