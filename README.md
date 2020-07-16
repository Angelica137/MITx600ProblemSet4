# MITx 600 problem set 4

- Word game

Dealing
A player is dealt a hand of n letters chosen at random (assume n=7 for now).

The player arranges the hand into as many words as they want out of the letters, using each letter at most once.

Some letters may remain unused (these won't be scored).

Scoring
The score for the hand is the sum of the scores for each word formed.

The score for a word is the sum of the points for letters in the word, multiplied by the length of the word, plus 50 points if all n letters are used on the first word created.

Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth 3, D is worth 2, E is worth 1, and so on. We have defined the dictionary SCRABBLE_LETTER_VALUES that maps each lowercase letter to its Scrabble letter value.

For example, 'weed' would be worth 32 points ((4+1+1+2) for the four letters, then multiply by len('weed') to get (4+1+1+2)\*4 = 32). Be sure to check that the hand actually has 1 'w', 2 'e's, and 1 'd' before scoring the word!

As another example, if n=7 and you make the word 'waybill' on the first try, it would be worth 155 points (the base score for 'waybill' is (4+1+4+3+1+1+1)\*7=105, plus an additional 50 point bonus for using all n letters).

## Sample output

Loading word list from file...
83667 words loaded.
Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: p z u t t t o
Enter word, or a "." to indicate that you are finished: tot
"tot" earned 9 points. Total: 9 points
Current Hand: p z u t
Enter word, or a "." to indicate that you are finished: .
Total score: 9 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: r
Current Hand: p z u t t t o
Enter word, or a "." to indicate that you are finished: top
"top" earned 15 points. Total: 15 points
Current Hand: z u t t
Enter word, or a "." to indicate that you are finished: tu
Invalid word, please try again.
Current Hand: z u t t
Enter word, or a "." to indicate that you are finished: .
Total score: 15 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: a q w f f i p
Enter word, or a "." to indicate that you are finished: paw
"paw" earned 24 points. Total: 24 points
Current Hand: q f f i
Enter word, or a "." to indicate that you are finished: qi
"qi" earned 22 points. Total: 46 points
Current Hand: f f
Enter word, or a "." to indicate that you are finished: .
Total score: 46 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: a r e t i i n
Enter word, or a "." to indicate that you are finished: inertia
"inertia" earned 99 points. Total: 99 points
Run out of letters. Total score: 99 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: e

### Notes

Problem 1: Word Scores
Implement code that allows to calcualte the score of a single word using the functoin getWordScore.

Prblem 2: Implement the function updateHand function to update the letters avalaibel to hte player once they have entered a word.

Problem 3: Implement hte isValidWord function to ensure the word the user enters is valid as per the hand they were dealt or the letters they have left.

for problem 3: This function (isValidWord) shouldn't use the function 'updateHand' - you don't want to mutate the hand within this function. A really helpful function is `getFrequencyDict` - this helper function is key to the solution to this problem.

Problem 4: Implement the function calcualteHandlen that returns the number of letters in the current hand.

Problem 5: Implement the playHand function to allow the user to play out a single hand.

Problem 6: Implement the playGame function. Remove the code that is currently uncommented in the playGame body. Read through the specification and make sure you understand what this function accomplishes. For the game, you should use the HAND_SIZE constant to determine the number of cards in a hand.

Problem 7: playing against the machine.
Use functions compChooseWord and compPlayHand

compChooseWord lets the computer choose a word and finds the word tha would give the highest score by iterating thorugh the list of words

compPlayHand lets the computer play

write code that implements the playGamefunction

This is a modified version of the playHand function from ps4a.
