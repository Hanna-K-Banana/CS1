print("Question 1.")
print()

print("Enter caffiene levels in mg to find")
print("caffiene levels after, six, twelve")
print("and twenty-four hours.")

caffeine_in_mg = int(input())

after_six_hours = caffeine_in_mg / 2
after_twelve_hours = after_six_hours / 2
after_twentyfour_hours = after_twelve_hours / 2

print('{:.2f}'.format(after_six_hours))
print('{:.2f}'.format(after_twelve_hours))
print('{:.2f}'.format(after_twentyfour_hours))

print()
print("Question 2.")
print()

print("Enter current price.")
current_price = int(input())
print("Enter price last month.")
price_last_month = int(input())
change_from_last_month = current_price - price_last_month
estimated_monthly_mortgage = (current_price * 0.051) / 12
print("This house is $" + str('{:.2f}'.format(current_price)) + ". The change is")
print("$" + str('{:.2f}'.format(change_from_last_month)) + " since last month.")
print("The estimated monthly mortgage is $" + '{:.2f}'.format(estimated_monthly_mortgage))

print()
print("Question 3.")
print()

print("Enter input 1.")
input_1 = float(input())
print("Enter input 2.")
input_2 = float(input())
print("Enter input 3.")
input_3 = float(input())
print("Enter input 4.")
input_4 = float(input())

product = input_1 * input_2 * input_3 * input_4
average = (input_1 + input_2 + input_3 + input_4) / 4

integer_product = int(product)
integer_average = int(average)
float_product = float(product)
float_average = float(average)

print('{:.0f}'.format(integer_product))
print('{:.0f}'.format(integer_average))
print('{:.3f}'.format(float_product))
print('{:.3f}'.format(float_average))

