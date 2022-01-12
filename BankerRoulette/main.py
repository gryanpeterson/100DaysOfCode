import random

names_string = input("Please enter everyone's name separated by commas. ")
split_string = names_string.split(", ")
random_list_number = random.randint(0, len(split_string) - 1)
print(f"{split_string[random_list_number]} is going to pay the bill today! ")