user_name=input("Enter you name : ")
print(f"Welcome {user_name} to this Adventure!")

answer=input("There is a dirty road ahead of you so you can either go Right or Left. which way you would go? (Right/Left) ").lower()

if answer == "left":
    answer= input("There is an empty land and a river where would you like to go? (river/land)  ").lower()
    if answer == "river":
        print(f"Sorry for you {user_name} You tried to cross the river but got eaten by an alligator and lost..")
    elif answer == "land":
        print("You chose to go to the empty land but you got ranout of water and just lost..")
    else:
        print(f"Invalid option {user_name} lost!")
elif answer == "right":
    answer=input("You saw a bridge would you like cross it or no? (Yes/No) ").lower()
    if answer == "yes":
        print("You crossed the bridge and saw a man there")
        answer=input("The man you saw after the crossing the bridge did you talk to him?(Yes/No)  ").lower()
        if answer == "yes":
            print(f"Congrats,{user_name} You did a great job talking to that person so he gave you gold and you won the game!")
        elif answer =="no":
            print(f"You should have talked to that stranger,you lost {user_name}")
        else:
            print(f"Invalid option {user_name} lost!")        
    elif answer == "no":
        print("You should have crossed the bridge so you did'nt and simply lost..")
    else:
        print(f"Invalid option {user_name} lost!")
else:
    print(f"Invalid option {user_name} lost!")
print(f"---Game Over---\nHope you enjoyed {user_name}")