import unittest
import fact_prime_area   # import the file
 
class TestPrime(unittest.TestCase):
   
    def test_factorial(self):
        self.assertEqual(fact_prime_area.factorial(4),24)

    def test_factorial(self):
       self.assertEqual(fact_prime_area.factorial(0),120)
       with self.assertRaises(ValueError):
          fact_prime_area.factorial(0)   
  
    def test_prime(self):
        self.assertEqual(fact_prime_area.prime(31),True)

    def test_prime(self):
        self.assertEqual(fact_prime_area.prime(17),True)

    def test_prime(self):
        self.assertEqual(fact_prime_area.prime(0),False)
        with self.assertRaises(ValueError):
            fact_prime_area.prime(0)   

    def test_area(self):
        self.assertEqual(fact_prime_area.circlearea(4),28.26)   

    def test_area(self):
        self.assertEqual(fact_prime_area.circlearea(0), False)
        with self.assertRaises(ValueError):
            fact_prime_area.circlearea(0)     

if __name__ == "__main__":
    unittest.main()
