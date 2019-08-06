import unittest
import RomanToDevanagariMap

class Test_test1(unittest.TestCase):
    def test_A(self):
        Map = RomanToDevanagariMap.RomanDiacriticToDevanagariMap()
        TestChar = u'\u1e41'

        Expected = u'\u0901'

        self.assertEqual(Map.GetDevanagari(TestChar), Expected)

if __name__ == '__main__':
    unittest.main()
