#this script will eventually run every two hours
#need to make functions to make this cleaner

import time
import webbrowser

break_count=0
total_breaks=3
three_goals = input("\nList your three goals for today: ")
while(break_count < total_breaks):
    time.sleep(10)
    now_goal= input("\nWhich goal do you want to work on now?")
    time.sleep(10)

    print("\nIt's time to take a break.\nCheck out this video and come back when you're done.")
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=tAUf7aajBWE")

    time.sleep(10)
    next_goal = input("\nWhat goal do you want to work on next?")
    print("You've got this " + next_goal + " !")
    break_count +=1
