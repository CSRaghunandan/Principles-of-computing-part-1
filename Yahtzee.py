"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    scores = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0}
    
    # score the hand
    for die_value in hand:
        scores[str(die_value)] += int(die_value)
    
    # return the maximum of the scores
    return max(scores.values())


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    
    # get all the possible outcomes of rolling the die based on the
    # number of sides of the die
    outcomes = []
    for item in range(1, num_die_sides + 1):
        outcomes.append(str(item))
    
    # generate all the sequences of rolls
    all_rolls = gen_all_sequences(outcomes, num_free_dice)
    
    current_score = 0
    for roll in all_rolls:
        current_score += score(held_dice + roll)
        
    return current_score / float(len(all_rolls))
    

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    
    answer_set = set([()])
    for dice_value in hand:
        for partial_sequence in set(answer_set):
            temp = tuple(sorted(list(partial_sequence) + [dice_value]))
            answer_set.add(temp)
                
    return answer_set


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    
    # generate all possible holds from the given hand configuration
    all_holds = gen_all_holds(hand)
    
    max_expected_value = 0
    best_choice_hold = ()
    
    for holds in all_holds:
        # get the expected value of the current hold and 
        # compare with the maxium expected value
        holds_expected_value = expected_value(holds, num_die_sides,len(hand) - len(holds))
        if max_expected_value < holds_expected_value:
            max_expected_value = holds_expected_value
            best_choice_hold = holds
    # return the maxium expected value and the best choice to hold
    return (max_expected_value, best_choice_hold)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
#run_example()

#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)                                
