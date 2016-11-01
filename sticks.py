def choose_number():
    number = 2 #input()
    while True:
        if number in [1, 2, 3]:
            return number
        else:
            print("Please choose 1 to 3 sticks to remove")

def initial_sticks():
    return 20

def current_sticks(initial_sticks, chosen_numbers):
    current_count = initial_sticks - chosen_numbers
    return current_count

def main():
    turn_counter = 0
    chosen_numbers = 0
    num_sticks = initial_sticks()
    number = choose_number()
    chosen_numbers += number
    current_sticks(num_sticks, chosen_numbers)
    return chosen_numbers
