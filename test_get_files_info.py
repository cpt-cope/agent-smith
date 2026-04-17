from functions.get_files_info import get_files_info

root_test = get_files_info("calculator", ".")
pkg_test = get_files_info("calculator", "pkg")
bin_test = get_files_info("calculator", "/bin")
bad_test = get_files_info("calculator", "../")

print (root_test)
print (pkg_test)
print (bin_test)
print (bad_test)