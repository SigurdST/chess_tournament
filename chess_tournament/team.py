class Country():


    def __init__(self, country):

        self.list_of_players = []
        self.country = country

    def add_player(self, player):
        if player.country == self.country:
            self.list_of_players.append(player)

    def order_elo(self):
        self.list_of_players.sort(key=lambda x: x.elo, reverse=True)

    def __str__(self):
        players_str = ', '.join([player.name for player in self.list_of_players])
        return f"Team {self.team_name} has players: {players_str}"