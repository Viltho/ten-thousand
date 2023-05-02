import random
from collections import Counter

class GameLogic():
    def __init__(self):
        pass

    @staticmethod
    def roll_dice(rdt):
        times = 0
        arr_times = []
        while True:
            if times != rdt and rdt <= 6 and rdt > 0:
                rolled_dice = random.randint(1,6)
                arr_times.append(rolled_dice)
                times += 1
            else:
                break
        tuple_times = tuple(arr_times)
        return tuple_times
    
    def calculate_score(roll_dice):
        sum = 0
        count_result = Counter(roll_dice)
        most_common = count_result.most_common()
        if len(most_common) == 6:
            sum += 2000
            return sum
        ## ChatGPT helped in all(count == 2 for _, count in most_common) in the following line which determines the count of the element to be exactly 2 in most_common ###
        elif len(most_common) == 3 and all(count == 2 for _, count in most_common):
            sum += 1500
            return sum
        
        else:
            for item in most_common:
                if item[0] == 1 and item[1] < 3: ##[(1, 2), ]
                    sum += 100 * item[1]
                if item[0] == 1 and item[1] == 3:
                    sum += 1000
                if item[0] == 1 and item[1] == 4:
                    sum += 2000
                if item[0] == 1 and item[1] == 5:
                    sum += 4000
                if item == (1, 6):
                    sum += 8000
                if item[0] == 5 and item[1] < 3:
                    sum += 50 * item[1]
                if item[1] == 2: ## [(2, 2), (3, 2), (4, 2), (6, 2)]
                    sum += 0
                if item[1] == 3 and item[0] != 1:
                    sum += 100 * item[0]
                if item[1] == 4 and item[0] != 1:
                    sum += 200 * item[0]
                if item[1] == 5 and item[0] != 1:
                    sum += 400 * item[0]
                if item[1] == 6 and item[0] != 1:
                    sum += 800 * item[0]
            return sum
        
    def get_scorers(roll_dice):
        main_score = GameLogic.calculate_score(roll_dice)
        scorers = []
        input_list = list(roll_dice)
        for i, val in enumerate(input_list):
            input_list.pop(i)
            element_score = GameLogic.calculate_score(tuple(input_list))
            if element_score != main_score:
                scorers.append(val)
                input_list.insert(i,val)
            else:
                input_list.insert(i, val)
        scorers_tuple = tuple(scorers)
        return scorers_tuple

    def validate_keepers(roll, keepers):
        roll= list(roll)
        for elem in keepers:
            if elem not in roll:
                return False
            else:
                roll.pop(roll.index(elem))
        return True
            
    

# after_input_ofdice = GameLogic.roll_dice(6)
# after_calculating_score = GameLogic.calculate_score(after_input_ofdice)

# # print(after_input_ofdice)
# print(after_calculating_score)
