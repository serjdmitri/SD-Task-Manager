from tkinter import *           #import everything from tkinter
from tkinter import messagebox  #import messagebox from tkinter because it wasnt included in the first import

tasks = [] #list for tasks made
completed_tasks = [] #list for tasks completed

# Main window
main = Tk() #start window
main.title("SD Task Manager") #title of window
main.geometry("2000x1000") #size of window

# FUNCTIONS: ----------------------------------------------------------------------------------------------

# Close program function for exit button
def close_program(): 
    main.destroy()

# Open new window when add task button is clicked: everything in add task menu
def open_add_task():
    add_task = Toplevel(main) #create new window
    add_task.title("Add Task") #title of new window
    add_task.geometry("300x500") #size of window
    
    #frame for when task is added to the list
    entry_frame = Frame(add_task)
    entry_frame.pack(fill="both", expand=True)

    #Text at the top of window saying what it is
    title_text = Label(entry_frame, text="Add Your Task Below", font=('American Typewriter', 16))
    title_text.pack(pady=10)
    
    #Desciption typing box
    box_text_title = Label(entry_frame, text="Description: ") #Label indicating what it is for
    box_text_title.pack(pady=5)
    box_text = Entry(entry_frame) #the typing box
    box_text.pack()

    #Due time typing box
    box_text_title2 = Label(entry_frame, text="Due: ") #Label indicating what it is for
    box_text_title2.pack(pady=5)
    box_text2 = Entry(entry_frame) #the typing box
    box_text2.pack()

    #The priotity selection drop down menu
    box_text_title3 = Label(entry_frame, text="Priority lvl: ") #Label indicating what it is for
    box_text_title3.pack(pady=5)
    options_var = StringVar(value="Select an option") #the drop down box with the starting text

    options = ["High", "Medium", "Low"] #the three options for the drop down menu
    menu = OptionMenu(entry_frame, options_var, *options) #when selection is made it is shown
    menu.pack()

    # Task saved confirmation frame
    success_frame = Frame(add_task)
    
    def show_success_frame():
        # Clear entry frame and show the success frame
        entry_frame.pack_forget()
        success_frame.pack(fill="both", expand=True)
        Label(success_frame, text="Task Successfully Saved!", font=('Arial', 16), fg="green").pack(pady=50)
        Button(success_frame, text="OK", command=add_task.destroy).pack(pady=20)

    # Save task and display it in the main window
    def save_task():
        task_desc = box_text.get()
        due_date = box_text2.get()
        priority = options_var.get()

        if task_desc and due_date and priority != "Select an option":  # Ensure all fields are filled
            task = f"{task_desc} (Due: {due_date}, Priority: {priority})"
            tasks.append(task)
            display_task(task)  # Show the task in the main window
            show_success_frame()  # Show confirmation

    Button(entry_frame, text="Save Task", command=save_task).pack(pady=10)

# Function to display tasks in the main window
def display_task(task):
    task_frame = Frame(main)
    task_frame.pack(fill="x", pady=5)

    # Task text
    Label(task_frame, text=task, anchor="w", wraplength=200).pack(side="left", padx=5)

    # Complete button to mark task as complete
    Button(task_frame, text="Complete", command=lambda: complete_task(task, task_frame)).pack(side="right", padx=5)

    
# Function to mark a task as complete
def complete_task(task, task_frame):
    tasks.remove(task)
    completed_tasks.append(task)
    task_frame.destroy()
    messagebox.showinfo(title = "YAY!", message = "You completed the task")
        
# Open new window when completed tasks button is clicked: everything in completed tasks menu
def open_completed_tasks():
    comp_task = Toplevel(main)
    comp_task.title("Completed Tasks")
    comp_task.geometry("300x500")
    
    for task in completed_tasks:
        Label(comp_task, text=task, anchor="w", wraplength=250).pack(fill="x", padx=10, pady=5)
       
    # Function to refresh the completed tasks list
    def refresh_completed_tasks():
        # Clear the current list
        for widget in comp_task.winfo_children():
            widget.destroy()
            
        title_text = Label(comp_task, text="Your Completed Tasks", font=('American Typewriter', 16))
        title_text.pack()

        # Display updated tasks
        for task in completed_tasks:
            Label(comp_task, text=task, anchor="w", wraplength=250).pack(fill="x", padx=10, pady=5)
        
        # Schedule the function to run again after 1000 ms (1 second)
        comp_task.after(1000, refresh_completed_tasks)

    # Start the refresh loop
    refresh_completed_tasks()

# MAIN WINDOW: -------------------------------------------------------------------------------------------

# Text in main window (name of "app")
text = Label(main, text="The SD Task Manager", fg="white", font=('American Typewriter', 25))
text.pack(pady=20)

# Add task button
button = Button(main, text="Add task", command=open_add_task)
button.pack(pady=50)

# View completed tasks button
button2 = Button(main, text="View Completed tasks", command=open_completed_tasks)
button2.pack(pady=42)

# The EXIT button
button3 = Button(main, text="EXIT", command=close_program, fg="red", height=2, width=2)
button3.pack(pady=70)

# Loads everything
main.mainloop()
