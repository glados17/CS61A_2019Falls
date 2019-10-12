"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    results = []
    for paragraph in paragraphs:
        if select(paragraph):
            results.append(paragraph)
        if len(results) == k+1:
            return results[k]
    return ''
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def select_about(paragraph):
        # para = lower(remove_punctuation(paragraph))
        # para = lower(para)
        for words in topic:
            if words in split(lower(remove_punctuation(paragraph))):
                return True
        return False
    return select_about
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if len(typed_words) == 0:
        return 0.00
    correct_count = 0
    for word_index in range(min(len(typed_words),len(reference_words))):
        if typed_words[word_index] == reference_words[word_index]:
            correct_count += 1
    return correct_count*100. / len(typed_words)



    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return len(typed) / 5 / elapsed *60. 
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if user_word in valid_words:
        return user_word

    result_word = user_word
    diff = limit + 1
    for word in valid_words:
        diff_now = diff_function(user_word,word,limit)
        if diff_now <= limit and diff_now < diff:
            diff, result_word = diff_now, word
    return result_word
    # END PROBLEM 5


def swap_diff(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    # assert False, 'Remove this line'

    ### First I try to use a helper function to calculate limit exceeding, it works
    ### but when I come to the edit_diff, it became unclear, then the next one come out

    # min_len = min(len(start), len(goal))-1
    # def diff_helper(sum_diff, n):
    #     if n > min_len or sum_diff > limit:
    #         return sum_diff
    #     elif start[n] != goal[n]:
    #         return diff_helper(sum_diff+1, n+1)
    #     else:
    #         return diff_helper(sum_diff, n+1)
    # return diff_helper(0,0) + abs(len(start) - len(goal))

    if len(start) == 0 or len(goal) == 0:
        return abs(len(start) - len(goal))
    elif limit < 0:
        return 1
    elif start[0] != goal[0]:
        diff = swap_diff(start[1:], goal[1:],limit-1) + 1
        # if diff > limit:
        #     return limit + 1
    else:
        diff = swap_diff(start[1:], goal[1:],limit) 
    return diff

    ## This is a solution using iteration instead of recursion
    # min_len = min(len(start),len(goal))
    # diff = 0 
    # for word_index in range(min_len):
    #     if start[word_index] != goal[word_index]:
    #         diff += 1
    #     if diff > limit:
    #         return diff
    # return diff + abs(len(start) - len(goal))

    # END PROBLEM 6

def edit_diff(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    # assert False, 'Remove this line'
    if len(start) == 0 or len(goal) == 0: # Fill in the condition
        # BEGIN
        return max(len(goal),len(start))
        # END
    elif limit < 0:
        return 1

    elif start[-1] == goal[-1]: # Feel free to remove or add additional cases
        # BEGIN
        return edit_diff(start[:-1], goal[:-1], limit)
        # END
    else:
        # BEGIN
        "*** YOUR CODE HERE ***"
        add_diff = edit_diff(start, goal[:-1], limit-1) # Fill in these lines
        remove_diff = edit_diff(start[:-1], goal, limit-1) 
        substitute_diff = edit_diff(start[:-1], goal[:-1], limit-1) 
        diff = min(add_diff, remove_diff, substitute_diff)
        return diff + 1
        # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'




###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    correct_count = 0
    for word_index in range(min(len(typed),len(prompt))):
        if typed[word_index] == prompt[word_index]:
            correct_count += 1
        else:
            break
    progress_now = correct_count / len(prompt)
    send({'id': id, 'progress': progress_now})
    return progress_now
    # END PROBLEM 8


def fastest_words_report(word_times):
    """Return a text description of the fastest words typed by each player."""
    fastest = fastest_words(word_times)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def fastest_words(word_times, margin=1e-5):
    """A list of which words each player typed fastest."""
    n_players = len(word_times)
    n_words = len(word_times[0]) - 1
    assert all(len(times) == n_words + 1 for times in word_times)
    assert margin > 0
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"

    def get_time_resuming(word_times,player,word_togo):
        return word_time(word(word_times[player][word_togo]),
                        elapsed_time(word_times[player][word_togo])
                         - elapsed_time(word_times[player][word_togo-1]))
    
    def get_resuming_words(word_times,n_players,n_words):
        result = [[] for x in range(n_players)]
        for player in range(n_players):
            for word_togo in range(1,n_words+1):
                result[player].append(get_time_resuming(word_times,player,word_togo))
        return result
    
    def get_n_word(word_times,n):
        return [row[n] for row in word_times]
    
    def get_min_word_col(word_col):
        return min([elapsed_time(word_time) for word_time in word_col])

    time_resuming_words = get_resuming_words(word_times,n_players,n_words)
    result =  [[] for x in range(n_players)]
    for word_togo in range(n_words):
        nth_word_time_col = get_n_word(time_resuming_words,word_togo)
        min_time = get_min_word_col(nth_word_time_col)
        for player in range(n_players):
            if elapsed_time(time_resuming_words[player][word_togo]) - min_time < margin:
                result[player].append(word(time_resuming_words[player][word_togo]))
    return result




    # END PROBLEM 9
    
def word_time(word, elapsed_time):
    """A data abstrction for the elapsed time that a player finished a word."""
    return [word, elapsed_time]


def word(word_time):
    """An accessor function for the word of a word_time."""
    return word_time[0]


def elapsed_time(word_time):
    """An accessor function for the elapsed time of a word_time."""
    return word_time[1]


enable_multiplayer = False  # Change to True when you


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)