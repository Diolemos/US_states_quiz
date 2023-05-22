import turtle
import pandas

states_data = pandas.read_csv("50_states.csv")
print(states_data)

#set up screen

screen = turtle.Screen()
screen.title("U.S States quiz game")
image = 'blank_states_img.gif'
screen.addshape(image)
correct_answers = []

turtle.shape(image)

#main game loop


while len(correct_answers)<50:
    answer_state = screen.textinput(title=f"{len(correct_answers)}/50", prompt="Pick a state name")
    answer_state = answer_state.title()
    states = states_data['state'].to_list()
   
    #if state name is entered again, ignore it
    if answer_state in states:
        
        if answer_state not in correct_answers:
            correct_answers.append(answer_state)
             
            data_row = states_data[states_data['state']== answer_state]  
            x_coor = int(data_row.x)
            y_coor = int(data_row.y)
            new_title = turtle.Turtle()
            new_title.ht()
            new_title.penup()
        
            new_title.goto(x=x_coor,y=y_coor)
            new_title.write(arg=f"{answer_state}",align='center', font=('Arial',8, 'normal'))
           
   


turtle.mainloop()