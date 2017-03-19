#!/usr/bin/python

import sys


def main():

    current_word = None
    current_count = 0

    for line in sys.stdin:
        word, count = line.split('\t')
        count = int(count)

        if current_word == word:
            current_count += count
        else:
            if current_word:
                print(str(word) + '\t' + str(current_count))

            current_word = word
            current_count = count

main()