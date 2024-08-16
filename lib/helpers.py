from models.coach import Coach
from models.athlete import Athlete

def exit_program(conn):
    conn.close()
    print("Goodbye!")

def create_coach(cursor):
    name = input("Enter coach's name: ")
    experience_years = input("Enter years of experience: ")
    try:
        coach = Coach.create(name, int(experience_years))
        print(coach)
    except Exception as e:
        print(f"Error: {e}")

def create_athlete(cursor):
    name = input("Enter athlete's name: ")
    sport = input("Enter athlete's sport: ")
    coach_id = input("Enter coach's ID: ")
    try:
        athlete = Athlete.create(name, sport, int(coach_id))
        print(athlete)
    except Exception as e:
        print(f"Error: {e}")

def delete_coach(cursor):
    id_ = input("Enter coach's ID to delete: ")
    try:
        coach = Coach.find_by_id(int(id_))
        if coach:
            coach.delete()
            print(f"Coach {id_} deleted.")
        else:
            print(f"Coach {id_} not found.")
    except ValueError:
        print("Invalid ID entered.")

def delete_athlete(cursor):
    id_ = input("Enter athlete's ID to delete: ")
    try:
        athlete = Athlete.find_by_id(int(id_))
        if athlete:
            athlete.delete()
            print(f"Athlete {id_} deleted.")
        else:
            print(f"Athlete {id_} not found.")
    except ValueError:
        print("Invalid ID entered.")

def display_all_coaches(cursor):
    coaches = Coach.get_all()
    if coaches:
        for coach in coaches:
            print(coach)
    else:
        print("No coaches found.")

def display_all_athletes(cursor):
    athletes = Athlete.get_all()
    if athletes:
        for athlete in athletes:
            print(athlete)
    else:
        print("No athletes found.")

def view_coach_athletes(cursor):
    coach_id = input("Enter coach's ID to view their athletes: ")
    try:
        coach = Coach.find_by_id(int(coach_id))
        if coach:
            athletes = coach.athletes()
            if athletes:
                for athlete in athletes:
                    print(athlete)
            else:
                print(f"No athletes found for coach {coach_id}.")
        else:
            print(f"Coach {coach_id} not found.")
    except ValueError:
        print("Invalid ID entered.")

def find_coach_by_id(cursor):
    id_ = input("Enter coach's ID: ")
    try:
        coach = Coach.find_by_id(int(id_))
        if coach:
            print(coach)
        else:
            print(f"Coach {id_} not found.")
    except ValueError:
        print("Invalid ID entered.")

def find_athlete_by_id(cursor):
    id_ = input("Enter athlete's ID: ")
    try:
        athlete = Athlete.find_by_id(int(id_))
        if athlete:
            print(athlete)
        else:
            print(f"Athlete {id_} not found.")
    except ValueError:
        print("Invalid ID entered.")
