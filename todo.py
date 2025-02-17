

class Todo:
    def __init__(self, name):
        if not name:
            raise ValueError('Missing name for todo list')
        self.name = name
        self.tasks = []

    def __str__(self):
        return f'To do list: {self.name} \nwith tasks: \n {'\n '.join(self.tasks)}'
    
    # add task
    def add_task(self, task):
        self.tasks.append(task)
    
    def view_tasks(self):
        count = 1
        for task in self.tasks:
            print(f'{count}. {task}')
            count+=1
   
    #def mark_complete(self, index):



    # Getter
    
    # Setter
    
class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False

    def __str__(self):
        return f'{self.name}, is completed: {self.completed}'

def create_task(name):
    return Task(name)

def create_todo():
    name = input("Name: ")
    return Todo(name)
   

    



def main():
    
    todo = create_todo()
    task_one = create_task('lift')
    todo.add_task(task_one)
    #todo.add_task('laundry')
    todo.view_tasks()
    #print(todo)




if __name__ == "__main__":
    main()