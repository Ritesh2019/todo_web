def read_file(filename="todo.txt"):
    """ this function use to
    read todos from file """
    with open(filename, "r") as file:
        my_todos = file.readlines()
        return my_todos


# print(help(read_file))


def write_file(my_todos,filename="todo.txt"):
    """ this function is use to write todos into a file """
    with open(filename, "w") as file:
        file.writelines(my_todos)

# print(__name__)


if __name__ == "__main__":
    print("hello")
    print(read_file())