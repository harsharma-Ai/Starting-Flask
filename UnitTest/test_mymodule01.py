import unittest

from mymodule import square, doubler, add
class TestMyModule(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(2), 4)
        
        self.assertEqual(square(3), 9)
        
        self.assertNotEqual(square(-3), -9)
        
    def test_doubler(self):
        self.assertEqual(doubler(2),4)
        
        self.assertEqual(doubler(-3.1),-6.2)
        
        self.assertEqual(doubler(0),0)  
        
if __name__ == '__main__':
    unittest.main()