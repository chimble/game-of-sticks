def choose_number():
    while True:
        number = input("Please choose 1 to 3 sticks to remove.")
        if number in ['1', '2', '3']:
            return int(number)
        else:
            continue

def initial_sticks():
    return 20

def current_sticks(initial_sticks, chosen_numbers):
    current_count = initial_sticks - chosen_numbers
    return current_count

def main():
    print("Welcome to the Game of Sticks!")
    turn_counter = 0
    chosen_numbers = 0
    num_sticks = initial_sticks()
    while True:
        if (turn_counter + 1) % 2 == 1:
            print("It's your turn, Player 1")
            number = choose_number()
            chosen_numbers += number
            stick_count = current_sticks(num_sticks, chosen_numbers)
            turn_counter += 1
            print("There are {} sticks left".format(stick_count))
        elif (turn_counter + 1) % 2 == 0:
            print("It's your turn, Player 2")
            number = choose_number()
            chosen_numbers += number
            stick_count = current_sticks(num_sticks, chosen_numbers)
            turn_counter += 1
            print("There are {} sticks left".format(stick_count))
    return chosen_numbers

main()
