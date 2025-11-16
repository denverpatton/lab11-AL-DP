import unittest
from calculator import mul, div, log, hypotenuse, square_root

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ####### Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2,3), 6)
        self.assertEqual(mul(2,8), 16)
        self.assertEqual(mul(2,-1), -2)


    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(2,3), 1.5)
        self.assertAlmostEqual(div(6,8), 4/3)
        self.assertAlmostEqual(div(6,-1), -1/6)

    ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 16)
        with self.assertRaises(ValueError):
            log(-2, 32)
        self.assertAlmostEqual(log(2, 16), 4)


    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(2,2), 2.82842712)
        self.assertAlmostEqual(hypotenuse(5,3), 5.83095189)
        self.assertAlmostEqual(hypotenuse(4,12), 12.6491106)

    def test_sqrt(self): # 3 assertions
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(9), 3)
        with self.assertRaises(ValueError):
            square_root(-1)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()