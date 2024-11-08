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
    print(books)
    return books

# Part 2
#DESIGN RECIPE:
    # Purpose: This function, when given a single parameter of type str, makes the lowercase character uppercase and vice versa for the given string.
    # Name of function: swap_case
    # Input type: str  Output type: str
    # Example Input: 'meow'
    # Output given the example input: 'MEOW'
    #How would I solve this problem if I was a computer? I'd iterate through each character, modifying the index's value to be upper/lower, depending on if its upper/lower.

def swap_case (string:str) -> str:
    final_swap = []
    for idx in string:
        if idx.isupper(): # uppercase --> lowercase
            final_swap.append(idx.lower())
        elif idx.islower():  # lowercase --> uppercase
            final_swap.append(idx.upper())
        else:
            final_swap.append(idx) # keep anything that isn't changed

    final_swap = ''.join(final_swap)
    print(final_swap)
    return final_swap

# Part 3
#DESIGN RECIPE:
    # Purpose: This function, when given three parameters (a strings, two of which are the old and new character) and returns a  new string that replaces each occurrence of the old character with the new character.
    # Name of function: str_translate
    # Input type: str  Output type: str
    # Example Input: 'Wow!' , w, e
    # Output given the example input: 'eoe'
    #How would I solve this problem if I was a computer? I'd iterate through each character, modifying the index's value IF it is equal to the old character provided,
    # changing that index value to the new character.

def str_translate(string:str, old:str, new:str) -> str:
    translated_str = []
    for idx in string:
        if idx == old:
            translated_str.append(new)
        else:
            translated_str.append(idx)

    translated_str = ''.join(translated_str)
    print(translated_str)
    return translated_str

# Part 4
#DESIGN RECIPE:
    # Purpose: This function, when given a single string, returns a dictionary mapping of strings to integers. It counts the number of times the word appears in the string.
    # Name of function: histogram
    # Input type: str  Output type: str
    # Example Input: "Cat Cat Cat Cat"
    # Output given the example input: {"Cat":4}
    #How would I solve this problem if I was a computer? create an empty dictionary to populate with words (key) and their associated count (value) to create a key-value pair.

def histogram(string:str) -> dict:
    temp = str.split(string)
    dict = {}
    for x in temp:
        if x not in dict:
            dict[x] = 1
        else:
            dict[x] += 1
    print(dict)
    return dict
