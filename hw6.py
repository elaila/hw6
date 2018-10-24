import re
import unittest

def sumNums(fileName):
    list_num = []
    open_file = open(fileName, 'r')
    readlines = open_file.readlines()
    sum = 0
    for line in readlines:
        list_num += re.findall(r'[0-9]+', line)
    for num in list_num:
        sum += int(num)
    open_file.close()
    return(sum)

def countWord(fileName, word):
    open_f = open(fileName, 'r')
    readlines = open_f.readlines()
    set_count = 0
    for line in readlines:
        l = line.lower()
        set_word = re.findall(r'\b'+ word + r'\b', l)
        set_count += len(set_word)
    open_f.close()
    return set_count

def listURLs(fileName):
    open_file = open(fileName, 'r')
    readlines = open_file.readlines()
    urls = []
    for line in readlines:
        urls += re.findall(r'w+\.\S+\.\S+', line)
    open_file.close()
    return urls

class TestHW6(unittest.TestCase):
    """ Class to test this homework """

    def test_sumNums1(self):
        """ test sumNums on the first file """
        self.assertEqual(sumNums("regex_sum_42.txt"), 445833)

    def test_sumNums2(self):
        """ test sumNums on the second file """
        self.assertEqual(sumNums("regex_sum_132198.txt"), 374566)

    def test_countWord(self):
        """ test count word on the first file """
        self.assertEqual(countWord("regex_sum_42.txt", "computer"),21)

    def test_listURLs(self):
        """ test list URLs on the first file """
        self.assertEqual(len(listURLs("regex_sum_42.txt")), 3)

# run the tests
unittest.main(verbosity=2)
