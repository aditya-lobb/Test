def main():
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    try:
        name = input("Enter your name: ").strip()

        if not name:
            print("Error: Name cannot be empty")
            return 400

        reversed_name = ""
        name_length = len(name)
        check = False

        while name_length:
            char = name[name_length - 1]
            reversed_name += char
            if char in vowels:
                check = True
            name_length -= 1

        print("name -->", name)
        print("this is test main")
        print(f"Your reversed name is {reversed_name}")
        if check:
            print("Your name has vowels in it.")
        else:
            print("Your name does not contain vowels.")

        return 200

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 500


if __name__ == "__main__":
    main()
