def subtraction(num1, num2):
    return (num1-num2)


def test_subtract():
    assert subtraction(5, 3) == 2
    assert subtraction(10, 4) == -5
    assert subtraction(0, 0) == 0


test_subtract()
print("All test cases passed successfully...")