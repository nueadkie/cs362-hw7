import unittest
import fizzbuzz

class Tester(unittest.TestCase):
  # Test that FizzBuzz can return a number that is not a multiple of 3 or 5.
  def test_normal(self):
    self.assertEqual(fizzbuzz.calc(2), "2")
  # Test if Fizz is returned for a number that is a multiple of 3.
  def test_fizz(self):
    self.assertEqual(fizzbuzz.calc(15), "Fizz")

if __name__ == '__main__':
  unittest.main()