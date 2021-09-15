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

print("Question 2.")
print("Given a highway number, indicate whether")
print("it is  a primary or auxiliary highway. If")
print("auxiliary, indicate what primary highway")
print("it serves. Also indicate if the (primary)")
print("highway runs north/south or east/west.")

highway_num = int(input())

elif highway_num >= 1 and highway_num <= 99:
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

