from sportsreference.nba.roster import Roster
from sportsreference.nba.roster import Player


#get and print player stats
#inspired by Bill Simmons' 42 Club: https://www.espn.com/espn/page2/story?page=simmons/060602
def playerStats(playerID, year):
    player = Player(playerID)
    points = player(year).points
    rebounds = player(year).total_rebounds
    assists = player(year).assists
    games = player(year).games_played
    club = (points+rebounds+assists)/games
    club = round(club, 2)
    print(player.name, ": ", club)


#get user input
team = input("Enter team abbreviation (ex: 'GSW' = Golden State Warriors): ")
year = input("Enter year: ")

#calculate nba season year
newYear = 0
year = int(year)
if(year >= 2000):
    newYear = year%2000
else:
    newYear = year%1900
year = year-1
if(newYear == 0):
    newYear = "00"
finYear = str(year) + "-"+ str(newYear)
print(finYear)

#check if roster exists
try:
    teams = Roster(team, year+1, slim = True)
except: 
    print("No teams found")
    quit()

roster = Roster(team, year+1, slim = True)

#iterate through roster
for player in roster.players:
    playerStats(player, finYear)

#playerLook = input("Twitter mentions of which player? ")
