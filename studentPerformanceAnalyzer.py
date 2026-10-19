# Task 1: Creating a KCAStudent Class

class KCAStudent:
    def __init__(self, student_id, fname, lname, math, english, science):
        self.student_id = student_id
        self.fname = fname
        self.lname = lname
        self.math = math
        self.english = english
        self.science = science
# Adding calculate_average()
    def calculate_average(self):    
        total_score = self.math + self.english + self.science
        average_score = total_score / 3
        return average_score 

# Adding get_grade()
    def get_grade(self):
        average_score = self.calculate_average()
        if average_score >= 70:
            return 'A'
        elif average_score >= 60:
            return 'B'
        elif average_score >= 50:
            return 'C'
        elif average_score >= 40:
            return 'D'
        else:
            return 'F'

# Instantiating KCAStudent objects for testing:
#KCAStudent1 = KCAStudent(1, "John", "Doe", 25, 18, 32)
#print(f"Average Score for {KCAStudent1.fname} {KCAStudent1.lname}: {KCAStudent1.calculate_average()}")
#print(f"Grade for {KCAStudent1.fname} {KCAStudent1.lname}: {KCAStudent1.get_grade()}")

# Task 3: Creating a PerformanceAnalyzer Class

class PerformanceAnalyzer:
    def __init__(self, students):
        self.students = students
# Adding highest_average() using max() function
    def highest_average(self):
        highest_average = max(
            self.students, 
            key=lambda student: student.calculate_average())
        return highest_average

# Adding lowest_average() using min() function
    def lowest_average(self):
        lowest_average = min(
            self.students, 
            key=lambda student: student.calculate_average())
        return lowest_average

# Adding class_average() 
    def class_average(self):
        total_average = sum(
            student.calculate_average() 
            for student in self.students)
        class_average = total_average / len(self.students)
        return class_average

# Testing the PerformanceAnalyzer class with KCAStudent objects
#KCAStudent1 = KCAStudent(1, "John", "Doe", 25, 18, 32)
#KCAStudent2 = KCAStudent(2, "Jane", "Smith", 45, 55, 65)
#KCAStudent3 = KCAStudent(3, "Alice", "Johnson", 75, 85, 95)

#performanceAnalyzer = PerformanceAnalyzer([KCAStudent1, KCAStudent2, KCAStudent3])

#print(f"Highest Average: {performanceAnalyzer.highest_average().calculate_average()}")
#print(f"Lowest Average: {performanceAnalyzer.lowest_average().calculate_average()}")    
#print(f"Class Average: {performanceAnalyzer.class_average()}")


# Task 4: Applying Inheritance to Student-scholariship_amount classes

class ScholarshipStudent(KCAStudent):
    def __init__(self, student_id, fname, lname, math, english, science, scholarship_amount):
        super().__init__(student_id, fname, lname, math, english, science)
        self.scholarship_amount = scholarship_amount
    def is_eligible(self):
        average_score = self.calculate_average()
        if average_score >= 85:
            return "Yes"
        else:
            return "No"
# Testing the ScholarshipStudent class
#scholarship_student = ScholarshipStudent(1, "Emily", "Brown", 90, 75, 98, 10000)
#print(f"Is {scholarship_student.fname} {scholarship_student.lname} eligible for scholarship? {scholarship_student.is_eligible()}")
