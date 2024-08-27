def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b

def test_add_numbers():
    """Test the add_numbers function."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    print("All tests passed!")

if __name__ == "__main__":
    test_add_numbers()
