# functions.py
# Katherine Taylor
# 2022-01-16

# libraries
from typing import Collection
import random
import collections

# deal round
def deal_round(card_dict):
    hand_1, cards_remaining = deal_hand(10, card_dict)
    hand_2, cards_remaining_2  = deal_hand(10, cards_remaining)
    return hand_1, hand_2, cards_remaining_2

def deal_hand(num_cards, card_dict):
    hand = random.choices(list(card_dict.keys()), weights = list(card_dict.values()), k = num_cards)
    cards_remaining = remove_from_deck(hand, card_dict)
    return hand, cards_remaining
    
def remove_from_deck(hand, card_dict):
    to_remove = collections.Counter(hand)
    new_freq = card_dict
    for card in new_freq:
        new_freq[card] -= to_remove[card]
    return new_freq


# play round
def play_round(hand_player_1, hand_player_2, hold_1, hold_2):
    while len(hand_player_1) > 0:
        pick_1 = random.choice(hand_player_1)
        hold_1.append(pick_1)
        hand_player_1.remove(pick_1)
        pick_2 = random.choice(hand_player_2)
        hold_2.append(pick_2)
        hand_player_2.remove(pick_2)
        temp_hand = hand_player_2
        hand_player_2 =  hand_player_1
        hand_player_1 = temp_hand        
    return hold_1, hold_2

def score_round(round_num, hold_1, hold_2, prev_score_1, prev_score_2, dumpling_values):
    counts_1 = collections.Counter(hold_1)
    counts_2 = collections.Counter(hold_2)
    # puddings
    puddings_1 = counts_1["pudding"]
    puddings_2 = counts_2["pudding"]

    if round_num == 3:
        if puddings_1 > puddings_2:
            prev_score_1 += 6
            prev_score_2 -= 6
        elif puddings_1 == puddings_2:
            prev_score_1 += 3
            prev_score_2 += 3
        else:
            prev_score_1 -= 6
            prev_score_2 += 6
    # maki rolls
    maki_1 = (counts_1["maki roll 3"] * 3 + counts_1["maki roll 2"] * 2 + counts_1["maki roll 1"])
    maki_2 = (counts_2["maki roll 3"] * 3 + counts_2["maki roll 2"] * 2 + counts_2["maki roll 1"])
    if maki_1 > maki_2:
        prev_score_1 += 6
        prev_score_2 += 3
    elif maki_1 == maki_2:
        prev_score_1 += 3
        prev_score_2 += 3
    else:
        prev_score_1 += 3
        prev_score_2 += 3
    
    # tempura
    if counts_1["tempura"] // 2 > 0:
        prev_score_1 += (counts_1["tempura"] // 2) * 5
    if counts_2["tempura"] // 2 > 0:
        prev_score_2 += (counts_2["tempura"] // 2) * 5
    
    if counts_1["sashimi"] // 3 > 0:
        prev_score_1 += (counts_1["sashimi"] // 3) * 10
    if counts_2["sashimi"] // 3 > 0:
        prev_score_2 += (counts_2["sashimi"] // 3) * 10
    
    # squid nigiri
    if counts_1["squid nigiri"] > 0:
        prev_score_1 += counts_1["squid nigiri"] * 3
    if counts_2["squid nigiri"] > 0:
        prev_score_2 += counts_2["squid nigiri"] * 3
    
    # salmon nigiri
    if counts_1["salmon nigiri"] > 0:
        prev_score_1 += counts_1["salmon nigiri"] * 2
    if counts_2["salmon nigiri"] > 0:
        prev_score_2 += counts_2["salmon nigiri"] * 2

    # egg nigiri
    if counts_1["egg nigiri"] > 0:
        prev_score_1 += counts_1["egg nigiri"]
    if counts_2["egg nigiri"] > 0:
        prev_score_2 += counts_2["egg nigiri"]
    
    # fix if has more than 5 dumplings
    if counts_1["dumpling"] > 5:
        counts_1["dumpling"] = 5
    if counts_2["dumpling"] > 5:
        counts_2["dumpling"] = 5
    
    prev_score_1 += dumpling_values[counts_1["dumpling"]]
    prev_score_2 += dumpling_values[counts_2["dumpling"]]
    
    hold_1.clear()
    hold_2.clear()
    
    if round != 3:
        for i in range(puddings_1):
            hold_1.append("pudding")
        for i in range(puddings_2):
            hold_2.append("pudding")
    return hold_1, hold_2, prev_score_1, prev_score_2