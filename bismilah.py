#bismilah 
#first project ever!!
#to do list app
#the task must be added and checked off and should be shown all the time

import sqlite3

db = sqlite3.connect("t.db")
cur = db.cursor()

# Create the tasks table if it doesn't exist
cur.execute('''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    checkmark TEXT
                 )''')

db.commit()


print("   \n    Hello!. this is your task manager, here we help you deal with tasks as efficent as possible.\n      \n -if you want to add a task you type \"add\". \n -if you want to remove a task you type \"remove\". \n -if you want to checkmark your task type \"checkmark\". \n -if you want to check your task list and its checkmarks type \"show\". \n -If you want to quit the app type \"exit\".")


condition = 1
task_not_checked = "X"
task_id = 1


def reassign_task_ids():
    cur.execute("SELECT id FROM tasks")
    task_ids = [row[0] for row in cur.fetchall()]
    for index, task_id in enumerate(task_ids, start=1):
        cur.execute("UPDATE tasks SET id = ? WHERE id = ?", (index, task_id))
    db.commit()

while condition == 1:

        choice = input("   \n                    What do you want to do?.               ")
        if choice == "exit":
            print('   \n   Thank you for using our app.')
            condition = 0
        elif choice == "add":
            task = input(" \n -Please type your new task: ")
            cur.execute("INSERT INTO tasks ( name, checkmark) VALUES (?, ?)", ( task, task_not_checked))
            db.commit()
            print(f"{cur.lastrowid} -  :  {task}  :   [ {task_not_checked} ]")
        elif choice == "checkmark":
                            cur.execute('SELECT id, name, checkmark FROM tasks')
                            print(" \n ")
                            for row in cur.fetchall():
                                task_id, task_name, task_checkmark = row
                                print(f"Task {task_id} - [{task_checkmark}] : {task_name}")
                            print(" \n ")    
                            try:
                                task_checkmark = int(input('What is the ID of the task you want to checkmark?.   '))
                                cur.execute("UPDATE tasks SET checkmark = '✓' WHERE id = ?", (task_checkmark,))
                                db.commit()
                            except ValueError:
                                print("  \n  You can only type an integer.")
        elif choice == "show":
            cur.execute('SELECT id, name, checkmark FROM tasks')
            print(" \n ")
            for row in cur.fetchall():
                task_id, task_name, task_checkmark = row
                print(f"Task {task_id} - [{task_checkmark}] : {task_name}")
        elif choice == "remove":
                        cur.execute('SELECT id, name, checkmark FROM tasks')
                        print(" \n ")
                        for row in cur.fetchall():
                            task_id, task_name, task_checkmark = row
                            print(f"Task {task_id} - [{task_checkmark}] : {task_name}")
                        print(" \n ")    
                        
                        try:
                            task_remove = int(input('What is the ID of the task you want to remove?.    '))
                            cur.execute('DELETE FROM tasks WHERE id =?' ,(task_remove,))
                            reassign_task_ids()
                            db.commit()
                        except ValueError:
                            print('  \n  You can only type an integer.')
        else:
            print('You can only type :\"checkmark\" or \"show\" or \"add\" or "exit".  ')
            condition = 0


#ٱلْحَمْدُ لِلَّٰهِ
#i just finished my first ever programme in about 3-5 days inshalah more to go!! im happy