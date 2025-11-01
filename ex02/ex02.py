def multiply_all (*args: int) -> int:
    result = 1
    for i in args:
        result *= i
    return result

if __name__ == "__main__":
    print(multiply_all(1,2,3,4,5))