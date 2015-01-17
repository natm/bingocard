#!/usr/bin/env python

import sys
import random

def loadwords(filename):
    words = []
    for line in open(filename,'r').readlines():
       word = line.strip()
       if len(word) > 0:
           words.append(word.strip())
    return words

def uniquecard(card,cards):
    return True

def randomselection(source,amount):
    selection = []
    selection.extend(source)
    random.shuffle(selection)
    return selection[:amount]

def main():
    print "starting"

    cardsrequired = 100
    percard = 16

    # load words from file
    words = loadwords("words.txt")
    if percard > words:
        print "Not enough words provided"
        sys.exit(1)

    cards = []

    for cardnum in range(1,cardsrequired + 1):
        unique = False
        while unique == False:
            card = randomselection(words,percard)
            unique = uniquecard(card,cards)
        print card
        cards.append(card)

    sys.exit(0)


if __name__ == '__main__':
    main()
