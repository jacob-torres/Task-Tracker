"""Reset the tasks file."""

import re


def uncheck_daily_todos():
    """Uncheck all daily todo checkboxes."""
    tasks = ""
    todos = ""
    pattern = re.compile(r"## To Do")

    with open("tasks.md", "r") as file:
        tasks += file.read()

    match_obj = pattern.search(tasks)
    index = match_obj.span()[0]
    todos = tasks[:index]
    todos = re.sub("\[x\]", "[ ]", todos)

    with open("tasks.md", "w") as file:
        file.write(todos)

    with open("tasks.md", "a") as file:
        file.write(tasks[index:])

