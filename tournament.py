import csv
import random
import sys

def read_team_data(file_name):
    teams = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            team = {"team": row[0], "rating": int(row[1])}
            teams.append(team)
    return teams

def simulate_game(team1, team2):
    total_rating = team1["rating"] + team2["rating"]
    probability_team1 = team1["rating"] / total_rating
    random_number = random.random()
    return random_number <= probability_team1

def simulate_round(teams):
    winners = []
    for i in range(0, len(teams), 2):
        team1 = teams[i]
        team2 = teams[i + 1]
        if simulate_game(team1, team2):
            winners.append(team1)
        else:
            winners.append(team2)
    return winners

def simulate_tournament(teams):
    while len(teams) > 1:
        teams = simulate_round(teams)
    return teams[0]

def main():
    if len(sys.argv) != 2:
        print("Usage: python tournament.py <team_file>")
        return

    team_file = sys.argv[1]
    teams = read_team_data(team_file)
    counts = {}
    N = 1000
    for i in range(N):
        winner = simulate_tournament(teams)
        if winner["team"] in counts:
            counts[winner["team"]] += 1
        else:
            counts[winner["team"]] = 1

    sorted_teams = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)

    total_simulations = len(teams) * N
    for team in sorted_teams:
        probability = counts[team] / total_simulations
        print(f"{team}: {probability:.2%}")

if __name__ == '__main__':
    main()
