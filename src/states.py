from Levenshtein import distance
import sys


def main():
    """This program asks the user to enter the US states. All right answers get
    a point. All almost correct answers, with low editing distance from right
    answers get half a point and a chance of redemption. All incorrect answers get
    no points. The program ends when the user enters an empty string.""" 
    states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
              "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois",
              "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
              "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana",
              "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York",
              "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
              "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
              "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    points = 0
    done = []
    almosts = []
    guesses = []
    while points < 50:
        answer = input("Enter the name of a US state: ")
        if answer == "":
            print("See you next time!")
            break
        elif answer in done:
            print("You have already entered that state.")
        elif answer in states:
            if answer in almosts:
                print("You almost got that one before!")
                almosts.remove(answer)
                points += 0.25
            else:
                points += 1
            print("Correct! You have {} points.".format(points))
            done.append(answer)
        else:
            lowest = 10**6
            lowest_state = ""
            for state in states:
                if distance(answer.lower(), state.lower()) < lowest:
                    lowest = distance(answer.lower(), state.lower())
                    lowest_state = state
            if lowest_state in almosts:
                print("You almost got that one before! Now I will withdraw 0.25 points.")
                score -= 0.25
            if lowest < 3:
                points += 0.5
                print("Almost correct! You have {} points.".format(points))
                almosts.append(lowest_state)
                guesses.append(answer)    
            else:
                points -= 1
                print("Incorrect! You have {} points after being punished with"\
                      +" a negative point.".format(points))
    else:
        print("Congratulations! You got all the states!")
        sys.exit()
    if almosts:
        print("You got {} points so far.".format(points))
        print("Let's see if you can solve the almosts!")
    for guess in guesses:
        answer = input("What state did you mean by {}? ".format(almost))
        if answer in almosts:
            points += 0.25
            print("You have redeemed one answer! You have {} points.".format(points))
            done.append(answer)
            almosts.remove(answer)
        else:
            if answer in states:
                print("You have already entered that state.")
            else:
                print("Incorrect! You have {} points.".format(points))
    print("You got {} points in total.".format(points))
    if done:
        print("The states you got are:", *done)
    if almosts:
        print("The states you almost got are:", *almosts)
    if len(done)<50:
        print("The states you missed are:", *list(set(states) - set(done)))


if __name__ == '__main__':
    main()