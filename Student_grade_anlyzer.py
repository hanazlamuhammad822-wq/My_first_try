from itertools import count

students = [
    ("Ali", 85),
    ("Sara", 92),
    ("Ahmed", 78),
    ("Fatima", 95),
    ("Bilal", 88),
    ("Zara", 92),
    ("Omar", 76),
    ("Ayesha", 95)
]
grade=[grade for name, grade in students]
average=sum(grade)/len(grade)
print(average)
max_grade = max(grade)
for name, grade in students:
    if grade == max_grade:
        print(name, max_grade)

passing_students = [name for name, grade in students if grade >=80]
print("Passing_student",passing_students)
unique_grade =[grade for name, grade in students]
print(sorted(unique_grade))
Furequency_count={}
for name, grade in students:
    if grade in Furequency_count:
        Furequency_count[grade]+=1
    else:
        Furequency_count[grade] = 1
print(Furequency_count,end=" ")