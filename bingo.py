#!/usr/bin/env python

import random

def loadwords(filename):
    words = ["a","b","c","d","e","f","g","h","i"]
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

    cardsrequired = 10
    percard = 3

    # load words from file
    words = loadwords("words.txt")
    cards = []

    for cardnum in range(1,cardsrequired + 1):
        unique = False
        while unique == False:
            card = randomselection(words,percard)
            unique = uniquecard(card,cards)
        print card
        cards.append(card)

    return


if __name__ == '__main__':
    main()
