from functions.run_python import run_python_file

def test():
    print(f"Result for main.py\n{run_python_file("calculator", "main.py")}")
    print(f"Result for main.py calc\n{run_python_file("calculator", "main.py", ["3 + 5"])}")
    print(f"Result for tests.py\n{run_python_file("calculator", "tests.py")}")
    print(f"Result for ../main.py\n{run_python_file("calculator", "../main.py")}")
    print(f"Result for nonexistent.py\n{run_python_file("calculator", "nonexistent.py")}")
     
test()