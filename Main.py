# User inputs score and par for course
# Check input for content or mistakes
# Parse the input with space as delimiter, so a list of strings will be made
# Cast each string to an int (no decimals) ** Will I need to make a new list to store casted values?
# Calculate 2 different things: Scoring average, and handicap, and return that to the user

print("\n---***--- Scoring Average and Handicap Calculator ---***---\n")

user_input = input("Welcome to the app! You will enter your score, followed by par for the course.\n"
                   "Press enter to begin! ")

scores = []
courses_par = []

run = True
while run:
    score = ""
    while score == "":
        try:
            score = int(input("\nEnter your score: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
    scores.append(score)

    par = ""
    while par == "":
        try:
            par = int(input("What was par for the course?: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
    courses_par.append(par)

    keep_on = True
    while keep_on:
        choice = input("Would you like to enter another score? Y/N: ")
        if choice.upper() == "N":
            keep_on = False
            run = False
        elif choice.upper() == "Y":
            keep_on = False
        else:
            print("Invalid choice. Try again.")

sum_of_scores = 0
for x in scores:
    sum_of_scores += x
scoring_avg = sum_of_scores / len(scores)

# Handicap = your average amount over or under par
# A handicap under par has a + preceding the value
to_par_list = []
for x in range(len(scores)):
    to_par_list.append(scores[x] - courses_par[x])
to_par_sum = 0
for x in to_par_list:
    to_par_sum += x
handicap = to_par_sum / len(to_par_list)
handicap_below_par = False
if handicap < 0:
    handicap_below_par = True


print("\n******************************\n")
print(f"Scoring Average: {scoring_avg:.1f}")
if handicap_below_par:
    print(f"Handicap: +{abs(handicap):.1f}")
else:
    print(f"Handicap: {handicap}")
print("\n******************************")

# print(scores)
# print(courses_par)




