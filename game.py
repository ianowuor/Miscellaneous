# Importing useful libraries
from tkinter import *
import random
import time

# Setting the main window
root = Tk()
root.title("Dice Quiz")
root.geometry("1100x600")

# Start Game Screen
welcome_label = Label(root, text="Welcome to Dice Quiz, a fun quiz game     ", font='Arial 24')
welcome_label.grid(column=0, row=0, sticky=W)

title_label = Label(root, text="                        How to Play                         ", font="Arial 24 underline")
title_label.grid(column=0, row=1, pady=20, padx=0, sticky=W)

# Instructions on how to play the game
instruction1 = Label(root, text="In this game six randomly selected multiple-choice questions will be presented to you", font="Arial 15")
instruction1.grid(column=0, row=2, sticky=W)
instruction2 = Label(root, text="You will click the Role Dice button below the questions", font="Arial 15")
instruction2.grid(column=0, row=3, sticky=W)
instruction3 = Label(root, text="The outcome of the dice roll will be the question you have to answer from the set of the six pre-selected questions", font="Arial 15")
instruction3.grid(column=0, row=4, sticky=W)
instruction4 = Label(root, text="Once a question has been determined you have to select the correct answer from the choices given", font="Arial 15")
instruction4.grid(column=0, row=5, sticky=W)
instruction5 = Label(root, text="Every correct answer earns you 5 points. A wrong answer earns you no points", font="Arial 15")
instruction5.grid(column=0, row=6, sticky=W)
instruction6 = Label(root, text="Press the START GAME button below to start playing", font="Arial 15")
instruction6.grid(column=0, row=7, sticky=W)

# Variable to keep track of points earned
points = 0

# Variable to keep track of dice roll
output = 0

