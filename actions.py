import subprocess
import tkinter as tk
import platform
import os
# button actions
    
def load_commands(listbox):
    listbox.delete(0, tk.END)  # Clear the listbox
    with open("commands.txt", "r") as file:
        for line in file:
            command = line.strip()
            listbox.insert(tk.END, command)

def delete_command(listbox):
    selected_indices = listbox.curselection()
    if selected_indices:
        index = selected_indices[0]
        listbox.delete(index)
        with open("commands.txt", "r") as file:
            commands = file.readlines()
        with open("commands.txt", "w") as file:
            for i, line in enumerate(commands):
                if i != index:
                    file.write(line)

def add_command(entry,listbox):
    command = entry.get()
    if command:
        with open("commands.txt", "a") as file:
            file.write(command + "\n")
            file.flush()  # Ensure changes are immediately written to the file
        entry.delete(0, tk.END)  # Clear the entry field after adding the command
        listbox.insert(tk.END, command)

        
def execute_command(listbox):
    selected_indices = listbox.curselection()
    if selected_indices:
        index = selected_indices[0]
        command = listbox.get(index)
        if platform.system() == 'Windows':
            subprocess.Popen(['cmd', '/c', 'start', 'cmd', '/k', command])
        elif platform.system() == 'Linux':
            subprocess.Popen(['x-terminal-emulator', '--tab', '-e', command])
            
def check_and_load_commands(listbox):
    file_path = "commands.txt"
    if os.path.exists(file_path):
        print("File 'commands.txt' exists. Loading commands...")
        load_commands(listbox=listbox)
    else:
        print("File 'commands.txt' does not exist. Creating the file...")
        with open(file_path, "w") as file:
            #file.write("# Add your commands here, one per line\n")
            pass
        print("File 'commands.txt' created.")