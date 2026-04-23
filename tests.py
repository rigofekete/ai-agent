from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file_content import write_file
from functions.run_python import run_python_file


class test:
    # /// GET_FILES_INFO() TEST ///

    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)

    result = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result)

    result = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result)

    result = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(result)

    # /// GET_FILES_CONTENT() TEST ///
    result = get_file_content("calculator", "lorem.txt")
    print("Result for 'lorem.txt' file:")
    print(result)

    result = get_file_content("calculator", "main.py")
    print("Result for 'main.py' file:")
    print(result)

    result = get_file_content("calculator", "pkg/calculator.py")
    print("Result for 'calculator.py' file:")
    print(result)

    result = get_file_content("calculator", "/bin/cat")
    print("Result for '/bin/cat' directory:")
    print(result)

    # /// WRITE_FILE() TEST ///
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("Result for 'lorem.txt' content write file")
    print(result)

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("Result for 'pkg/morelorem.txt' content write file")
    print(result)

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("Result for '/tmp/temp.txt' content write file")
    print(result)

    # /// RUN_PYTHON() TEST ///
    result = run_python_file("calculator", "main.py")
    print("\nResult for 'main.py':\n")
    print(result)

    result = run_python_file("calculator", "tests.py")
    print("\nResult for 'tests.py':\n")
    print(result)

    result = run_python_file("calculator", "../main.py")
    print("\nResult for '../main.py':\n")
    print(result)

    result = run_python_file("calculator", "nonexistent.py")
    print("\nResult for 'nonexistent.py':\n")
    print(result)


if __name__ == "__main__":
    test()
