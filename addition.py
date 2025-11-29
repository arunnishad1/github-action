def addition(num1, num2):
    return (num1+num2)

def test_add():
    assert addition(2, 3) == 5
    assert addition(-1, 4) == 3
    assert addition(0, 0) == 0

test_add()

print("All test cases passed successfully...")