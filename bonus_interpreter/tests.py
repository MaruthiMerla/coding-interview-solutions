import unittest
from solution import MiniInterpreter

class TestMiniInterpreter(unittest.TestCase):
    def setUp(self):
        self.interpreter = MiniInterpreter()
    
    def test_arithmetic(self):
        self.assertEqual(self.interpreter.evaluate("(+ 1 2)"), 3)
        self.assertEqual(self.interpreter.evaluate("(* 3 (+ 2 4))"), 18)
        self.assertEqual(self.interpreter.evaluate("(/ 10 2)"), 5.0)
    
    def test_let(self):
        self.assertEqual(self.interpreter.evaluate("(let x 5 y 10 (+ x y))"), 15)
        self.assertEqual(self.interpreter.evaluate("(let x 1 y x (+ x y))"), 2)
    
    def test_if(self):
        self.assertEqual(self.interpreter.evaluate("(if (> 3 2) 10 20)"), 10)
        self.assertEqual(self.interpreter.evaluate("(if (< 3 2) 10 20)"), 20)
        self.assertEqual(
            self.interpreter.evaluate("(let x 5 (if (== x 5) 100 200))"),
            100
        )
    
    def test_comparisons(self):
        self.assertTrue(self.interpreter.evaluate("(> 5 3)"))
        self.assertFalse(self.interpreter.evaluate("(<= 10 5)"))
        self.assertTrue(self.interpreter.evaluate("(== 7 7)"))
    
    def test_nested(self):
        expr = """
            (let x 10
                 y (if (> x 5) 20 30)
                 (+ x y))
        """
        self.assertEqual(self.interpreter.evaluate(expr), 30)

if __name__ == '__main__':
    unittest.main()