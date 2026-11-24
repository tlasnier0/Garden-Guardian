def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        raise ValueError("invalid literal for int() with base 10: 'abc'")
    elif operation_number == 1:
        raise ZeroDivisionError("division by zero")
    elif operation_number == 2:
        raise FileNotFoundError("[Errno 2] No such file or directory: "
                                "'/non/existent/file'")
    elif operation_number == 3:
        raise TypeError('can only concatenate str (not "int") to str')
    else:
        return


def test_error_type() -> None:
    print("=== Garden Error Types Demo ===")
    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_type()