# A list of Dictionaries to store all quiz questions and choices
quiz_questions = [
    {
        "question": "How many planets are in the Solar System?",
        "choice1": "10",
        "correct": "8",
        "choice2": "5",
        "choice3": "7"
    },
    {
        "question": "What is the name given to 23 and 1/2 degrees North latitude?",
        "choice1": "Tropic of Capricon",
        "choice2": "Greenwich Meridian",
        "correct": "Tropic of Cancer",
        "choice3": "Equator"
    },
    {
        "question": "Which is the largest country in Western Asia?",
        "choice1": "Iraq",
        "choice2": "Japan",
        "choice3": "Russia",
        "correct": "Saudi Arabia"
    },
    {
        "question": "Which is the longest river in North America?",
        "correct": "Mississippi-Missouri",
        "choice1": "Nile",
        "choice2": "Amazon",
        "choice3": "Congo"
    },
    {
        "question": "Which USA city is known as 'The Windy City'?",
        "choice1": "New York",
        "correct": "Chicago",
        "choice2": "Denver",
        "choice3": "Seattle"
    },
    {
        "question": "Which continent is just in North of Africa?",
        "choice1": "Antarctica",
        "choice2": "Asia",
        "correct": "Europe",
        "choice3": "Australia"
    },
    {
        "question": "Which is the largest country in Africa?",
        "correct": "Algeria",
        "choice1": "Sudan",
        "choice2": "South Africa",
        "choice3": "DRC"
    },
    {
        "question": "Which is the smallest continent?",
        "choice1": "Antarctica",
        "choice2": "Asia",
        "correct": "Australia",
        "choice3": "North America"
    },
    {
        "question": "What is the southernmost country in Africa?",
        "choice1": "Zimbabwe",
        "choice2": "Botswana",
        "choice3": "Lesotho",
        "correct": "South Africa"
    },
    {
        "question": "The South pole is in the middle of which continent?",
        "correct": "Antarctica",
        "choice1": "Asia",
        "choice2": "Europe",
        "choice3": "Australia"
    },
    {
        "question": "You are on the east coast of Argentina in South America. Which ocean do yo see?",
        "choice1": "The Pacific",
        "correct": "The Atlantic",
        "choice2": "The Indian Ocean",
        "choice3": "Arctic Ocean"
    },
    {
        "question": "Which country is also known as the 'Horn of Africa'?",
        "choice1": "Morocco",
        "choice2": "Egypt",
        "choice3": "Ethiopia",
        "correct": "Somalia"
    },
    {
        "question": "What is the highest point on Earth?",
        "choice1": "Mt. Kilimanjaro",
        "choice2": "Mt. Whitney",
        "correct": "Mt. Everest",
        "choice3": "Mt. Saint Elias"
    },
    {
        "question": "The Rift Valley is found on which continent?",
        "choice1": "Antarctica",
        "choice2": "Asia",
        "correct": "Africa",
        "choice3": "Australia"
    },
    {
        "question": "What kind of land form are the Himalayas?",
        "correct": "Mountains",
        "choice1": "Plateau",
        "choice2": "Valley",
        "choice3": "Plain"
    },
    {
        "question": "How many countries border China in Asia?",
        "choice1": "8",
        "choice2": "12",
        "correct": "13",
        "choice3": "11"
    },
    {
        "question": "What large island lies off the east coast of Africa?",
        "choice1": "Seychelles",
        "choice2": "Mauritius",
        "choice3": "Comoros",
        "correct": "Madagascar"
    },
    {
        "question": "Which of the following countries is the smallest by area?",
        "choice1": "Mexico",
        "correct": "kenya",
        "choice2": "Argentina",
        "choice3": "Niger"
    },
    {
        "question": "In what country is the famous Grand Canyon National Park?",
        "choice1": "Australia",
        "correct": "USA",
        "choice2": "Canada",
        "choice3": "Brazil"
    },
    {
        "question": "How many continents are there in the world?",
        "choice1": "8",
        "choice2": "5",
        "choice3": "9",
        "correct": "7"
    },
    {
        "question": "Which is the largest desert in the world?",
        "choice1": "Kalahari",
        "correct": "Sahara",
        "choice2": "Arabian Desert",
        "choice3": "Australian Desert"
    },
    {
        "question": "How many time zones does the world have?",
        "choice1": "10",
        "choice2": "20",
        "choice3": "18",
        "correct": "24"
    },
    {
        "question": "Which country is called the 'Land of the Rising Sun'?",
        "correct": "Japan",
        "choice1": "India",
        "choice2": "Phillipines",
        "choice3": "Nigeria"
    },
    {
        "question": "Which of the following is not a dwarf planet?",
        "choice1": "Ceris",
        "choice2": "Haumea",
        "correct": "Mercury",
        "choice3": "Pluto"
    },
    {
        "question": "Which is the tallest mountain in Africa?",
        "choice1": "Mt. Ruwenzori",
        "correct": "Mt. Kilimanjaro",
        "choice2": "Mt. Elgon",
        "choice3": "Mt. Kenya"
    },
    {
        "question": "Which is the deepest lake in the world?",
        "correct": "Lake Baikal",
        "choice1": "Lake Tanganyika",
        "choice2": "Lake Victoria",
        "choice3": "Great Slave Lake"
    },
    {
        "question": "What is the saltiest sea in the world?",
        "choice1": "The Red Sea",
        "choice2": "The Mediterranean Sea",
        "correct": "The Dead sea",
        "choice3": "The Caribbean Sea"
    },
    {
        "question": "How long does it take the earth to rotate around the sun?",
        "choice1": "365 Days",
        "correct": "24 Hours",
        "choice2": "12 Hours",
        "choice3": "20 hours"
    },
    {
        "question": "Which is the second most populous country in the world?",
        "choice1": "The USA",
        "choice2": "China",
        "choice3": "Russia",
        "correct": "India"
    },
    {
        "question": "The Taj Mahal is a large tomb located in which country?",
        "choice1": "Qatar",
        "choice2": "Cuba",
        "correct": "India",
        "choice3": "Iran"
    }
]

# Function to select 6 Random Questions
def select_questions():
    global quiz_questions
    selected_questions = []
    while len(selected_questions) <= 6:
        question = random.choice(quiz_questions)
        if question not in selected_questions:
            selected_questions.append(question)
        else:
            pass

    return selected_questions

# 6 Randomly Selected Questions
questions = select_questions()

# Tkinter string variable to store players choice
choice = StringVar()

# A Label for points
points_label = Label(root, text=f"Points : {points}", font='Arial 24', fg="green", bg="black")

# A title lable for questions
questions_label = Label(root, text="    Questions    ", font='Arial 15 underline')

