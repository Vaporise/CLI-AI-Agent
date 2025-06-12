from functions.get_file_content import get_file_content

loremget = get_file_content("calculator", "lorem.txt")
mainget = get_file_content("calculator", "main.py")
calcget = get_file_content("calculator", "pkg/calculator.py")
catget = get_file_content("calculator", "/bin/cat")

print(loremget)
print(mainget)
print(calcget)
print(catget)