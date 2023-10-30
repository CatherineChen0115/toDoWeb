import streamlit as st
import modules.toDoFunctions as fn

todos = fn.get_todos()

def add_todo():
    
    todo = st.session_state["newTodo"] + "\n"
    todos.append(todo)
    #print(todo)
    fn.write_todos(todos)
    
### layout ###
tab1, tab2, tab3 = st.tabs(["toDo", "ref", "others"])
with tab1: #todo
    st.image("images/cat.jpg", width=150)
    st.header("Todo Function")
    #st.subheader("This is a todo web app.")
    st.write("Please check the item you want to complete.")


    st.text_input(label="", placeholder="Enter a new todo...",
                on_change=add_todo, key="newTodo")

    for index, todo in enumerate(todos):
        todo_item = f"{index+1}． {todo}"
        checkBoxItem = st.checkbox(label=todo_item, key=todo) # show todo list
        if checkBoxItem:
            todos.pop(index) #remove item from todos list
            fn.write_todos(todos) #update to files
            del st.session_state[todo]
            st.experimental_rerun()
            #st.rerun()

with tab2: #api ref link
    link = 'https://docs.streamlit.io/library/api-reference/text/st.markdown'
    st.markdown(link)

#print("Hello") #execut each time browser reload

#st.session_state