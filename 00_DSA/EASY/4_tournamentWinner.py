"""
 Problem Statement:-
    There will be matrix of n x 2, where n will the number of compeititions and two
    members are going to participate in the tournament where the columns represents,

    1st column  --> Home Team
    2nd column  --> Away Team

    you will have to return tournament winner by using the array which consists of
    all the winners of all the competitions where 0 -> Away and viceversa.

"""

HOME_TEAM_WON = 1


def tournamentWinner(competitions, competition_result):
    """
    Approach 1: Time Complexity: O(N) | Space Complexity O(k)

    what we going to do is pretty simple and the beauty of this problem lies
    in it's presentation although it falls in Easy category it can be very Hard
    as well.

    we will Iterate over the matrix using single for loop and we know that
    each row contains only two values and we will mantain a dictionary to keep
    check of the winningteam and a Variable CurrentBestTeam.

    update the winningteam according to who win the match and increase their
    value in scores and check if that become best team or not.

    """

    currentBestTeam = ""
    scores = {currentBestTeam: 0}

    for idx, competition in enumerate(competitions):
        print(idx)
        result = competition_result[idx]
        homeTeam, awayTeam = competition

        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

        updateScores(winningTeam, 3, scores)

        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam

    return currentBestTeam, scores


def updateScores(team, points, scores):
    if team not in scores:
        scores[team] = 0

    scores[team] += points
    # pass


competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
competition_result = [0, 0, 1]


winner, scores = tournamentWinner(competitions, competition_result)
print(f"Tournament Winner is: {winner} {scores}")
