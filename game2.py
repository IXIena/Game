import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def get_user_name():
    name = input("Enter your astronaut name: ")
    return name

def introduction(name):
    print_slow(f"Welcome, astronaut {name}! You are stationed on the research outpost Perseus, orbiting Nexus-9.")
    print_slow("Your mission is to investigate anomalies and manifestations around Nexus-9.")
    print_slow("Be cautious, as the planet seems to respond to thoughts and memories.")
    print_slow("You wake up in your quarters. It's eerily silent.")

def explore_station():
    print_slow("\nYou decide to explore the research outpost.")
    print_slow("As you walk down the corridor, you notice a flickering light in the control room.")
    time.sleep(2)
    print_slow("\nWhat do you want to do?")
    print_slow("1. Investigate the flickering light.")
    print_slow("2. Go to the observation deck.")

def investigate_light():
    print_slow("\nYou cautiously approach the control room.")
    print_slow("Inside, you see holographic projections swirling around.")
    time.sleep(2)
    print_slow("\nTwo doors appear in front of you.")
    print_slow("1. Approach the holographic projections.")
    print_slow("2. Check the computer logs.")

def confrontation():
    print_slow("\nYou feel a sudden surge of memories flooding your mind.")
    print_slow("Strange illusions begin to form around you.")
    time.sleep(2)
    print_slow("\nWhat will you do?")
    print_slow("1. Try to confront the illusions.")
    print_slow("2. Attempt to ground yourself and focus on reality.")

def main_game():
    user_name = get_user_name()
    introduction(user_name)

    explore_station_choice = input("\nDo you want to explore the station? (yes/no): ").lower()
    if explore_station_choice == "yes":
        explore_station()
        station_option = input("\nEnter your choice (1/2): ")

        if station_option == "1":
            investigate_light()
            light_option = input("\nEnter your choice (1/2): ")

            if light_option == "1":
                confrontation()
                # Continue game based on the final choice
                # Add more story prompts or outcomes here based on player's choices
            elif light_option == "2":
                print("\nYou access the computer logs and find some intriguing data.")
                # Continue game based on the chosen path
        elif station_option == "2":
            print("\nYou reach the observation deck and witness breathtaking cosmic phenomena.")
            # Continue game based on the chosen path
    else:
        print("\nYou decide to stay in your quarters.")
        # Continue game based on the chosen path

if __name__ == "__main__":
    main_game()