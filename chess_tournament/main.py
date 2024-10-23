from team import Country
from player import Player
from league import Tournament

import pandas as pd






# Function to run the simulation
def run_simulation():

    chess_players = pd.read_excel('chess_players.xlsx')
    # Create the list of players

    players = []

    for index, row in chess_players.iterrows():
        name = row['Player']
        country = row['Country']
        elo = row['Elo']
        player = Player(name, elo, country)
        players.append(player)
    
    # Create the teams

    countries = chess_players['Country'].unique()
    teams = [Country(country) for country in countries]
    for player in players:
        for team in teams:
            if player.country == team.country:
                team.add_player(player)
    
    # Create the tournament

    tournament = Tournament(teams)
    tournament.simulate_tournament()
    tournament.ranking()
                


if __name__ == "__main__":
    
    run_simulation()




