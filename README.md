# Roster Management CLI Application

## Overview

The Roster Management CLI Application is a Python-based command-line interface (CLI) that allows users to manage a roster of coaches and athletes. The application leverages a SQLite database and an Object-Relational Mapping (ORM) approach to handle data management. Users can create, update, delete, and view both coaches and athletes, with athletes being associated with a specific coach.

## Features

- Manage Coaches: Create, view, delete, and search for coaches.

- Manage Athletes: Create, view, delete, and search for athletes, with each athlete linked to a specific coach.

- One-to-Many Relationship: Each coach can have multiple athletes, demonstrating a one-to-many relationship.

- User Input Validation: The CLI validates user input to prevent errors and ensure data integrity.

## Requirements

### ORM Requirements

- Database creation and modification with Python ORM methods.

- Two model classes: Coach and Athlete.

- One-to-many relationship between Coach and Athlete.

- Property methods to add constraints to model classes.

- ORM methods for creating, deleting, retrieving all, and finding objects by ID.

### CLI Requirements

- Interactive CLI with menus for user selection.

- Looping mechanism to keep the user in the application until they choose to exit.

- Options for each model class to create, delete, display all, view related objects, and find by attribute.

- Input validation and error handling to guide the user.

### Project Environment, Configuration, and Documentation

- The code follows OOP best practices.

- A Pipfile manages project dependencies.

- Imports are used only where necessary.

- The project structure follows organized and meaningful naming conventions.

- Includes this README file describing the application.
## Setup and Installation

### Prerequisites

- Python 3.8.13

- SQLite

## Installation

1. Clone the repository:

```bash
git clone https://github.com/abrahamscott02/python-p3-v2-final-project-template.git
cd roster-management-cli
```
2. Install the dependencies:

```bash
pipenv install
```
3. Run the application:

```bash
pipenv run python cli.py
```

## Usage

Upon running the application, you will be presented with a menu of options to manage coaches and athletes. Select an option by entering the corresponding number. After executing an operation, press Enter to return to the main menu.

### Example Commands

- Create a Coach: Enter the coach's name and years of experience.
- Create an Athlete: Enter the athlete's name, sport, and coach ID.

- View all Coaches/Athletes: Display a list of all coaches or athletes.

- Find by ID: Look up a coach or athlete by their unique ID.

- View Athletes of a Coach: Display all athletes associated with a particular coach.