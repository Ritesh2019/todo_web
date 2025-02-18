import streamlit as st
import functions

st.title("My Todo App")
st.subheader("This a todo app")
st.write("This app is to maintain your daily todos")
todos = functions.read_file()
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_file(todos)
        del st.session_state[todo]
        st.rerun()

def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.write_file(todos)


st.text_input(label="Enter a todo", placeholder="Enter a todo",
              key="new_todo", on_change=add_todo)
st.session_state

