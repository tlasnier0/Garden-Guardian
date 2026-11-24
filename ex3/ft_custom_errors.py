class GardenError(Exception):
    def __init__(self, message: str = "A Garden Error has occurred"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "A Plant Error has occurred"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "A Water Error has occurred"):
        super().__init__(message)


def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        raise PlantError("The tomato plant is wilting!")
    elif operation_number == 1:
        raise WaterError("Not enough water in the tank!")


def test_error_types() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        garden_operations(0)
        print("Operation completed successfully")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        garden_operations(1)
        print("Operation completed successfully")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    for i in range(2):
        try:
            garden_operations(i)
            print("Operation completed successfully")
        except GardenError as e:
            print(f"Caught GardenError: {e}")

    print("\nAll custom types work correctly!")


if __name__ == "__main__":
    test_error_types()
