import unittest
import SimpleCalculator from simple_calculator

class TestSimpleCalculator(unittest.TestCase):
    def setup(self):
       # Set up the SimpleCalculator instance before each test.
        self.calc = SimpleCalculator()


    def test_addition(self):
        #Test the addition method.
        self.assertEqual(self.calc.add(2,3),5)
        self.assertEqual(self.calc.add(-2,3),1)
        self.assertEqual(self.calc.add(-1,1),0)
        self.assertEqual(self.calc.add(2,-3),-1)
        self.assertEqual(self.calc.add(-2,-3),-5)
    
    def test_subtraction(self):
        #Test the subtraction method.
        self.assertEqual(self.calc.subtract(2,3),-1)
        self.assertEqual(self.calc.subtract(-2,-3),1)
        self.assertEqual(self.calc.subtract(2,-3),5)
        self.assertEqual(self.calc.subtract(1,1),0)
        self.assertEqual(self.calc.subtract(4,10),-6)

    def test_multiply(self):
        # Test the multiply method.
        self.assertEqual(self.calc.multiply(2,3), 6)
        self.assertEqual(self.calc.multiply(-2,-3), 6)
        self.assertEqual(self.calc.multiply(2,-3), -6)
        self.assertEqual(self.calc.multiply(-2,3), -6)
        self.assertEqual(self.calc.multiply(2,0), 0)

    def test_divide(self):
        #Test the divide method.
        self.assertEqual(self.calc.divide(6,3), 2)
        self.assertEqual(self.calc.divide(6,0), None)
        self.assertEqual(self.calc.divide(6,-3), -2)
        self.assertEqual(self.calc.divide(-6,-3),2)
        self.assertEqual(self.calc.divide(-6,3),-2)
