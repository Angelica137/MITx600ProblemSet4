### more test cases for isValidWord

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

hand = {'r': 1, 'h': 1, 'a': 1, 'm': 2, 'e': 1}
word = "hammer"
print("hand" + str(hand))
print("e" in hand.keys())
print("frequency" + str(getFrequencyDict(word)))
print("updateHand" + str(updateHand(hand, word)))
print(isValidWord(word, hand, wordList))
print("---------------\n")

hand = {'a': 3, 'p': 2, 't': 1, 'e': 1, 'r': 1, 'u': 1}
word = "rapture"
print("hand" + str(hand))
print("e" in hand.keys())
print("frequency" + str(getFrequencyDict(word)))
print("updateHand" + str(updateHand(hand, word)))
print(isValidWord(word, hand, wordList))
print("---------------\n")
