vowels = ['a', 'e', 'i', 'o',' u', 'A', 'E', 'I', 'O', 'U']

name = input("Enter your name: ")
reversed_name = ""

name_length = len(name)
check = False

while(name_length):
    char = name[name_length-1]
    reversed_name += char
    if char in vowels:
        check = True
    name_length -= 1

print("name --> ",name)
print("this is test")
print(f"Your reversed name is {reversed_name}")
if check:
    print("Your name have vowels in it")
else:
    print("Your name does not contain vowles")
