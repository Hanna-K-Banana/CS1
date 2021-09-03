import math
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
    print("Write a program using integers user_num and x as input,")
    print("and output user_num divided by x three times.")
    print()
    
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
    print("Write a program with a car's miles per gallon and gas")
    print("dollar per gallon (both floats) as input, and output")
    print("the gas cost for 20 miles, 75 miles, and 500 miles.")
    print("Output each floating point value with 2 digit after the decimal.")
    print()
          
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
        format_cost_per_gallon = "{:.2f}".format(cost_per_gallon)
        print("Cost of", str(miles), "mile trip: ", str(format_cost_per_gallon), "dollars")

        print("Would you like to run again? Y or N")
        User_answer = input()
        if User_answer == 'N':
            Question_answered = True

def PrintQuestionThree():
    print("Given three floating point values x, y, and z, output x")
    print("to the power of z, x to the power of (y to the power of z,)")
    print("the absolute value of x minus y, and the square root of x")
    print("to the power of z. Output each floating point value with")
    print("two digits after the decimal point.")
    print()
    
    print("Enter value for x.")
    x = input()
    print("Enter value for y.")
    y = input()
    print("Enter value for z.")
    z = input()

    print("x^z =")
    x_z = (float(x)**float(z))
    format_x_z = "{:.2f}".format(x_z)
    print(format_x_z)
    
    print("x^y^z =")
    x_y_z = (float(x)**(float(y)**float(z)))
    format_x_y_z = "{:.2f}".format(x_y_z)
    print(format_x_y_z)

    print("Absolute value of x - y =")
    abs_x_y = (abs((float(x) - float(y))))
    format_abs_x_y = "{:.2f}".format(abs_x_y)
    print(format_abs_x_y)
    
    print("Square root of x^z")
    sqrt_x_z = math.sqrt(float(x))**float(z)
    format_sqrt_x_z = "{:.2f}".format(sqrt_x_z)
    print(format_sqrt_x_z)
      
main()
