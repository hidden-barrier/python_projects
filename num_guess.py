import random

def num_generator():
    """
    function that generates a random integer from 0 to 36
    """
    num = random.randint(0, 36)
    return num

def main():
    """
    main function for random number guessing game
    """
    playing_game = True

    while playing_game:
        num = num_generator()
        attempts = 5 #number of trials
        print('Welcome to the number guessing game')
        print(f'you have {attempts} attempts to guess the number from 0 to 36')

        while attempts > 0:
            guess = input('Enter guess: ')
            try:
                #checking if the user entered a number and converting it to a string
                guess = int(guess)
            
            except:
                #restarts the guess process
                print('Invalid input')
                continue
            if guess == num:
                print('You Win!')
                break

            elif guess < num:
                print('The number is low')

            else:
                print('The number is high')
            
            attempts -= 1
            print(attempts)
            if attempts > 0:
                print(f'You have {attempts} remaining')
            else:
                print(f'You have run out of attempts the correct number was {num}')
        play_again = input('Do you want to guess again(yes/no): ').strip().lower()
        if play_again != 'yes':
            print('Thanks for playing Good Bye!')
            playing_game = False

if __name__ == '__main__':
    main()