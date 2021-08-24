def main():
    print("Welcome to Hanna's Homework.")

    Choose_other_question = True
    
    while Choose_other_question == True:
        print("Would you like to see question one, two, or three? (enter 1, 2, or 3)")
        User_choice = int(input())
        
        if User_choice == 1:
            PrintQuestionOne()
        elif User_choice == 2:
            PrintQuestionTwo()
        elif User_choice == 3:
            PrintQuestionThree()
        else:
            print("Press 1, 2, or 3.")

        print("Do you want to see another question?")
        print("Enter Y for yes, enter N for no.")
        yes_or_no = input()

        if yes_or_no == 'N':
            Choose_other_question = False
    print("Goodbye.")
        
def PrintQuestionOne():
    print("(Display three messages) Write a program that displays")
    print("Welcome to Python, Welcome to Computer Science, and Programming is fun.")
    print("Hanna's answer :")
    print("\tWelcome to Python")
    print("\tWelcome to Computer Science")
    print("\tProgramming is fun.")

def PrintQuestionTwo():
    print("(Summation of a series) Write a program that displays")
    print("the result of 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9.")
    print("Hanna's answer :")
    Result = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
    print("\t" + str(Result))

def PrintQuestionThree():
    print("(Average speed in kilometers) Assume a runner runs 24")
    print("miles in 1 hour, 40 minutes, and 35 seconds. Write a")
    print("program that displays the average speed in kilometers")
    print("per hour.")
    print("Note that 1 mile is 1.6 kilometers.")
    print("Hanna's answer :")
    hours = 1
    minutes = 40
    seconds = 35
    distance_in_miles = 24
    distance_in_kilometers = distance_in_miles * 1.6
    time_in_minutes = hours * 60 + minutes + seconds / 60
    kilometers_per_hour = 60 * distance_in_kilometers / time_in_minutes
    print("\t" + str(kilometers_per_hour),"KPH")

main()
