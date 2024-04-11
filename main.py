import tkinter as tk
import ui

# root object
root = tk.Tk()
root.title("Task Executer 🏹")

#render ui
ui.renderUi(root)

# window size
root.geometry("800x600+100+100")

# tkinter main thread
root.mainloop()