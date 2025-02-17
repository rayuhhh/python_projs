

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
   

    
def display_menu(todo: Todo)-> None:
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2/ View Tasks")
        print("3. Mark Task Complete")
        print("4. Remove Task")
        print("5. Save Tasks")
        print("6. Load Tasks")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter Task: ")
            # line methods up with this menu for all choices
            create_task(task)
            todo.add_task
        elif choice == "2":
            #view_tasks()
        elif choice == "3":
            #
            task_idx =  int(input("Enter task number to mark as complete: "))
            mark_complete(task_idx)
        elif choice == "4":
        elif choice == "5":
        elif choice == "6":
        elif choice == "7":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

def main():
    
    todo = create_todo()
    display_menu(todo)

    
    todo.add_task(task_one)
    #todo.add_task('laundry')
    todo.view_tasks()
    #print(todo)




if __name__ == "__main__":
    main()