from models.coach import Coach
from models.athlete import Athlete
import os


import sqlite3
from helpers import (
    create_coach,
    create_athlete,
    delete_coach,
    delete_athlete,
    display_all_coaches,
    display_all_athletes,
    view_coach_athletes,
    find_coach_by_id,
    find_athlete_by_id,
    exit_program
)

# Initialize database connection
CONN = sqlite3.connect('roster.db')
CURSOR = CONN.cursor()

Coach.create_table()
Athlete.create_table()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create a Coach")
    print("2. Create an Athlete")
    print("3. Delete a Coach")
    print("4. Delete an Athlete")
    print("5. Display all Coaches")
    print("6. Display all Athletes")
    print("7. View Athletes of a Coach")
    print("8. Find Coach by ID")
    print("9. Find Athlete by ID")

def main():
    result = ''
    while True:
        clear_screen()
        menu()
        choice = input("> ")

        if choice == "0":
            exit_program(CONN)
            break

        elif choice == "1":
            create_coach(CURSOR)

        elif choice == "2":
            create_athlete(CURSOR)

        elif choice == "3":
            delete_coach(CURSOR)

        elif choice == "4":
            delete_athlete(CURSOR)

        elif choice == "5":
            display_all_coaches(CURSOR)

        elif choice == "6":
            display_all_athletes(CURSOR)

        elif choice == "7":
            view_coach_athletes(CURSOR)

        elif choice == "8":
            find_coach_by_id(CURSOR)

        elif choice == "9":
            find_athlete_by_id(CURSOR)

        else:
            print("Invalid choice")

        print("\n" + result)
        input("\nPress Enter to return to the menu...")

if __name__ == "__main__":
    main()
