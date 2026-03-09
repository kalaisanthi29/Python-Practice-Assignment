#Exercise 2: Task list manager (with separate module) 
def add_task(task_list, task): 
    task_list.append(task)

def remove_task(task_list, task): 
    if task in task_list: 
        task_list.remove(task)
    else:
        print("Task not found.")