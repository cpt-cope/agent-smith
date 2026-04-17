from functions.get_file_content import *

lorem_test = get_file_content("calculator", "lorem.txt")
main_test = get_file_content("calculator", "main.py")
pkg_test = get_file_content("calculator", "pkg/calculator.py")
bin_test = get_file_content("calculator", "/bin/cat")
bad_file_test = get_file_content("calculator", "pkg/does_not_exist.py")


print (lorem_test)
print (main_test)
print (pkg_test)
print ( bin_test)
print (bad_file_test)

