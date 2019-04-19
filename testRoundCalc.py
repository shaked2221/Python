#shaked astemker 311499917
import unittest
import roundCalc

class TestCalc(unittest.TestCase):
    
    def test_mul1(self):
        "check if mul if work good"
        print("testing the mul function")
        actualResult=roundCalc.mul1(2,3)
        expectedResult = 6
        self.assertEqual(actualResult, expectedResult, "mul function failed")

    def test_rest_by_10(self):
        "check if the  rest work good on negtive"
        print("testing the rest function on negtive number")
        actualResult=roundCalc.rest_by_10(-4)
        expectedResult = 6
        self.assertEqual(actualResult, expectedResult, "rest_by_10 function failed on negtive number")

    def test_roundUpMul_1(self):
        "check if the  roundUpMul work good on positve num"
        print("testing the roundUpMul function on positve num")
        actualResult=roundCalc.roundUpMul(11,2)
        expectedResult = 30
        self.assertEqual(actualResult, expectedResult, "roundUpMul function failed on positve num")

    def test_roundUpMul_2(self):
        "check if the  roundUpMul work good on negtive num"
        print("testing the roundUpMul function on negtive num")
        actualResult=roundCalc.roundUpMul(11,-2)
        expectedResult = -20
        self.assertEqual(actualResult, expectedResult, "roundUpMul function failed on negtive num")

    def test_roundDownMul_1(self):
        "check if the roundDownMul work good on positve num"
        print("testing the roundDownMul function on positve num")
        actualResult=roundCalc.roundDownMul(11,2)
        expectedResult = 20
        self.assertEqual(actualResult, expectedResult, "roundDownMul function failed on positve num")

    def test_roundDownMul_2(self):
        "check if the roundDownMul work good on nagtive num"
        print("testing the roundDownMul function on nagtive number")
        actualResult=roundCalc.roundDownMul(11,-2)
        expectedResult = -30
        self.assertEqual(actualResult, expectedResult, "roundDownMul function failed on nagtive num num")


    def test_roundMax_1(self):
        "check if the roundMax work good on same number what hapen"
        print("testing the roundMax function when gat same number")
        actualResult=roundCalc.roundMax(9,9)
        expectedResult = 10
        self.assertEqual(actualResult, expectedResult, "roundMax function failed on give 2 same number")

    def test_roundMax_2(self):
        "check if the roundDownMul work good on one positve num and one neg num"
        print("testing the roundMax function  on one positve num and one neg num")
        actualResult=roundCalc.roundMax(11,-2)
        expectedResult = 20
        self.assertEqual(actualResult, expectedResult, "roundMax function failed on one number postive and one number nagtive")    

'''
if __name__=='__main__':
     unittest.main()
'''

        
        
    
