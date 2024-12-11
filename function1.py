# Calculate Average Marks
def AverageMarks(marks):
    Sum = sum(marks)
    Average = Sum/5
    print("Average marks is", Average)
    return Average

# Find Grade and Return    
def FindGrade(Average):
    if Average >= 80 :
        grade = 'A'
    elif Average < 80 and Average >= 60 :
        grade = 'B'
    elif Average < 60 and Average >= 50 :
        grade = 'C'
    else :
       grade = 'F'
    return grade

marks = [55,64,75,80,65]
Average = AverageMarks(marks)
grade = FindGrade(Average)
print("Your Grade is ", grade)