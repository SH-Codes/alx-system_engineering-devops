#!/usr/bin/python3
"""
100-main
"""
import sys

<<<<<<< HEAD
=======

>>>>>>> a46235057e8e5a21cf47637b5deb5dfbdeec9827
if __name__ == '__main__':
    count_words = __import__('100-count').count_words
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        result = count_words(sys.argv[1], [x for x in sys.argv[2].split()])
