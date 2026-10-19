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

    # Find the student with the highest average
    def highest_average(self):
        if not self.students:
            return None

        return max(
            self.students,
            key=lambda student: student.calculate_average()
        )

    # Find the student with the lowest average
    def lowest_average(self):
        if not self.students:
            return None

        return min(
            self.students,
            key=lambda student: student.calculate_average()
        )

    # Generate the performance report
    def generate_report(self, top_student, lowest_student, class_average,filename="performance_report.pdf"):
        if not self.students:
            print("No student records available.")
            return

        with open(filename, "w", encoding="utf-8") as file:
            file.write("STUDENT PERFORMANCE ANALYSIS REPORT\n")
            file.write("_" * 45 + "\n\n")

            file.write("A) INDIVIDUAL STUDENT PERFORMANCE\n")
            file.write("-" * 45 + "\n")

            for student in self.students:
                file.write(
                    f"Student ID: {student.student_id}\n"
                    f"Name: {student.fname} {student.lname}\n"
                    f"Maths: {student.math}\n"
                    f"English: {student.english}\n"
                    f"Science: {student.science}\n"
                    f"Average: {student.calculate_average()}\n"
                    f"Grade: {student.get_grade()}\n"
                    f"{'-' * 30}\n"
                )

            file.write("\nB) CLASS PERFORMANCE SUMMARY\n")
            file.write("-" * 45 + "\n")

            file.write(
                f"Top Performer: {top_student.fname} "
                f"{top_student.lname} "
                f"({top_student.calculate_average()})\n"
            )

            file.write(
                f"Lowest Performer: {lowest_student.fname} "
                f"{lowest_student.lname} "
                f"({lowest_student.calculate_average()})\n"
            )

            file.write(f"Class Average: {class_average:.2f}\n")

            file.write("\nSCHOLARSHIP ELIGIBILITY\n")
            file.write("-" * 45 + "\n")

            for student in self.students:
                eligible = student.calculate_average() >= 85
                status = "Yes" if eligible else "No"

                file.write(
                    f"{student.fname} {student.lname}: {status}\n"
                )

            file.write(
                "\nVisualization: student_performance_chart.png\n"
            )

        print(f"Report generated successfully: {filename}")

# Adding class_average() 
    def class_average(self):
        total_average = sum(
            student.calculate_average() 
            for student in self.students)
        class_average = total_average / len(self.students)
        return class_average

#Testing the PerformanceAnalyzer class with KCAStudent objects
KCAStudent1 = KCAStudent(1, "John", "Doe", 25, 18, 32)
KCAStudent2 = KCAStudent(2, "Jane", "Smith", 45, 55, 65)
KCAStudent3 = KCAStudent(3, "Alice", "Johnson", 75, 85, 95)

performanceAnalyzer = PerformanceAnalyzer([KCAStudent1, KCAStudent2, KCAStudent3])
performanceAnalyzer.generate_report(
    top_student=performanceAnalyzer.highest_average(),
    lowest_student=performanceAnalyzer.lowest_average(),
    class_average=performanceAnalyzer.class_average()
)


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
