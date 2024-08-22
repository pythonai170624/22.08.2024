import calculator

def test_calculator_add_small():
    # Arrange
    x: int = 1
    y: int = 2
    expected: int = 3

    # Activate
    actual: int = calculator.add(x, y)

    # Assert
    assert actual == expected
