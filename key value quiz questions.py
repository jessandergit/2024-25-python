from random import *

# Set up the question bank
question_bank = {
    'The area of Texas': 'The area of France',
    'A Zettabyte': 'An Exabyte',
    'Mars': 'Mercury',
    'Population of Austria': 'Population of Switzerland',
    'Common seal': 'Labrador dog',
    'GDP of India': 'GDP of the UK',
    'Number of kinds of bee': 'Number of kinds of bat',
    'Jupiter': 'All the other planets put together',
    'Words in the works of Shakespeare': 'Words in the Bible',
    'Number of bees on Earth': 'Number of stars in our galaxy'
}

def show_flashcard():
    """ Show the user a random key and ask them
        to define it. Show the definition
        when the user presses return.    
    """
    # DO NOT ALTER THE NEXT LINE
    global score_count

    # MAKE YOUR CHANGES BETWEEN HERE AND THE END OF THE show_flashcard() FUNCTION
    
    #>> show a question
    #select a random key-value pair, with key being bigger and value being smaller
    items = list(question_bank.items())
    big, small = choice(items)
    
    #randomly choose whether to present question as (big, small) or (small, big)
    if choice([True, False]):
        option_a, option_b = big, small
    else:
        option_a, option_b = small, big
    
    #label the items in order of A, B.
    print("Which is bigger?")
    print("A.", option_a)
    print("B.", option_b)
    
    #>> check the user’s answer
    user_choice = input("Enter A or B: ")
    
    if (user_choice == "A" and option_a == big) or (user_choice == "B" and option_b == big):
        #if correct: inform user & increase score by 1
        print("Thats correct.")
        score_count += 1
        #if the user enters the values without capital letters they will still be correct
    elif (user_choice == "a" and option_a == big) or (user_choice == "b" and option_b == big):
        print("Thats correct.")
    else:
        #if incorrect: inform user & increase score by 0
        print("That is incorrect.")

#interactive loop
score_count = 0
exit_game = False

while not exit_game:
    #>> repeat/exit
    #input s to continue, q to quit
    user_input = input('Enter “s” to show a question, or “q” to quit:  ')
    if user_input == 'q':
        exit_game = True
    elif user_input == 's':
        show_flashcard()
    else:
        print('You need to enter either “q” or “s”.')

print('Number of correct answers:', score_count)
