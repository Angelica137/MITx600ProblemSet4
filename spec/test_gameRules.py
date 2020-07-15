from gameRules import gameRules


def test_returns_hand_to_play():
    play = 'n'
    assert ifPlayN(play) ==


def test_getWordScore():
    """
    Unit test for getWordScore
    """
    failure = False
    # dictionary of words and scores
    words = {("", 7): 0, ("it", 7): 4, ("was", 7): 18, ("scored", 7): 54,
             ("waybill", 7): 155, ("outgnaw", 7): 127, ("fork", 7): 44, ("fork", 4): 94}
    for (word, n) in words.keys():
        score = getWordScore(word, n)
        if score != words[(word, n)]:
            print("FAILURE: test_getWordScore()")
            print("\tExpected", words[(word, n)], "points but got '" +
                  str(score) + "' for word '" + word + "', n=" + str(n))
            failure = True
    if not failure:
        print("SUCCESS: test_getWordScore()")
