#Author: Shikha Patel 
#Homework Number & Name: Homework 4 Grade Calculator
#Due Date: October 4, 2022
#Program Description:  The program determines a student’s grade in MIS 304. User will enter grades for each of the 5 grades for MIS 304 (see table below). Your program will validate inputs, calculate numeric average and letter grade. 
    
# define 5 global constants for the weights for each grade
weight_exam1 = 0.20
weight_exam2 = 0.20
weight_exam3 = 0.20
weight_homework = 0.30
weight_final = 0.10

#define function to query input
def get_grade(assignment_name): 
    
    #queries the user for a grade 
    assignment_grade = float(input("What is your grade for " +  assignment_name + "? "))
    
    #validates if the grade is in the correct range
    while not 0 <=  assignment_grade <= 100: 
        print("Grade must be a number between 0 and 100")
        
        #query the user again if the input is invalid
        assignment_grade = float(input("What is your grade for " +  assignment_name + "? "))
    
    #return the valid grade that the user inputs
    return assignment_grade
        
#define function to calculate numeric average
def calc_average(exam_1, exam_2, exam_3, homework, final): 
    
    #calculate the course grade using the weights
    weighted_average = (exam_1 * weight_exam1) + (exam_2 * weight_exam2) + (exam_3 * weight_exam3) + (homework * weight_homework) + (final * weight_final)  
    
    #return the final numeric average
    return weighted_average
    
#define function to transform numeric average into letter grade
def calc_letter(average):
    #determine the final letter grade based on the following cutoffs
    if average >=89.5:
        return 'A'
    elif average >=79.5:
        return 'B'
    elif average >=69.5:
        return "C"
    elif average >=59.5:
        return "D"
    elif average <59.5:
        return "F"
    
    #return the corresponding letter grade.
    
#define main function
def main(): 
    
    #call the functions defined above
    exam_1 = get_grade("Exam 1")
    exam_2 = get_grade("Exam 2")
    exam_3 = get_grade("Exam 3")
    homework = get_grade("Homework")
    final = get_grade("Final Project")
    average = calc_average(exam_1, exam_2, exam_3, homework, final)
    letter = calc_letter(average)
    
    #display the final results
    print("Final Numeric Grade:", format(average, '.2f'))
    print("Final Letter Grade:",letter)

    
#call main
main()
       

    