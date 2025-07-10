# Task 1: Check if a Number is Even or Odd
number = int(input("Enter a number: "))
if number % 2 != 0:
    print(f"{number} is an odd number.")
else:
    print(f"{number} is an even number.")



# assignment2-- task second
total_sum = 0
for number in range(1, 51):
    total_sum = total_sum + number
    print(f"The sum of numbers from 1 to 50 is : {total_sum}")

