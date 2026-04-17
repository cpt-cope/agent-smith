from functions.run_python_file import run_python_file

main_test = run_python_file("calculator", "main.py")
rendered_main_test = run_python_file("calculator", "main.py", ["3 + 5"])
tests_test = run_python_file("calculator", "tests.py")
bad_test = run_python_file("calculator", "../main.py")
non_existent_test = run_python_file("calculator", "nonexistent.py")
lorem_test = run_python_file("calculator", "lorem.txt")

print(main_test)
print(rendered_main_test)
print(tests_test)
print(bad_test)
print(non_existent_test)
print(lorem_test)