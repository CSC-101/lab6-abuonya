import data
from typing import Optional
from data import Book

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
#DESIGN RECIPE:
    # Purpose: This function, when given a single parameter of type list[Book]. uses a selection sort to sort the list of a book by title in alphabetical order.
    # Name of function: selection_sort_books
    # Input type: list[str]  Output type: list[str]
    # Example Input: [('Toni Morrison', 'The Bluest Eye'), ('Andy Weir', 'Project Hail Mary')]
    # Output given the example input: [('Andy Weir', 'Project Hail Mary'), ('Toni Morrison', 'The Bluest Eye')]
    #How would I solve this problem if I was a computer? I'd take my list of books, sort through the first index of each nested list (exclude the author).

def index_smallest_from1(books:list[Book], start:int) -> Optional[int]:
    mindex = start
    for idx in range(start + 1, len(books)):
        if books[idx].title < books[mindex].title:
            mindex = idx

    return mindex

def selection_sort_books(books: list[Book]) -> list:
    for idx in range(len(books) - 1):
        mindex = index_smallest_from1(books, idx)
        tmp = books[mindex]
        books[mindex] = books[idx]
        books[idx] = tmp
    return books

# Part 2
#DESIGN RECIPE:
    # Purpose: This function, when given a single parameter of type str, makes the lowercase character uppercase and vice versa for the given string.
    # Name of function: swap_case
    # Input type: str  Output type: str
    # Example Input: 'meow'
    # Output given the example input: 'MEOW'
    #How would I solve this problem if I was a computer? I'd iterate through each character, modifying the index's value to be upper/lower, depending on if its upper/lower.

def



# Part 3



# Part 4
