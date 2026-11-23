def input_temperature(temp_str: str) -> int:
    temp_int: int = int(temp_str)

    if temp_int < 0:
        raise ValueError(f"{temp_int}°C is too cold for plants (min 0°C)")
    elif temp_int > 40:
        raise ValueError(f"{temp_int}°C is too hot for plants (max 40°C)")
    else:
        return temp_int


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===\n")

    for data in ['25', 'abc', '100', '-50']:
        print(f"Input data is '{data}'")
        try:
            print(f"Temperature is now {input_temperature(data)}°C\n")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}\n")

    print("All tests completed - program didn't crash!")

    print()


if __name__ == "__main__":
    test_temperature()
