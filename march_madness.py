with open("teams_scored.csv") as scores:
    teams=scores.read().splitlines()
    for index,row in enumerate(teams):
        teams[index]=row.split(",")
    teams.pop(0)
    team_scores={}
    for index, school in enumerate(teams):
        team_scores[teams[index][0]]=float(teams[index][1])


with open("bracket.csv",'r') as bracket:
    matchups=bracket.read().splitlines()
    for index,row in enumerate(matchups):
        matchups[index]=row.split(",")

    for matchup in matchups:
        team1=matchup[0]
        team2=matchup[1]
        if team_scores[team1] < team_scores[team2]:
            winner=team1
        elif team_scores[team1] > team_scores[team2]:
            winner=team2
        else:
            print "Something went wrong"

        print "In the game between {0} and {1}, {2} wins".format(team1, team2, winner)

entries="y"
while entries=="y":
    team1=raw_input("Who is team 1? ")
    team2=raw_input("Who is team2? ")
    if team_scores[team1] < team_scores[team2]:
         winner=team1
    elif team_scores[team1] > team_scores[team2]:
        winner=team2
    else:
        print "Something went wrong"
        print "{0} score: {1}".format(team1,team_scores[team1])
        print "{0} score: {1}".format(team2,team_scores[team2])

    print "In the game between {0} and {1}, {2} wins".format(team1, team2, winner)
    entries=raw_input("do you have more games to pick? y/n ")

