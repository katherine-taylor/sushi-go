# game_play.py
# Katherine Taylor
# 2022-01-16

# libaries
import functions as func
import random
import pandas as pd
import copy
# main
# set seed
random.seed(48259)
# load game data
game_data = pd.read_csv("data/card_data.csv", delimiter="\t")
cards = dict(zip(game_data["card_name"],game_data["amount"]))
dumpling_values = [0,1,3,6,10,15]
sim_save = []
for i in range(1000):
    cards = dict(zip(game_data["card_name"],game_data["amount"]))
    # round 1
    hand_1, hand_2, c_r = func.deal_round(cards)
    hold_1, hold_2 = func.play_round(hand_1, hand_2, [],[])
    round_1_dict = {"run":i+1,"round":1, "hold_1" : copy.deepcopy(hold_1), "hold_2" : copy.deepcopy(hold_2)}
    new_hold_1, new_hold_2, score_1, score_2 = func.score_round(1, hold_1, hold_2, 0,0, dumpling_values)
    round_1_dict["score_1"] = score_1
    round_1_dict["score_2"] = score_2
    sim_save.append(round_1_dict)
    # round 2
    hand_3, hand_4, c_r2 = func.deal_round(c_r)
    hold_3, hold_4 = func.play_round(hand_3, hand_4, new_hold_1, new_hold_2)
    round_2_dict = {"run":i+1,"round":2, "hold_1" : copy.deepcopy(hold_3), "hold_2" : copy.deepcopy(hold_4)}
    new_hold_3, new_hold_4, score_3, score_4 = func.score_round(2, hold_3, hold_4, score_1,score_2, dumpling_values)
    round_2_dict["score_1"] = score_3
    round_2_dict["score_2"] = score_4
    sim_save.append(round_2_dict)
    # round 3
    hand_5, hand_6, c_r3 = func.deal_round(c_r2)
    hold_5, hold_6 = func.play_round(hand_5, hand_6, new_hold_3, new_hold_4)
    round_3_dict = {"run":i+1,"round":3, "hold_1" : copy.deepcopy(hold_5), "hold_2" : copy.deepcopy(hold_6)}
    new_hold_5, new_hold_6, score_5, score_6 = func.score_round(3, hold_5, hold_6, score_3,score_4, dumpling_values)
    round_3_dict["score_1"] = score_5
    round_3_dict["score_2"] = score_6
    sim_save.append(round_3_dict)
    print("Run",i+1,"completed")

results = pd.DataFrame(sim_save)
pd.DataFrame.to_csv(results,"data/sim_results.csv")