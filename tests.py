from functions.get_files_info import get_files_info

dotcheck = get_files_info("calculator", ".")
pkgcheck = get_files_info("calculator", "pkg")
bincheck = get_files_info("calculator", "/bin")
dotscheck = get_files_info("calculator", "../")

print(dotcheck)
print(pkgcheck)
print(bincheck)
print(dotscheck)