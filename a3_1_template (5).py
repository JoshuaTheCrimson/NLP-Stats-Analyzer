import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import numpy as np
nltk.download('punkt')
nltk.download('gutenberg')
from sklearn.feature_extraction.text import TfidfVectorizer
import collections
import os
import pandas as pd
os.system("python -m spacy download en_core_web_sm")
import en_core_web_sm
import collections

# Task 1 (3 marks)
def stats_pos(csv_file_path):
    """Return the normalized frequency of all appeared part of speech in the questions and answers
    (namely the `sentence text` column) in the given csv file, respectively. Each of the resulting 
    two lists must be sorted alphabetically according to tags.
    Example:
    >>> stats_pos('dev_test.csv')
    output would look like [(ADV, 0.1), (NOUN, 0.21), ...], [(ADJ, 0.08), (ADV, 0.22), ...]
    """

 
        
    return [], []

# Task 2 (3 marks)
def stats_top_stem_ngrams(csv_file_path, n, N):
    """Return the N most frequent n-gram of stems together with their normalized frequency 
    for questions and answers, respectively. Each is sorted in descending order of frequency
    Example:
    >>> stats_top_stem_ngrams('dev_test.csv', 2, 5)
    output would look like [('what', 'is', 0.43), ('how', 'many', 0.39), ....], [('I', 'feel', 0.64), ('pain', 'in', 0.32), ...]
    """
    # read data to list

    
    return [], []

# Task 3 (2 marks)
def stats_ne(csv_file_path):
    """Return the normalized frequency of all named entity types for questions and answers, respectively.
    Each is sorted in descending order of frequency.
    Example:
    >>> stats_ne('dev_test.csv')
    output would look like [(DATE, 0.34), ....]
    """
    
    return [], []

# Task 4 (2 marks)
def stats_tfidf(csv_file_path):
    """Return the ratio of questions that its most similar sentence falls in its answers.
    Example:
    >>> stats_tfidf('dev_test.csv')
    output would be a decimal like 0.38
    """
  
   
    return 0


# DO NOT MODIFY THE CODE BELOW
if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
    # print("---------Task 1---------------")
    # print(stats_pos('data/dev_test.csv'))
  
    # print("---------Task 2---------------")
    # print(stats_top_stem_ngrams('data/dev_test.csv', 2, 5))

    # print("---------Task 3---------------")
    # print(stats_ne('data/dev_test.csv'))

    # print("---------Task 4---------------")
    # print(stats_tfidf('data/dev_test.csv'))
  
