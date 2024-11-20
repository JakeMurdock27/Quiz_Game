print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")
score = 0

if playing.lower() != "yes":
    quit()


print("Okay! Let's play :)")

question_1 = input("What does CPU stand for? ")

if question_1.lower() == "central processing unit":
    print("That is correct!")
    score += 1
else:
    print("Sorry, that is not correct.")

question_2 = input("What does GPU stand for? ")

if question_2.lower() == "graphics processing unit":
    print("That is correct!")
    score += 1
else:
    print("Sorry, that is not correct.")

question_3 = input("What does RAM stand for? ")

if question_3.lower() == "random Access Memory":
    print("That is correct!")
    score += 1
else:
    print("Sorry, that is not correct.")

question_4 = input("What does PSU stand for? ")

if question_4.lower() == "power supply unit":
    print("That is correct!")
    score += 1
else:
    print("Sorry, that is not correct.")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "% correct!")
