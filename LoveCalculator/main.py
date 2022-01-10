print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combined_names = name1.lower() + name2.lower()
true_count = 0
love_count = 0

if combined_names.count("t") > 0:
  true_count += combined_names.count("t")
if combined_names.count("r") > 0:
  true_count += combined_names.count("r")
if combined_names.count("u") > 0:
  true_count += combined_names.count("u")
if combined_names.count("e") > 0:
  true_count += combined_names.count("e")

if combined_names.count("l") > 0:
  love_count += combined_names.count("l")
if combined_names.count("o") > 0:
  love_count += combined_names.count("o")
if combined_names.count("v") > 0:
  love_count += combined_names.count("v")
if combined_names.count("e") > 0:
  love_count += combined_names.count("e")

true_count_as_string = str(true_count)
love_count_as_string = str(love_count)
love_score = int(true_count_as_string + love_count_as_string)

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos. ")
elif love_score >= 40 and love_score <= 50:
  print(f"Your score is {love_score}, you are alright together. ")
else:
  print(f"Your score is {love_score}. ")