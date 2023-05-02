from ten_thousand.game_logic import GameLogic
import sys

calculator = GameLogic.calculate_score
total_score = 0
roll = GameLogic.roll_dice
validate_keepers = GameLogic.validate_keepers

def play(roller=GameLogic.roll_dice):
    global roll
    roll = roller
#         1 function welcome yes or no input
#           return answer
    print("Welcome to Ten Thousand\n(y)es to play or (n)o to decline")
    user_input = input("> ")
    if user_input == "y":
        start_round()
            ## anything else will quit
    elif user_input == "n":
        quitter()

def quitter():
    print("OK. Maybe another time")

def start_round(round=1, number_of_dice=6, new_total_score=total_score, unbanked_score=0, set_of_dice=0):
    print("Starting round {}".format(round))
    set_of_dice = start_rolling(number_of_dice, round, new_total_score, unbanked_score)
    if input_check_for_cheating(set_of_dice, number_of_dice, new_total_score, round, unbanked_score) == "cheater":
        print("stop")
    else:
        pass

def start_rolling(number_of_dice, round, new_total_score, unbanked_score):
    print("Rolling {} dice...".format(number_of_dice))
    rolling_dice = roll(number_of_dice)
    unpacked_dice = " ".join(str(x) for x in rolling_dice)
    print("*** {} ***".format(unpacked_dice))
    if calculator(rolling_dice) == 0:
        unbanked_points = 0
        zelch(round, unbanked_points, new_total_score)
    else:
        set_of_dice = rolling_dice
        input_check_for_cheating(set_of_dice, number_of_dice, new_total_score, round, unbanked_score)

def zelch(round, unbanked_score, new_total_score):
    print("****************************************")
    print("**        Zilch!!! Round over         **")
    print("****************************************")
    print("You banked {} points in round {}".format(unbanked_score, round))
    round +=1
    print("Total score is {} points".format(new_total_score))
    start_round(round, number_of_dice=6, new_total_score=total_score)

def input_check_for_cheating(set_of_dice, number_of_dice, new_total_score, round, unbanked_score):
    print("Enter dice to keep, or (q)uit:")
    user_input = input("> ")
    user_input = user_input.replace(" ", "")
    if user_input == "q":
        quit(new_total_score)
    else:
        list_from_user = [int(x) for x in user_input]
        unpacked_dice = " ".join(str(x) for x in set_of_dice)  
        if validate_keepers(set_of_dice, list_from_user) == False:
                print("Cheater!!! Or possibly made a typo...")
                print("*** {} ***".format(unpacked_dice))
                input_check_for_cheating(set_of_dice, number_of_dice, new_total_score, round, unbanked_score)
        else:
            if len(list_from_user) == len(set_of_dice) and calculator(list_from_user) == 1500:
                unbanked_score += 1500
                number_of_dice = 6
                unbanked_score_options(unbanked_score, number_of_dice, new_total_score, round)
            if len(list_from_user) == len(set_of_dice):
                unbanked_score += calculator(list_from_user)
                banking(round, new_total_score, unbanked_score, number_of_dice)
            else:
                unbanked_score += calculator(list_from_user)
                new_number_of_dice = number_of_dice - len(list_from_user)
                unbanked_score_options(unbanked_score, new_number_of_dice, new_total_score, round)

def unbanked_score_options(unbanked_score, new_number_of_dice, new_total_score, round):
    print("You have {} unbanked points and {} dice remaining".format(unbanked_score, new_number_of_dice))
    print("(r)oll again, (b)ank your points or (q)uit:")
    user_input = input("> ")
    if user_input == "r":
        start_rolling(new_number_of_dice, round, new_total_score, unbanked_score)
    elif user_input == "b":
        banking(round, new_total_score, unbanked_score, new_number_of_dice)
    else:
        quit(new_total_score)

def banking(round, new_total_score, unbanked_score, number_of_dice):
#            5 function banking store print total score store and starts round function
    new_total_score += unbanked_score
    number_of_dice = 6
    print("You banked {} points in round {}\nTotal score is {} points".format(unbanked_score, round, new_total_score))
    round += 1
    start_round(round, number_of_dice, new_total_score, unbanked_score=0)
        
def quit(new_total_score):
#           total points is not supposed to be static it should be from a return value
    print("Thanks for playing. You earned {} points".format(new_total_score))
    sys.exit()

if __name__ == "__main__":
    play()