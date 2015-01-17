#!/usr/bin/env python

import csv
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

def writecsv(cards):
    header = []
    for col in range(1,len(cards[0]) + 1):
        header.append("Word%d" % col)
    writer = csv.writer(sys.stdout, delimiter=',',quotechar='\"', quoting=csv.QUOTE_ALL)
    writer.writerow(header)
    for card in cards:
        writer.writerow(card)

def main():

    cardsrequired = 100
    percard = 9

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
        cards.append(card)
    writecsv(cards)

    sys.exit(0)


if __name__ == '__main__':
    main()
