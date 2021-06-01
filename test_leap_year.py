import unittest
import leap_year

class Tester(unittest.TestCase):
  # Test that 2004 is recognized as a leap year, but 2003 is not.
  def test_div_by_4(self):
    self.assertTrue(leap_year.calc(2004) == True and leap_year.calc(2003) == False)
  
  # Test that 1900 is not recognzied as a leap year.
  def test_div_by_100(self):
    self.assertFalse(leap_year.calc(1900))

if __name__ == '__main__':
  unittest.main()