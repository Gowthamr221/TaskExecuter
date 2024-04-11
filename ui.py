import tkinter as tk
import actions
custom_font = ('Helvetica', 12, 'bold')

def renderUi(UiRoot):
    # Frame for Commands List
    commandsFrame = tk.Frame(UiRoot)
    commandsFrame.pack(anchor='nw', padx=10, pady=10,fill='both',expand=True)
    
    commandsListbox = tk.Listbox(commandsFrame, width=50, height=10)
    commandsListbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    # load commands from txt file for the first time
    actions.check_and_load_commands(commandsListbox)
    
    scrollbar = tk.Scrollbar(commandsFrame, orient=tk.VERTICAL)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # button behaviour
    
    executeCommand = tk.Button(UiRoot, text="Execute",command=lambda:actions.execute_command(listbox=commandsListbox),font=custom_font,bg='black',fg='white')
    executeCommand.pack(anchor='nw', padx=10, pady=10)
    
    executeCommand = tk.Button(UiRoot, text="Load Commands",command=lambda:actions.load_commands(listbox=commandsListbox),font=custom_font,bg='black',fg='white')
    executeCommand.pack(anchor='nw', padx=10, pady=10)
    
    deleteCommand = tk.Button(UiRoot, text="Delete Command",command=lambda:actions.delete_command(listbox=commandsListbox),font=custom_font,bg='black',fg='white')
    deleteCommand.pack(anchor='nw', padx=10, pady=10)
    
    addCommandLabel = tk.Label(UiRoot, text="Add Command", font=custom_font)
    addCommandLabel.pack(anchor='nw', padx=10, pady=10)

    addCommandInput = tk.Entry(UiRoot, font=custom_font)
    addCommandInput.pack(anchor='nw', padx=10, pady=10,fill='x')

    addCommandButton = tk.Button(UiRoot, text="Add Command",command=lambda:actions.add_command(entry=addCommandInput,listbox=commandsListbox), font=custom_font,bg='black',fg='white')
    addCommandButton.pack(anchor='nw', padx=10, pady=10)











