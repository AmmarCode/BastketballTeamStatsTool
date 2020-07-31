# Basketball Team Stats Tool

In this project I will be writing a program that reads from the "constants" data (`PLAYERS` and `TEAMS`) in `constants.py`. This data will be translated into a new collection and the fields will be changed to something that makes more sense for Python to do its comparisons.


**Steps of the project:**

1. Create a new empty script file called `app.py` or `application.py`

2. Import from constants.py the players' data to be used within the program.

3. Create clean data function to clean the player's data without changing the original data.
   Data to be cleaned:
    * Height: This should be saved as an integer.
    * Experience: This should be saved as a boolean value (True or False).
    * Clean guardians data.

4. Create a balance_teams function.
     * Balance the players across the three teams: Panthers, Bandits and Warriors. 
     * Each team will have the same number of total players.
     * Each team will have the same number of experienced and inexperienced players.

5. Creat a menu function for options selection.
   Main Menu:
     * Display Team Stats.
     * Quit. 
   Team Menu:
     * Choose a team to view it's stats.
      
6. Display stats.
     * Team's name.
     * Total players on the team.
     * Total experienced players on the team.
     * Total inexperienced players on the team.
     * Average height of players on the team.

7. Prompt users with main menu after displaying stats until they choose to Quit the program.




