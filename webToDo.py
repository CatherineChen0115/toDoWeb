import streamlit as st
import modules.toDoFunctions as fn

todos = fn.get_todos()

def add_todo():
    
    todo = st.session_state["newTodo"] + "\n"
    todos.append(todo)
    #print(todo)
    fn.write_todos(todos)
    
st.title("My Todo App")
st.subheader("This is my first web app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    todo_item = f"{index+1}． {todo}"
    checkBoxItem = st.checkbox(label=todo_item, key=todo) # show todo list
    if checkBoxItem:
        todos.pop(index) #remove item from todos list
        fn.write_todos(todos) #update to files
        del st.session_state[todo]
        st.experimental_rerun()
        #st.rerun()
    
st.text_input(label="", placeholder="Enter a new todo...",
              on_change=add_todo, key="newTodo")

print("Hello") #execut each time browser reload

st.session_state