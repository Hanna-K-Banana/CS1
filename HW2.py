import math
def main():
    #TODO: IF STATEMENT TO CHOOSE QUESTION AND LOOP
    PrintQuestionOne()
    PrintQuestionTwo()
    PrintQuestionThree()

def PrintQuestionOne():
    print("Enter input one.")
    user_num_1 = input()
    print("Enter input two.")
    user_num_2 = input()
    
    user_num_1 = int(user_num_1)   
    user_num_2 = int(user_num_2)

    for i in range(3):
        output = user_num_1 / user_num_2
        user_num_1 = output
        print(str(int(output)))
    
def PrintQuestionTwo():
    #TODO: OUTPUT TO TWO DECIMAL PLACES
    Question_answered = False
    while Question_answered == False:
        print("Enter miles per gallon.")
        miles_per_gallon = input()
        print("Enter cost of one gallon of gas in dollars.")
        dollars_per_gallon = input()
        print("Enter miles.")
        miles = input()

        miles_per_gallon = int(miles_per_gallon)
        dollars_per_gallon = int(dollars_per_gallon)
        miles = int(miles)
    
        cost_per_gallon = miles / miles_per_gallon * dollars_per_gallon
        print("Cost of", str(miles), "mile trip: ", str(cost_per_gallon), "dollars")

        print("Would you like to run again? Y or N")
        User_answer = input()
        if User_answer == 'N':
            Question_answered = True

def PrintQuestionThree():
    #TODO: OUTPUT DECIMAL PLACES TO TWO DIGITS
    x = input()
    y = input()
    z = input()

    print(float(x)**float(y))
    
    print(float(x)**(float(y)**float(z)))

    print(abs((float(x) - float(y))))
    ans = math.sqrt(float(x))**float(z)
    print(str(ans))
    
    
        
    


    
main()
