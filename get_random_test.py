import unittest

from collections import Counter

from get_random import get_random


def createTestData(maxNum, testRange):
    return [get_random(maxNum) for i in range(testRange)]


def CountTestData(testData):
    return Counter(testData)


def checkFrequencyEvenness(testDataCounter, testRange):
    mostFrequentCount = max(testDataCounter.values())
    return mostFrequentCount < (testRange // 2)


class TestMaxZero(unittest.TestCase):
    def setUp(self):
        self.maxNum = 0
        self.testRange = 10

        self.testData = createTestData(self.maxNum, self.testRange)
        self.testDataCounter = CountTestData(self.testData)

    def testRangeSuccess(self):
        self.assertTrue(max(self.testData) <= self.maxNum, "success")
        self.assertTrue(min(self.testData) >= 0, "success")


class TestMaxTen(unittest.TestCase):
    def setUp(self):
        self.maxNum = 10
        self.testRange = 50

        self.testData = createTestData(self.maxNum, self.testRange)
        self.testDataCounter = CountTestData(self.testData)

    def testRangeSuccess(self):
        self.assertTrue(max(self.testData) <= self.maxNum, "success")
        self.assertTrue(min(self.testData) >= 0, "success")

    def testRandomPercentSuccess(self):
        self.assertTrue(checkFrequencyEvenness(self.testDataCounter, self.testRange))


class TestMaxHundred(unittest.TestCase):
    def setUp(self):
        self.maxNum = 100
        self.testRange = 1000

        self.testData = createTestData(self.maxNum, self.testRange)
        self.testDataCounter = CountTestData(self.testData)

    def testRangeSuccess(self):
        self.assertTrue(max(self.testData) <= self.maxNum, "success")
        self.assertTrue(min(self.testData) >= 0, "success")

    def testRandomPercentSuccess(self):
        self.assertTrue(checkFrequencyEvenness(self.testDataCounter, self.testRange))


class TestMaxThousand(unittest.TestCase):
    def setUp(self):
        self.maxNum = 1000
        self.testRange = 10000
        
        self.testData = createTestData(self.maxNum, self.testRange)
        self.testDataCounter = CountTestData(self.testData)

    def testRangeSuccess(self):
        self.assertTrue(max(self.testData) <= self.maxNum, "success")
        self.assertTrue(min(self.testData) >= 0, "success")

    def testRandomPercentSuccess(self):
        self.assertTrue(checkFrequencyEvenness(self.testDataCounter, self.testRange))


if __name__ == "__main__":
    unittest.main()
