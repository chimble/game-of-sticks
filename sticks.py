def choose_number():
    while True:
        number = input("Please choose 1 to 3 sticks to remove. ")
        if number in ['1', '2', '3']:
            return int(number)
        else:
            continue

def initial_sticks():
    num_sticks = input("Choose a number of sticks ")
    return int(num_sticks)

def current_sticks(initial_sticks, chosen_numbers):
    current_count = initial_sticks - chosen_numbers
    return current_count

def possible_stick_nums(num_sticks):
    return range(num_sticks)

def ai_choice(stick_count, information):

    random.choice()


def main():
    information = 
    print("Welcome to the Game of Sticks!")
    turn_counter = 0
    chosen_numbers = 0
    num_sticks = initial_sticks()
    hatlist = possible_stick_nums(num_sticks)
    information =
    print("There are {} sticks on the board.".format(num_sticks))
    while True:
        if (turn_counter + 1) % 2 == 1:
            print("It's your turn, Player 1")
            number = choose_number()
            chosen_numbers += number
            stick_count = current_sticks(num_sticks, chosen_numbers)
            turn_counter += 1
            print("There are {} sticks left".format(stick_count))
            if stick_count <= 0:
                print("You lose! Player 2 WINS!")
                break
        elif (turn_counter + 1) % 2 == 0:
            print("It's your turn, Player 2")
            number = choose_number()
            chosen_numbers += number
            stick_count = current_sticks(num_sticks, chosen_numbers)
            turn_counter += 1
            print("There are {} sticks left".format(stick_count))
            if stick_count <= 0:
                print("You lose! Player 1 WINS!")
                break

main()
