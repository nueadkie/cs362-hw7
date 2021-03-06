import unittest
import fizzbuzz

class Tester(unittest.TestCase):
  # Test that FizzBuzz can return a number that is not a multiple of 3 or 5.
  def test_normal(self):
    self.assertEqual(fizzbuzz.calc(2), "2")
  # Test if Fizz is returned for a number that is a multiple of 3.
  def test_fizz(self):
    self.assertEqual(fizzbuzz.calc(6), "Fizz")
  # Test if Buzz is returned for a number that is a multiple of 5.
  def test_buzz(self):
    self.assertEqual(fizzbuzz.calc(10), "Buzz")
  # Test if FizzBuzz is returned for a number that is a multiple of 3 and 5.
  def test_fizzbuzz(self):
    self.assertEqual(fizzbuzz.calc(15), "FizzBuzz")

if __name__ == '__main__':
  unittest.main()