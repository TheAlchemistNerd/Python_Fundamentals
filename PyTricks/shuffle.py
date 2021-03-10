from random import shuffle
from time import time

def shuffle_arrays():
    """ This function function implements monte carlo method of simulation.
        It shuffles a deck of 52 cards and returns probability of one card
        remaining in place   
    """
    total_arrays = 0 # Arrays with atleast one unmoved element after shuffling
    for trial in range(TRIAL_RUNS):
        array = list(range(LIST_SIZE))
        shuffle(array)
        for num in range(LIST_SIZE):
            if array[num] == num:
                total_arrays += 1
                break
    probability = round(total_arrays/TRIAL_RUNS, 2)
    return probability

def print_result(probability):
    """ This function takes the probability as an argument 
        and returns the formatted output to the console. 
    """
    print('Result:', probability, 'is the probability of an array having\
    at \nleast one unmoved element after shuffling. This is based \non a\
    computer simulation with an array size = ',
    LIST_SIZE, 'and ', TRIAL_RUNS, 'trial runs.')

TRIAL_RUNS = 1000000
LIST_SIZE = 52
assert LIST_SIZE > 1    # LIST_SIZE must be greater than 1.

def main():
    probability = shuffle_arrays()
    print_result(probability)

if __name__ == '__main__':
    START_TIME = time()
    main()
    print('\n  '+'- '*12)
    print('PROGRAM RUN TIME :%6.2f'%(time()-START_TIME),
    'seconds.')