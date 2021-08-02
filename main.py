import turtle
from turtle import Turtle, Screen
import csv
import pandas

screen = Screen()
screen.title("USA State Game")
screen.bgpic("blank_states_img.gif")
screen.setup(730, 500)

state = pandas.read_csv("50_states.csv")
correct_states = []
correct_count = 0
while correct_count < 50:
    guessed_already = False
    guess = screen.textinput(f"{correct_count}/50 States correct: ", "What is another state name?").title()
    if guess in correct_states:
        print("You already chose this state")
        guessed_already = True


    for states in state["state"]:
        if guess == states and guessed_already == False:
            correct_count += 1
            correct_states.append(states)
            all_state_info = state[state["state"] == states]
            turtle.hideturtle()
            turtle.speed("fastest")
            turtle.penup()
            turtle.setpos(int(all_state_info["x"]),int(all_state_info["y"]))
            turtle.write(states)
            print(f"Good job! You got {correct_count}/50 states correct")

    if guess == "Exit":
        missing_states = []
        for states in state["state"]:
            if states not in correct_states:
                missing_states.append(states)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("learn.csv")

        print('You chose to exit')
        print(f"You got {correct_count}/50 states correct")
        exit()

def cordz(x, y):
    print(x, y)

turtle.onscreenclick(cordz)
turtle.mainloop()