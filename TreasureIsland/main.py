print("Welcome to Treasure Island. Your mission is to find the treasure. \n")
left_right = input("You arrive on the beach and enter the mainland. You find and path and come to a fork in the road. \nWill you go LEFT or RIGHT? ")
left_right_lower = left_right.lower()

if left_right_lower == "left":
    swim_wait = input("You have selected the correct path. You follow the path to a lake. \nWill you SWIM or WAIT? ")
    swim_wait_lower = swim_wait.lower()
    if swim_wait_lower == "wait":
        red_blue_yellow = input("You waited and found a boat to take you to the other side of the lake. \nYou find and enter the temple and see three different color doors. What door will you choose? RED, BLUE, or YELLOW? ")
        red_blue_yellow_lower = red_blue_yellow.lower()
        if red_blue_yellow_lower == "yellow":
            print("You selected the correct door and find the hidden treasure behind the door. ")
        elif red_blue_yellow_lower == "blue":
            print("You were eaten by beasts. GAME OVER! ")
        elif red_blue_yellow_lower == "red":
            print("You were burned by fire. GAME OVER! ")
        else:
            print("You fell into a pit full of poisonous snakes. GAME OVER! ")
    else:
        print("You were attacked and killed by sharks with friggin' laser beams attached to their friggin' heads. ")
else:
    print("You fell into a hole. GAME OVER! ")






