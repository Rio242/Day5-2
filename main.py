# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

#initilize new variable
high_score = 0

# for loop to sort through student scores
for score in student_scores:
  # if current score is greater than previous that value is stored until end of list
  if score > high_score:
    high_score = score
    
# print out final highest score 
print(f"The highest score in the list is {high_score}")
  