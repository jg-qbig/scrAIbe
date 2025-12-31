from functions.get_file_content import get_file_content


def test():
    result = get_file_content("calculator", "lorem.txt")
    n = len(result)
    print(f"Number of characters in file: {n}\nTail: {result[n-100:]}")

    result = get_file_content("calculator", "main.py")
    print(result)

    result = get_file_content("calculator", "pkg/calculator.py")
    print(result)

    result = get_file_content("calculator", "/bin/cat")
    print(result)

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(result)


if __name__ == "__main__":
    test()
