from functions.write_file import write_file

lorem_test = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
pkg_test = write_file("calculator", "pkg/morelorem.text", "lorem ipsum dolor sit amet")
tmp_test = write_file("calculator", "/tmp/temp.text", "this should not be allowed")

print(lorem_test)
print(pkg_test)
print(tmp_test)
