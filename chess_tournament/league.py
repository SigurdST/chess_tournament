import random

class Tournament:
    def __init__(self, teams):
        self.teams = teams
        self.results = {teams.country: 0 for team in teams}

    def simulate_game(self, player1, player2):
        # Calcul des probabilités en fonction des classements Elo
        ratio = player1.elo / player2.elo
        if - 0.49 < (ratio - 1)  < 0.49:
            proba_blanc_victoire = 0.5  * (ratio - 1)
            proba_blanc_nul = 0.5 - (ratio - 1)
            proba_blanc_defaite = 1 - proba_blanc_victoire - proba_blanc_nul
        elif (ratio - 1)  >= 0.49:
            proba_blanc_victoire = 0.98
            proba_blanc_nul = 0.01
            proba_blanc_defaite = 1 - proba_blanc_victoire - proba_blanc_nul
        else:
            proba_blanc_victoire = 0.01
            proba_blanc_nul = 0.01
            proba_blanc_defaite = 1 - proba_blanc_victoire - proba_blanc_nul

        score1 = 0
        score2 = 0

        # Partie 1: joueur1 a les blancs
        result = random.choices([1, 0.5, 0], [proba_blanc_victoire, proba_blanc_nul, proba_blanc_defaite])[0]
        score1 += result
        score2 += 1 - result
        print(f"Partie 1 : {player1.name} avec les blancs vs {player2.name} avec les noirs: {result}")

        # Partie 2: joueur2 a les blancs (inverser les probabilités)
        result = random.choices([1, 0.5, 0], [proba_blanc_defaite, proba_blanc_nul, proba_blanc_victoire])[0]
        score2 += result
        score1 += 1 - result
        print(f"Partie 2 : {player2.name} avec les blancs vs {player1.name} avec les noirs: {result}")

        return score1, score2

    def simulate_duel(self, team1, team2):
        """Simule une rencontre entre deux équipes. Les joueurs s'affrontent par niveau."""
        team1.order_elo()
        team2.order_elo()
        score_equipe1 = 0
        score_equipe2 = 0

        # Les meilleurs joueurs s'affrontent, puis les deuxièmes meilleurs, etc.
        for i in range(4):
            joueur1 = team1.players[i]
            joueur2 = team2.players[i]
            score1, score2 = self.simulate_game(joueur1, joueur2)
            score_equipe1 += score1
            score_equipe2 += score2


        self.results[team1.country] += score1
        self.results[team2.country] += score2
   

    def simulate_tournament(self):

        for i in range(len(self.teams)):
            for j in range(i + 1, len(self.teams)):
                self.simulate_duel(self.equipes[i], self.teams[j])

    def ranking(self):

        classement = sorted(self.res.items(), key=lambda x: x[1], reverse=True)
        print("CTournament ranking :")
        for rang, (country, points) in enumerate(classement, 1):
            print(f"{rang}. {country} - {points} points")