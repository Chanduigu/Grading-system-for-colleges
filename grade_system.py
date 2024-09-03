number_of_subjects=input("Enter the number of subjects  that you have for this particular sem 5,6,7 or 8: ")
if number_of_subjects=="5":
    total_number_of_subjects=5
    print("Enter each subject marks to know your cgpa")
    sub1=int(input("Enter the subject one marks: "))
    sub2=int(input("Enter the subject two marks: "))
    sub3=int(input("Enter the subject three marks: "))
    sub4=int(input("Enter the subject four marks: "))
    sub5=int(input("Enter the subject five marks: "))
    percentage=((sub1+sub2+sub3+sub4+sub5)/total_number_of_subjects)
    conversion=0.095
    cgpa=percentage*conversion
    print("your cgpa: ",cgpa)
elif number_of_subjects=="6":
    total_number_of_subjects=6
    print("Enter each subject marks to know your cgpa")
    sub1=int(input("Enter the subject one marks: "))
    sub2=int(input("Enter the subject two marks: "))
    sub3=int(input("Enter the subject three marks: "))
    sub4=int(input("Enter the subject four marks: "))
    sub5=int(input("Enter the subject five marks: "))
    sub6=int(input("Enter the subject six marks: "))
    percentage=((sub1+sub2+sub3+sub4+sub5+sub6)/total_number_of_subjects)
    conversion=0.095
    cgpa=percentage*conversion
    print("your cgpa:" ,cgpa)
elif number_of_subjects=="7":
    total_number_of_subjects=7
    print("Enter each subject marks to know your cgpa")
    sub1=int(input("Enter the subject one marks: "))
    sub2=int(input("Enter the subject two marks: "))
    sub3=int(input("Enter the subject three marks: "))
    sub4=int(input("Enter the subject four marks: "))
    sub5=int(input("Enter the subject five marks: "))
    sub6=int(input("Enter the subject six marks: "))
    sub7=int(input("Enter the subject seven marks: "))
    percentage=((sub1+sub2+sub3+sub4+sub5+sub6+sub7)/total_number_of_subjects)
    conversion=0.095
    cgpa=percentage*conversion
    print("your cgpa:",cgpa)
elif number_of_subjects=="8":
    total_number_of_subjects=8
    print("Enter each subject marks to know your cgpa")
    sub1=int(input("Enter the subject one marks: "))
    sub2=int(input("Enter the subject two marks: "))
    sub3=int(input("Enter the subject three marks: "))
    sub4=int(input("Enter the subject four marks: "))
    sub5=int(input("Enter the subject five marks: "))
    sub6=int(input("Enter the subject six marks: "))
    sub7=int(input("Enter the subject seven marks: "))
    sub8=int(input("Enter the subject eight marks: "))
    percentage=((sub1+sub2+sub3+sub4+sub5+sub6+sub7+sub8)/total_number_of_subjects)
    conversion=0.095
    cgpa=percentage*conversion
    print(f"Your CGPA:",cgpa)


else:
    print ("invalid")
if 9<= cgpa  <10:
    print("Oustanding")
elif 8<= cgpa  <9:
    print("A+")
elif 7<= cgpa  <8:
    print("A")
elif 6<= cgpa  <7:
    print("B")
elif 5<= cgpa  <6:
    print("C")
elif 4<= cgpa  <5:
    print("D")
else:
    print("Fail")
