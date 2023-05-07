import turtle
import pandas

screen = turtle.Screen()
screen.title("Brazil Game")
image = "mapa-regioes.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("states.csv")
all_states = data.state.to_list()
guessed_sates = []

while len(guessed_sates) < 27:
    answer_state = screen.textinput(title=f"{len(guessed_sates)}/27 estados",
                                    prompt="Escreva o nome do estado:").title()
    if answer_state == "Sair":
        missing_states = []
        for state in all_states:
            if state not in guessed_sates:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_sates.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.acronym.item())



