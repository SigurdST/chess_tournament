import random

class Tournament:

    def __init__(self, teams):
        self.teams = teams
        self.results = {team.country: 0 for team in teams}

    def simulate_game(self, player1, player2):

        print(f"\n----- Partie {player1.name} vs {player2.name} -----\n")
        # Calcul des probabilités en fonction des classements Elo
        ratio1 = player1.elo / player2.elo
        if - 0.99 < (ratio1 - 1)  < 0.99:
            proba_blanc_victoire1 = 0.5  + (ratio1 - 1)
            proba_blanc_nul1 = 0.5 - (ratio1 - 1)
            proba_blanc_defaite1 = 1 - proba_blanc_victoire1 - proba_blanc_nul1
        elif (ratio1 - 1)  >= 0.99:
            proba_blanc_victoire1 = 0.98
            proba_blanc_nul1 = 0.01
            proba_blanc_defaite1 = 1 - proba_blanc_victoire1 - proba_blanc_nul1
        else:
            proba_blanc_victoire1 = 0.01
            proba_blanc_nul1 = 0.01
            proba_blanc_defaite1 = 1 - proba_blanc_victoire1 - proba_blanc_nul1

        ratio2 = player2.elo / player1.elo
        if - 0.99 < (ratio2 - 1) < 0.99:
            proba_blanc_victoire2 = 0.5 + (ratio2 - 1)
            proba_blanc_nul2 = 0.5 - (ratio2 - 1)
            proba_blanc_defaite2 = 1 - proba_blanc_victoire2 - proba_blanc_nul2
        elif (ratio2 - 1) >= 0.99:
            proba_blanc_victoire2 = 0.98
            proba_blanc_nul2 = 0.01
            proba_blanc_defaite2 = 1 - proba_blanc_victoire2 - proba_blanc_nul2
        else:
            proba_blanc_victoire2 = 0.01
            proba_blanc_nul2 = 0.01
            proba_blanc_defaite2 = 1 - proba_blanc_victoire2 - proba_blanc_nul2

        


        score1 = 0
        score2 = 0

        # Partie 1: joueur1 a les blancs
        result = random.choices([1, 0.5, 0], [proba_blanc_victoire1, proba_blanc_nul1, proba_blanc_defaite1])[0]
        score1 += result
        score2 += 1 - result
        print(f"Partie 1 : {player1.name} avec les blancs vs {player2.name} avec les noirs: {result} - {1 - result}\n")

        # Partie 2: joueur2 a les blancs (inverser les probabilités)
        result = random.choices([1, 0.5, 0], [proba_blanc_victoire2, proba_blanc_nul2, proba_blanc_defaite2])[0]
        score2 += result
        score1 += 1 - result
        print(f"Partie 2 : {player2.name} avec les blancs vs {player1.name} avec les noirs: {result} - {1 - result}\n")

        return score1, score2

    def simulate_duel(self, team1, team2):
        print(f"\n\n--------------- Match {team1.country} vs {team2.country} ---------------\n")
        team1.order_elo()
        team2.order_elo()
        score_equipe1 = 0
        score_equipe2 = 0

        # Les meilleurs joueurs s'affrontent, puis les deuxièmes meilleurs, etc.
        for i in range(4):
            joueur1 = team1.list_of_players[i]
            joueur2 = team2.list_of_players[i]
            score1, score2 = self.simulate_game(joueur1, joueur2)
            score_equipe1 += score1
            score_equipe2 += score2


        self.results[team1.country] += score1
        self.results[team2.country] += score2

        print(f"Résultat final: {team1.country} {score1} - {score2} {team2.country}\n")
   

    def simulate_tournament(self):
        print("\n---------- BIENVENUE DANS LA SIMULATION DU TOURNOI D'ECHECS ----------\n")
        for i in range(len(self.teams)):
            for j in range(i + 1, len(self.teams)):
                self.simulate_duel(self.teams[i], self.teams[j])

    def ranking(self):

        classement = sorted(self.results.items(), key=lambda x: x[1], reverse=True)
        print("Chess ournament ranking :")
        for rang, (country, points) in enumerate(classement, 1):
            print(f"{rang}. {country} - {points} points")