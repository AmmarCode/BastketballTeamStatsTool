import constants
import copy
import sys


def clean_data():
    # Clean player's list data by formating:
    # player's experience to boolean and
    # player's height to integer
    for player in players:
        if player['experience'].lower() == 'yes':
            player['experience'] = True
        elif player['experience'].lower() == 'no':
            player['experience'] = False
        player['height'] = int(player['height'][:2])
        player['guardians'] = player['guardians'].split('and')


def balance_team():
    # Devide players to 2 groups: Experienced, Inexperienced
    experienced = [player for player in players if player['experience'] == True]
    inexperienced = [player for player in players if player['experience'] == False]
    team_total = len(experienced) / len(teams) + len(inexperienced) / len(teams)
    # Add equal number of experienced players to each team
    for player in experienced:
        if player not in Panthers and len(Panthers) != 3:
            Panthers.append(player)
        elif player not in Bandits and len(Bandits) != 3:
            Bandits.append(player)
        elif player not in Warriors and len(Warriors) != 3:
            Warriors.append(player)
    # Add equal number of inexperienced players to each team
    for player in inexperienced:
        if player not in Panthers and len(Panthers) != 6:
            Panthers.append(player)
        elif player not in Bandits and len(Bandits) != 6:
            Bandits.append(player)
        elif player not in Warriors and len(Warriors) != 6:
            Warriors.append(player)
    # Add team names to the team's lists
    Panthers[0]['team name'] = teams[0]
    Bandits[0]['team name'] = teams[1]
    Warriors[0]['team name'] = teams[2]


def menu():
    # Print App name and menu options
    print(f"{'-' * 26}\nBASKETBALL TEAM STATS TOOL\n{'-' * 26}\n\n----MENU----\n\n"
          "Here are your choices:\n1) Display Team Stats\n2) Quit")
    while True:
        try:
            # Prompt user to choose: use app or quit
            choice = input(" Enter an option > ")
            choice = int(choice)
            if choice < 1 or choice > 2:
                raise ValueError("Please choose option 1 or 2")
        except ValueError as err:
            print(f"Invalid input,{err}")
            continue
        else:
            # Prompt user to choose a team to view it's stats
            while choice == 1:
                print("\n1) Panthers\n2) Bandits\n3) Warriors\n")
                try:
                    select = input("Enter an option> ")
                    select = int(select)
                    if select < 1 or select > 3:
                        raise ValueError('Please select a number from options (1-3)')
                except ValueError as err:
                    print(f"Invalid input,{err}")
                    continue
                else:
                    if select == 1:
                        return Panthers
                    elif select == 2:
                        return Bandits
                    elif select == 3:
                        return Warriors
            if choice == 2:
                # Print Goodbye message
                print(f"{'-' * 46}\nThank you for using BASKETBALL TEAM STATS TOOL\n{'-' * 46}")
                sys.exit()


def display_stats(team):
    count = 0
    while True:
        # Calculate average height
        try:
            team_height = [player['height'] for player in team]
            sum_height = sum(team_height)
            avg_height = round((sum_height) / len(team), 1)
        except TypeError:
            print(count)
            count += 1
            continue
        # display team stats:
        # ( Total players, Experienced, Inexperienced, Average height
        print(f"\nTeam: {team[0]['team name']}\n{'-' * 20}\nTotal players: {len(team)}\nTotal "
              f"experienced: {int(len(team) / 2)}\nTotal inexperienced: "
              f"{int(len(team) / 2)}\nAverage height: {avg_height}\n\nPlayers on team:")
        # Format players name to string
        name_list = [player['name'] for player in team]
        name = ', '.join(name_list)
        print(name + '\n')
        # Format guardians to string
        guardians = []
        for index in team:
            for guardian in index['guardians']:
                guardians.append(guardian)
        guard = ', '.join(guardians)
        print(f"Guardians:\n{guard}")
        # Prompt user to press Enter to return to Main menu
        input("Press Enter to continue")
        display_stats(menu())


# ------------------------------------------------
if __name__ == '__main__':
    players = copy.deepcopy(constants.PLAYERS)
    teams = copy.deepcopy(constants.TEAMS)

    Panthers = []
    Bandits = []
    Warriors = []
    clean_data()
    balance_team()
    display_stats(menu())
