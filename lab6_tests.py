import data
import lab6
import unittest
from data import Book


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1

    def test_selection_sort_books1(self):
        books_to_sort1 = Book('Toni Morrison', 'The Bluest Eye')
        books_to_sort2 = Book('Andy Weir', 'Project Hail Mary')
        books_list = [books_to_sort1, books_to_sort2]
        result = lab6.selection_sort_books(books_list)
        expected = [Book('Andy Weir', 'Project Hail Mary'), Book('Toni Morrison', 'The Bluest Eye')]
        self.assertEqual(expected, result)

    def test_selection_sort_books2(self):
        books_to_sort1 = Book('Toni Morrison', 'The Bluest Eye')
        books_to_sort2 = Book('Andy Weir', 'Project Hail Mary')
        books_to_sort3 = Book('Random Author', 'A Silly Tale')
        books_list = [books_to_sort1, books_to_sort2, books_to_sort3]
        result = lab6.selection_sort_books(books_list)
        expected = [Book('Random Author', 'A Silly Tale'), Book('Andy Weir', 'Project Hail Mary'), Book('Toni Morrison', 'The Bluest Eye')]
        self.assertEqual(expected, result)

    def test_selection_sort_books3(self):
        books_list = []
        result = lab6.selection_sort_books(books_list)
        expected = []
        self.assertEqual(expected, result)
    # Part 2
    def test_swap_case1(self):
        string = 'meow'
        result = lab6.swap_case(string)
        expected = 'MEOW'
        self.assertEqual(expected, result)

    def test_swap_case2(self):
        string = 'MeOw!!1'
        result = lab6.swap_case(string)
        expected = 'mEoW!!1'
        self.assertEqual(expected, result)

    def test_swap_case3(self):
        string = '143 <3'
        result = lab6.swap_case(string)
        expected = '143 <3'
        self.assertEqual(expected, result)

    # Part 3
    def test_str_translate1(self):
        string = 'WOW!'
        old = 'W'
        new = 'E'
        result = lab6.str_translate(string, old, new)
        expected = 'EOE!'
        self.assertEqual(expected, result)

    def test_str_translate2(self):
        string = 'WWWWWWWWWW!2345'
        old = 'W'
        new = 'E'
        result = lab6.str_translate(string, old, new)
        expected = 'EEEEEEEEEE!2345'
        self.assertEqual(expected, result)

    def test_str_translate3(self):
        string = 'I Love My Fat Cat'
        old = 'a'
        new = 'W'
        result = lab6.str_translate(string, old, new)
        expected = 'I Love My FWt CWt'
        self.assertEqual(expected, result)

    # Part 4
    def test_histogram1(self):
        string = "I Love Love Love Love My Cat"
        result = lab6.histogram(string)
        expected = {"I":1, "Love":4, "My":1, "Cat":1}
        self.assertEqual(expected, result)

    def test_histogram2(self):
        string = "Meow Meow Meow Meow Meow Meow"
        result = lab6.histogram(string)
        expected = {"Meow":6}
        self.assertEqual(expected, result)

    def test_histogram3(self):
        string = ""
        result = lab6.histogram(string)
        expected = {}
        self.assertEqual(expected, result)




if __name__ == '__main__':
    unittest.main()
