### more test cases for isValidWord

hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1}
word = "rapture"
print(hand)
print(getFrequencyDict(word))
print(updateHand(hand, word))
print(isValidWord(word, hand, wordList))
print("---------------\n")

hand = {'k': 1, 'i': 2, 'o': 1, 'b': 1, 'w': 1, 'j': 1}
word = "kwijibo"
print("hand" + str(hand))
print("frequency" + str(getFrequencyDict(word)))
print("updateHand" + str(updateHand(hand, word)))
print(isValidWord(word, hand, wordList))
print("---------------\n")

hand = {'c': 2, 'h': 1, 'a': 1, 't': 2, 'o': 2, 'u': 2, 'y': 1, 'z': 1}
word = "chayote"
print("hand" + str(hand))
print("e" in hand.keys())
print("frequency" + str(getFrequencyDict(word)))
print("updateHand" + str(updateHand(hand, word)))
print(isValidWord(word, hand, wordList))
print("---------------\n")