# Function to submit players choice
def submit_choice(choice, question_dictionary):
    global points, points_label, questions_label, rolldice_button
    if choice == question_dictionary["correct"]:
        points += 5
        points_label.destroy()
        points_label = Label(root, text=f"Points : {points}", font='Arial 24', fg="green", bg="black")
        points_label.grid(column=0, row=0, sticky=W)
        label_text = "Correct: +5 Points"
    else:
        label_text = f"Incorrect: Correct answer is {question_dictionary['correct']}"

    all_elements = root.winfo_children()
    for x in range(len(all_elements)):
        all_elements[x].destroy()

    points_label = Label(root, text=f"Points : {points}", font='Arial 24', fg="green", bg="black")
    questions_label = Label(root, text="    Questions    ", font='Arial 15 underline')
    rolldice_button = Button(root, text="Roll Dice", command=rollDice,  font="Arial 15")

    global next_question, result_label
    result_label = Label(root, text=label_text, font="Arial 20", fg="green")
    result_label.grid(column=0, row=0, sticky=W)
    next_question = Button(root, text="Next Question", command=display_questions,  font="Arial 15")
    next_question.grid(column=0, row=1, pady=20)

# Function to roll dice
def rollDice():
    global output
    output = random.randint(1, 6)

    global rolldice_button
    rolldice_button.destroy()

    # Delay for one second
    time.sleep(0.5)

    outcome_label = Label(root, text=f"Outcome : {output}", fg="blue",  font="Arial 20")
    outcome_label.grid(column=0, row=8, sticky=W, pady=20)
    
    # Display the question to be answered
    global questions
    attempted_question = questions[output - 1]
    answered_question = Label(root, text=attempted_question["question"],  font="Arial 20")
    answered_question.grid(sticky=W, pady=10)

    # Loop to display available choices as radio buttons
    global choice
    for key in attempted_question.keys():
        if key == "question":
            pass
        else:
            Radiobutton(root, text=attempted_question[key], variable=choice, value=attempted_question[key],  font="Arial 15").grid(sticky=W)

    # A button for submitting the selected choice
    choice.set(attempted_question["choice1"])
    submit_button = Button(root, text="Submit", command=lambda: submit_choice(choice.get(), attempted_question),  font="Arial 15")
    submit_button.grid()

# Button to call the dice rolling function
rolldice_button = Button(root, text="Roll Dice", command=rollDice,  font="Arial 15")

# Function to start game
def startGame():
    # Remove all labels from the welcome game window
    welcome_label.destroy()
    title_label.destroy()
    instruction1.destroy()
    instruction2.destroy()
    instruction3.destroy()
    instruction4.destroy()
    instruction5.destroy()
    instruction6.destroy()
    start_button.destroy()

    # Function to display the first set of questions
    display_questions()

# Function to display questions on the window
def display_questions():
    # Remove next_question and result_label if in the root window
    if next_question in root.winfo_children() and result_label in root.winfo_children():
        next_question.destroy()
        result_label.destroy()
    else:
        pass

    global points_label, questions_label, questions
    points_label.grid(column=0, row=0, sticky=W)
    questions_label.grid(column=0, row=1, pady=20, sticky=W)
    questions = select_questions()

    # Display 6 Randomly selected questions
    Label(root, text=f"1. {questions[0]['question']}", font="Arial 20").grid(column=0, row=2, sticky=W)
    Label(root, text=f"2. {questions[1]['question']}", font="Arial 20").grid(column=0, row=3, sticky=W) 
    Label(root, text=f"3. {questions[2]['question']}", font="Arial 20").grid(column=0, row=4, sticky=W) 
    Label(root, text=f"4. {questions[3]['question']}", font="Arial 20").grid(column=0, row=5, sticky=W) 
    Label(root, text=f"5. {questions[4]['question']}", font="Arial 20").grid(column=0, row=6, sticky=W) 
    Label(root, text=f"6. {questions[5]['question']}", font="Arial 20").grid(column=0, row=7, sticky=W)

    # Put button on the screen
    rolldice_button.grid(column=0, row=8, pady=20)

# A Lable to display the result
result_label = Label(root, text="",  font="Arial 20")

# A Button to display the next set of questions
next_question = Button(root, text="Next Question", command=display_questions,  font="Arial 15")

# Button to start game
start_button = Button(root, text="START GAME", font="Arial 15", command=startGame)
start_button.grid(column=0, row=8, pady=20)

root.mainloop()