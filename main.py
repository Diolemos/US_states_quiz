import turtle
import pandas

states_data = pandas.read_csv("50_states.csv")
print(states_data)

screen = turtle.Screen()
screen.title("U.S States quiz game")
image = 'blank_states_img.gif'
screen.addshape(image)

#Buggy library, how does this work :P a turtle has not even been instantiated 
turtle.shape(image)

answer_state = screen.textinput(title="Guess the state", prompt="Pick a state name")
answer_state = answer_state.title()
states = states_data['state'].to_list()
# print(states)

if answer_state in states:
    print("nailed!")
# states_data[(states_data['state']).lower() == answer_state]