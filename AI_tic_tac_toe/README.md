# Tic Tac Toe wit AI

Coffee Machine is an [Hyperskill](https://hyperskill.org/projects/82?goal=391https://hyperskill.org/curriculum#about) Python project that simulates a game of Tic Tac Toe against 
an AI. The AI can play at 3 different skills levels: 'easy', 'medium' and 'hard'.

## Run the Project

In order to run the project, run the following commands.

```bash
git clone https://github.com/Attol8/Python-projects.git
cd Python-projects/AI_tic_tac_toe
python tic_tac_toe.py
```
## Example

Below is an example of a game between yourself ('user') and the most intelligent AI ('hard'). You can change the game by changing the command after 'Input command:'.

```bash
#the two parameters after 'start' can be 'user', 'easy', 'medium' or 'hard'.
Input command:start user hard 
---------
|       |
|       |
|       |
---------
Enter the coordinates:1 1
---------
|       |
|       |
| X     |
---------
Making move level "hard"
---------
|       |
|   O   |
| X     |
---------
Enter the coordinates:1 2
---------
|       |
| X O   |
| X     |
---------
Making move level "hard"
---------
| O     |
| X O   |
| X     |
---------
Enter the coordinates:2 1
---------
| O     |
| X O   |
| X X   |
---------
Making move level "hard"
---------
| O     |
| X O   |
| X X O |
---------
O wins
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.