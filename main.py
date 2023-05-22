import turtle
import pandas

states_data = pandas.read_csv("50_states.csv")
print(states_data)

screen = turtle.Screen()
screen.title("U.S States quiz game")
image = 'blank_states_img.gif'
screen.addshape(image)
correct_answers = []
#Buggy library, how does this work :P a turtle has not even been instantiated 
turtle.shape(image)
while True:
    answer_state = screen.textinput(title=f"{len(correct_answers)}/50", prompt="Pick a state name")
    answer_state = answer_state.title()
    states = states_data['state'].to_list()
    # print(states)

    if answer_state in states:
        print("nailed!")
        correct_answers.append(answer_state)
    # states_data[(states_data['state']).lower() == answer_state]


turtle.mainloop()