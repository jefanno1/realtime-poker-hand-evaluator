from collections import Counter

def findPokerHand(hand):
    ranks = []
    suits = []


    symbol_dict = {
        "J" : 11,
        "Q" : 12,
        "K" : 13,
        "A" : 14
    }

    for card in hand:
        symbol = card[-1]
        number = card[:-1]

        if number in symbol_dict:
            number = symbol_dict[number]
        else:
            number = int(number)
        
        ranks.append(number)
        suits.append(symbol)

    sorted_ranks = sorted(ranks)

    frequence = list(Counter(ranks).values())

    is_flush = len(set(suits)) == 1

    is_straight = (len(set(ranks)) == 5) and (sorted_ranks[-1] - sorted_ranks[0] == 4)


    if is_straight and is_flush and sorted_ranks[-1] == 14:
        return "Royal Flush"
    elif is_straight and is_flush:
        return "Straight Flush"
    elif 4 in frequence:
        return "Four of a Kind"
    elif 3 in frequence and 2 in frequence:
        return "Full House"
    elif is_flush:
        return "Flush"
    elif is_straight:
        return "Straight"
    elif 3 in frequence:
        return "Three of a Kind"
    elif frequence.count(2) == 2:
        return "Two Pair"
    elif 2 in frequence:
        return "Pair"
    else:
        return "High Card"

# --- AREA UJI COBA ---
if __name__ == "__main__":
    print(findPokerHand(["KH", "AH", "QH", "JH", "10H"]))  # Hasil: Royal Flush
    print(findPokerHand(["QC", "JC", "10C", "9C", "8C"]))  # Hasil: Straight Flush
    print(findPokerHand(["5C", "5S", "5H", "5D", "QH"]))   # Hasil: Four of a Kind
    print(findPokerHand(["2H", "2D", "2S", "10H", "10C"])) # Hasil: Full House
    print(findPokerHand(["2D", "KD", "7D", "6D", "5D"]))   # Hasil: Flush
    print(findPokerHand(["JC", "10H", "9C", "8C", "7D"]))  # Hasil: Straight