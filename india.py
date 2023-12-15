import turtle
import pandas
screen = turtle.Screen()
screen.title("India State Game")

image = "inde15.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("Indian_state.csv")
state_list = data["state"].to_list()
guessed_state = []

while len(guessed_state) < 32:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/32 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        state_empty = [g_state for g_state in state_list if g_state not in guessed_state]

        new_data = pandas.DataFrame(state_empty)
        new_data.to_csv("India missing state.csv")
        break
    if answer_state in state_list:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

turtle.mainloop()
