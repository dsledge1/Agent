from functions.get_file_content import get_file_content

def test():
    print(f"Result for main.py\n{get_file_content("calculator", "main.py")}")
    print(f"Result for pkg/calculator.py\n{get_file_content("calculator", "pkg/calculator.py")}")
    print(f"Result for /bin/cat\n{get_file_content("calculator", "/bin/cat")}")
    print(f"Result for does not exist\n{get_file_content("calculator", "pkg/does_not_exist.py")}")

test()