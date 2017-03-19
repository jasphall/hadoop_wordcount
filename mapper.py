#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from nltk.corpus import stopwords


def main():

    for line in sys.stdin:
        line = line.strip()
        words = line.split()
        for word in words:
            if len(word) != 0 and word.lower().decode('utf-8') not in stopwords.words('english'):
                processed_word = ''.join(letter for letter in word if letter.isalnum())
                print(str(processed_word) + '\t' + str(1))

main()