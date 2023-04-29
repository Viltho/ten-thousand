from game_logic import GameLogic

calculator = GameLogic.calculate_score
total_score = 0
roll = GameLogic.roll_dice
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

def start_round(round = 1, new_total_score = total_score, dice_count = 6):
#           2 start round function
#           variable <= 20
#           **care of how many dice i need to roll**
#           out put of this function is a tuple of remaining dice
  
        six_dice = roll(dice_count)
        unpacked_dice = " ".join(str (x) for x in six_dice)
        print("Starting round {}\nRolling {} dice...\n*** {} ***".format(round, dice_count, unpacked_dice))
        if calculator(six_dice) == 0 or dice_count == 0:
            print("You lost your turn")
            round += 1
            # start_round(round, new_total_score, dice_count)
        else:
            print("Enter dice to keep, or (q)uit:")
            user_input = input("> ")
            if user_input == "q" and dice_count != 0:
                quit(new_total_score)
            elif not isinstance(int(user_input), (int)):
                print("Cheating ?")
            else:
                kept_dices = tuple(int (x) for x in user_input)
                if set(kept_dices).intersection(set(six_dice)):
                    dice_count = dice_count - len(kept_dices)
                    score = calculator(kept_dices)
                    # total_score = total_score + score
                    print("You have {} unbanked points and {} dice remaining".format(score, dice_count))
                    print("(r)oll again, (b)ank your points or (q)uit:")
                    user_choice = input("> ")
                    if user_choice == "q":
                        quit(new_total_score)
                    elif user_choice == "r":
                        new_total_score += score
                        start_round(round, new_total_score, dice_count)
                    elif user_choice == "b":
                        new_total_score += score
                        banking(score, round, new_total_score)
                else:
                    print("You are cheating")

def banking(score, round, new_total_score):
#            5 function banking store print total score store and starts round function
        print("You banked {} points in round {}\nTotal score is {} points".format(score, round, new_total_score))
        round += 1
        start_round(round, new_total_score)
        
def quit(new_total_score):
#           total points is not supposed to be static it should be from a return value
        print("Thanks for playing. You earned {} points".format(new_total_score))

if __name__ == "__main__":
    play()