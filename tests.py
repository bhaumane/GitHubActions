# Write python program to perform unit testing on the sum_of_two_numbers function and print the results if test passes or fails.
import pytest
from main import sum_of_two_numbers

def test_sum_of_two_numbers():
    assert sum_of_two_numbers(10, 20) == 30
    assert sum_of_two_numbers(-5, 5) == 0
    assert sum_of_two_numbers(0, 0) == 0
    assert sum_of_two_numbers(-3, -7) == -10
if __name__ == "__main__":
    pytest.main()



    