# Choose you own adveture by Bambo
answer = input("Would you like to play? (yes/no): ")

if answer.lower().strip() == "yes":
     
    answer = input("You reach a crossroads, would you like to go left or right: ").lower().strip()
    if answer == "left":
        answer = input("You encounter a monster would you like to run or attack: ")
        if answer == "attack":
            print("You made the monster mad and he pummled you into pulp, You died")
        elif answer == "run":
            print("You outrun the monster with it still chasing you")
            answer = input("As you run from the monster you come across a ruined building would you like to keep running or do you enter the building: ")
            if answer == "keep running":
                print("You keep running and end up in and allyway with no exits and the monster catches up with you, You died")
            elif answer == "enter the building":
                print("you enter the building and sucessfully hide from the monster")
                answer = input("As you explore the building you come across a rickity staicase do you go down it or continue along the hallway: ")
                if answer == "go down it":
                    print("You make it down three stairs before the enitre thing collapase and you fall into the basement and suffer serious injury, You died")
                elif answer == "continue along the hallway":
                    print("You keep walking along the hallway when you hear a loud crack and you fall through the floor to your death, You died")
            else:
                print("You took to long to pick and was squished by the monster cahsing you, You died")
        else:
            print("The monster decided to keep you as a pet this is your life now")

    elif answer == "right":
        answer = input("You find a suietcase full of money would you like to leave it or pick it up: ")
        if answer == "leave it":
            print("You keep walking down the road")
            answer = input("As you keep walking you find that a man is following you would you like to run away of confront: ")
            if answer == "run away":
                print("You keep running untill you cant see the man anymore thats when you realize you have lost your winning lotto ticket, You lost")
            elif answer == "confront":
                print("As you confront the man he tells you that he was only trying to return your lotto ticket, You won")
            else:
                print("In your panicked state you steped out onto the road and got hit by a bus, You died")
        elif answer == "pick it up":
            print("You got caught stealing and are now in prison, You lost")


    else:
        print("You were indisiceve and got run over, You died")

else:
    print("That's to bad")