# Coffee Machine

Coffee Machine is an [Hyperskill](https://hyperskill.org/projects/68?goal=391) Python project that simulates the actions of a coffee machine.

## Run the Project

In order to run the prject, run the following commands.

```bash
git clone https://github.com/Attol8/Python-projects.git
cd Python-projects/coffee_machine
python coffee_machine.py
```
## Example

Below is an example of the woring code

```bash
Input command:start user hard #the two parameters after 'start' can be 'user', 'easy', 'medium' or 'hard'. 'user' lets the human inputs coordinates
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
Input command:
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.