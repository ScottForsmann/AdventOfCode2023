from collections import defaultdict

faces = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
def getScore(hand):
    score = [0]

    """
    First number represents:
    6: five of kind
    5: four of kind
    4: full house
    3: three of a kind
    2: two pair
    1: one pair
    0: high card
    
    Next 5 numbers represent the value of the cards
    """

    count = defaultdict(int)
    for c in hand:
        count[c] += 1

        if c.isnumeric():
            score.append(int(c))
        else:
            score.append(faces[c])

    unique_cards = count.keys()

    # Five of a kind
    if len(unique_cards) == 1:
        score[0] = 6

    # Four of a kind OR Full House
    elif len(unique_cards) == 2:
        score[0] = 4
        for card in unique_cards:
            if count[card] == 4:
                score[0] = 5

    # Three of a Kind OR Two Pairs
    elif len(unique_cards) == 3:
        score[0] = 2
        for card in unique_cards:
            if count[card] == 3:
                score[0] = 3

    # One Pair
    elif len(unique_cards) == 4:
        score[0] = 1

    # High Card
    else:
        score[0] = 0

    return score


def main():
    data = open('data.txt').read().strip().split('\n')
    maxRank = len(data)

    for i in range(len(data)):
        data[i] = data[i].split()

    scoresBids = []

    for hand, bid in data:
        score = getScore(hand)
        scoresBids.append([score, int(bid)])

    scoresBids.sort()

    rank = 1
    res = 0
    for _, bid in scoresBids:
        res += rank * bid
        rank += 1

    print(res)

if __name__ == "__main__":
    main()