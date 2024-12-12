# Calculate Average Marks
def AverageMarks(marks,n):
    Sum = sum(marks)
    Average = Sum/n
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

marks = []
n = int(input("Enter the numbers of subject: "))
for i in range(n):
    marks.append(int(input("Enter the marks of subject "+str(i+1)+": ")))
Average = AverageMarks(marks,n)
grade = FindGrade(Average)
print("Your Grade is ", grade)
