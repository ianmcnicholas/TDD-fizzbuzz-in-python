import fizzBuzz

def test_checkForFizz():
    assert fizzBuzz.fizzBuzz(1) != "Fizz"
    assert fizzBuzz.fizzBuzz(3) == "Fizz"
    assert fizzBuzz.fizzBuzz(5) != "Fizz"
    assert fizzBuzz.fizzBuzz(15) != "Fizz"

def test_checkForBuzz():
    assert fizzBuzz.fizzBuzz(1) != "Buzz"
    assert fizzBuzz.fizzBuzz(3) != "Buzz"
    assert fizzBuzz.fizzBuzz(5) == "Buzz"
    assert fizzBuzz.fizzBuzz(15) != "Buzz"

def test_checkForFizzBuzz():
    assert fizzBuzz.fizzBuzz(1) != "FizzBuzz"
    assert fizzBuzz.fizzBuzz(3) != "FizzBuzz"
    assert fizzBuzz.fizzBuzz(5) != "FizzBuzz"
    assert fizzBuzz.fizzBuzz(15) == "FizzBuzz"