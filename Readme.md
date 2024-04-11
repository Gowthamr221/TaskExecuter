# Task Executer

Task Executer is a simple program designed to store commands in a text file (`commands.txt`) and then load them into a list in a graphical user interface (UI). The program provides users with the ability to modify commands (add, delete, or load), and once done, users can launch each command on their platform's available terminal.

## Features

- **Store Commands**: Users can store commands in the `commands.txt` file. Each command should be placed on a separate line in the file.
  
- **Load Commands**: Task Executer loads the commands from `commands.txt` into a list in the UI, allowing users to view and select commands.

- **Modify Commands**: Users can modify commands by adding new ones, deleting existing ones, or reloading commands from the `commands.txt` file.

- **Launch Commands**: Once the desired commands are loaded, users can launch each command on their platform's available terminal. Currently, the launch features are hardcoded for Windows (using cmd) and Linux (using GNOME Terminal).

## Usage

1. **Store Commands**:
   - Open the `commands.txt` file.
   - Add your commands, one per line, and save the file.

2. **Launch Task Executer**:
   - Run the Task Executer program.
   - It will automatically load commands from `commands.txt` into the UI.

3. **Modify Commands**:
   - Use the UI to add, delete, or load commands.

4. **Launch Commands**:
   - Select a command from the list in the UI.
   - Click the "Launch" button to execute the selected command on your platform's terminal.

## Supported Platforms

- **Windows**: Uses the default command prompt (`cmd.exe`).
- **Linux**: Uses GNOME Terminal.

## Notes

- Task Executer is designed to simplify the execution of lengthy commands that need to be run on terminals, saving users time and effort.

- For further assistance or customization, refer to the program's documentation or contact the developer.

