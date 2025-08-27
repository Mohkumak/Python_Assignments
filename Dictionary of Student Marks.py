
university_results = {'mohit': 45,'Rohit': 55, 'Amber' : 65,'Tarang': 75, 'Ravi': 85}
student_name = input("enter the student's name:  ")
if student_name in university_results:
    print(f"{student_name}'s Marks: {university_results['student_name']}")
else:
    print(f"{student_name} is not found")


# list slicing.....

original_list = [1,2,3,4,5,6,7,8,9,10]
extracted = original_list[0:5]
reversed_list = extracted[::-1]
print(f"Extracted first five elements: {extracted}")
print(f"Reversed extracted value: {reversed_list}")
      