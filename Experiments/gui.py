import functions
import FreeSimpleGUI as sg
import time

sg.theme('DarkPurple4')

clock = sg.Text('', key='clock')
label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip='Enter todo', key='todo')
add_button = sg.Button(size=10, image_source='add.png', mouseover_colors='LightBlue2', key='Add')
list_box = sg.Listbox(values= functions.get_todos(), key= 'todos',
                      enable_events=True, size=[45,10])
edditbutton = sg.Button('Edit')
complete_button = sg.Button(size=10, image_source='complete.png', mouseover_colors='LightBlue2', key='Complete')
Exit_button = sg.Button('Exit')

window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edditbutton, complete_button],
                           [Exit_button]],
                   font=('Helvetica', 10))

while True:
    event, values = window.read(timeout=10)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values["todo"]+"\n"
            todos.append(new_todo)
            functions.get_now(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            try:
                todo = values['todos'][0]
                new_todos = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo)
                todos[index] = new_todos
                functions.get_now(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup('Please select and item first', font=('Helvetica', 10))
        case'Complete':
            try:
                todotocomplete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todotocomplete)
                functions.get_now(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup('Please select and item first', font=('Helvetica', 10))
        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case 'Exit':
            break
window.close()
