import os

file_path = "C:\Users\teais\Desktop\Personal\Daily life"

class Todo:
    def __init__(self, name):
        if not name:
            raise ValueError('Missing name for todo list')
        self.name = name
        self.tasks = []

    def __str__(self):
        return f'To do list: {self.name} \nwith tasks: \n' +('\n '.join(self.tasks)) if len(self.tasks)>1 else f'To Do item: {self.tasks[0]}'
    
    # add task
    def add_task(self, task):
        self.tasks.append(task)
    
    def view_tasks(self):
        count = 1
        for task in self.tasks:
            print(f'{count}. {task}')
            count+=1
   
    def index_check(self, index):
        if index < 0 or index> len(self.tasks)-1:
            print('Invalid task index, please enter valid index.')
            return False
        return True

    def mark_complete(self, index):
        if self.index_check(index):
            if self.tasks[index].completed:
                print('task already completed')
            else:
                self.tasks[index].completed = True
    
    def remove_task(self, index):
        if self.index_check(index):
            self.tasks.pop(index)
    
    def save_to_file(self, file_path):
        with open(file_path, 'w') as file:
            file.write(f'{self.name}\n')
            for task in self.tasks:
                file.write(f'{task.name}, completed: {task.completed}')
        print("To do list and tasks saved to file")
    



    
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
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Remove Task")
        print("5. Save Tasks")
        print("6. Load Tasks")
        print("7. Exit")
        choice = input("Choose an option: ")

        print()

        # Add a Task
        if choice == "1":
            task = input("Enter Task: ")
            # line methods up with this menu for all choices
            task_one = create_task(task)
            todo.add_task(task_one)

        # View Tasks of to do list
        elif choice == "2":
            todo.view_tasks()
        
        # Mark task as complete
        elif choice == "3":
        
            task_idx =  int(input("Enter task number to mark as complete: ")) - 1

            todo.mark_complete(task_idx)
        # Remove task from To Do list    
        elif choice == "4":
            task_idx = int(input("Enter task number to removed from list: ")) - 1
            todo.remove_task(task_idx)

        # Save Tasks
        # elif choice == "5":
        # elif choice == "6":
        elif choice == "7":
            print("Exiting the program.")
            #todo.view_tasks()
            break
        else:
            print("Invalid option. Please try again.")

def main():
    
    todo = create_todo()
    display_menu(todo)





    # task_one = create_task('Add')
    
    # todo.add_task(task_one)
    #todo.add_task('laundry')
    #print(todo)
    # todo.view_tasks()
    # todo.mark_complete(0)
    # todo.view_tasks()
    #print(todo)




if __name__ == "__main__":
    main()