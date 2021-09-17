
#Main Method takes no arguments and runs homework 4
def main():
    print("Welcome to Hanna's homework!")
    #Set conditional for while loop
    DoneLooking = False

    while DoneLooking == False:
        print("Would you like to see question one, two, or three? Press 1, 2, or 3 and hit Enter.")
        userChoice = input()
        #change user choice to an integer to evaluate which question to go to
        userChoice = int(userChoice)

        if userChoice == 1:
            RunQuestionOne()
        elif userChoice == 2:
            RunQuestionTwo()
        elif userChoice == 3:
            RunQuestionThree()
        else:
            print("You did not enter a valid choice")

        print("Do you want to see another question? Enter Y for yes and N for no.")
        goAgain = input()
        if goAgain == 'N':
            DoneLooking = True

    print("Goodbye!")

#RunQuestionOne is a function that takes three integers and sorts them
#with a type of bubble sort for three numbers and then prints from smallest to largest
def RunQuestionOne():
    print("Question 1.")
    print("Enter 3 numbers to sort from smallest to")
    print("largest: (press enter after each number)")

    input_1 = int(input())
    input_2 = int(input())
    input_3 = int(input())

    nums_sorted = False

    while nums_sorted == False :
        if input_1 > input_2:
            input_1, input_2 = input_2, input_1

        elif input_2 > input_3:
            input_2, input_3 = input_3, input_2
        
        elif input_1 < input_2 and input_2 < input_3:
            nums_sorted = True
    
    print(str(input_1), str(input_2), str(input_3))


def RunQuestionTwo():
    print("Question 2.")
    print("Given a highway number, indicate whether")
    print("it is  a primary or auxiliary highway. If")
    print("auxiliary, indicate what primary highway")
    print("it serves. Also indicate if the (primary)")
    print("highway runs north/south or east/west.")

    #input sanitization 
    valid_input = False
    while valid_input == False:
        print("Please enter the highway number you would like to look up.")
        highway_num = int(input())
        zeroChecker = str(highway_num)
        zeros = "00"
    
        if zeros in zeroChecker:
            print("That is not a valid input, please try again.")
        elif highway_num == 0:
            print("That is not a valid input, please try again.")
        else:
            #exit while loop
            valid_input = True

    if highway_num >= 1 and highway_num <= 99:
        print("I-" + str(highway_num) + " is primary.")
    
        if highway_num % 2 == 0:
            print("It goes east/west.")
        else:
            print("It goes north/south.")
    
    elif highway_num >= 100 and highway_num <= 999:
        print("I-" + str(highway_num) + " is auxiliary.")
    
        hwy_num_str = str(highway_num)
        hwy_num_length = len(hwy_num_str)
        last_two_digits = int(hwy_num_str[hwy_num_length - 2: hwy_num_length])

        if highway_num % 2 == 0:
            print("It serves I-" + str(last_two_digits) + " which goes east/west.")
        else:
            print("It serves I-" + str(last_two_digits) + " which goes north/south.")


def RunQuestionThree():
    # given change amount output fewest coins
        #dollars, nickels, quarters, dimes, pennies
    print("Enter total change amount")
    change = int(input())

    dollar = 0
    quarter = 0
    dime = 0
    nickel = 0
    penny = 0

    dollarString = ""
    quarterString = ""
    dimeString = ""
    nickelString = ""
    pennyString = ""
    

    if change / 100 >= 1:
        dollar = change // 100
        change -= dollar * 100
    if change / 25 >= 1:
        quarter = change // 25
        change -= quarter * 25 
    if change / 10 >= 1:
        dime = change // 10
        change -= dime * 10
    if change / 5 >= 1:
        nickel = change // 5
        change -= nickel * 5
    penny = change

    if dollar == 1:
        dollarString = " Dollar, "
    else:
        dollarString = " Dollars, "
    if quarter == 1:
        quarterString = " Quarter, "
    else:
        quarterString = " Quarters, "
    if dime == 1:
        dimeString = " Dime, "
    else:
        dimeString = " Dimes, "
    if nickel == 1:
        nickelString = " Nickel, "
    else:
        nickelString = " Nickels, "
    if penny == 1:
        pennyString = " Penny. "
    else:
        pennyString = " Pennies. "
    
    print(str(dollar) + dollarString + str(quarter) + quarterString + str(dime) + dimeString + str(nickel) + nickelString + str(penny) + pennyString)


main()
