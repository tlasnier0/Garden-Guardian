class GardenError(Exception):
    def __init__(self, message: str = "A Garden Error has occurred"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "A Plant Error has occurred"):
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name.capitalize() == plant_name:
        return
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(plant: list[str]) -> None:
    try:
        for str in plant:
            water_plant(str)
            print(f"Watering {str}: [OK]")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n.. ending tests and returning to main")
        return
    finally:
        print("Closing watering system\n")


def main() -> None:
    print("=== Garden Watering System ===\n")

    print("Testing valid plants...\nOpening watering system")
    test_watering_system(["Tomato", "Lettuce", "Carrots"])

    print("Testing invalid plants...\nOpening watering system")
    test_watering_system(["Tomato", "lettuce", "carrots"])

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
