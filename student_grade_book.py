class Student:
    def __init__(self, student_id, name, grades):
        self.student_id = student_id
        self.name = name
        self.grades = grades

    def get_grades(self):
        return self.grades

    def update_grade(self, subject_index, new_grade):
        if 0 <= subject_index < len(self.grades):
            self.grades[subject_index] = new_grade

    def __str__(self):
        return f"{self.name} (ID: {self.student_id}): {self.grades}"

class GradeBook:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, grades):
        self.students[student_id] = Student(student_id, name, grades)
        print(f"{name} Student with ID {student_id} added.")

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print(f"Student with ID {student_id} removed.")

    def update_student_grade(self, student_id, subject_index, new_grade):
        if student_id in self.students:
            self.students[student_id].update_grade(subject_index, new_grade)

    def display_grades(self):
        for student_id, student in self.students.items():
            print(student)
            print(f"Highest Grade: {max(student.grades)}")
            print(f"Lowest Grade: {min(student.grades)}")

    def calculate_averages(self):
        for student_id, student in self.students.items():
            avg_grade = sum(student.grades) / len(student.grades)
            print(f"{student.name} (ID: {student_id}) Average Grade: {avg_grade}")

        num_subjects = len(next(iter(self.students.values())).grades)
        class_averages = [0] * num_subjects
        for student in self.students.values():
            for i in range(num_subjects):
                class_averages[i] += student.grades[i]
        class_averages = [total / len(self.students) for total in class_averages]
        print(f"Class Averages per Subject: {class_averages}")

    def compare_averages(self):
        num_subjects = len(next(iter(self.students.values())).grades)
        class_averages = [0] * num_subjects
        for student in self.students.values():
            for i in range(num_subjects):
                class_averages[i] += student.grades[i]
        class_averages = [total / len(self.students) for total in class_averages]

        for student_id, student in self.students.items():
            avg_grade = sum(student.grades) / len(student.grades)
            class_avg = sum(class_averages) / len(class_averages)
            comparison = "equal to"
            if avg_grade > class_avg:
                comparison = "above"
            elif avg_grade < class_avg:
                comparison = "below"
            print(f"{student.name} (ID: {student_id}) is {comparison} the class average.")


grade_book = GradeBook()
grade_book.add_student(18, "Auwal",grades=[90, 85, 88, 92, 95])
grade_book.add_student(19, "Bashir",grades=[85, 80, 90, 95, 88])
grade_book.add_student(20, "Yipmong",grades=[92, 98, 90, 85, 95])
grade_book.add_student(21, "Okolene",grades=[92, 68, 70, 85, 95])
grade_book.add_student(22, "Moses",grades=[80, 65, 88, 82, 75])

grade_book.display_grades()
grade_book.calculate_averages()
grade_book.compare_averages()
grade_book.update_student_grade(18, 2, 95)
grade_book.display_grades()
grade_book.calculate_averages()
grade_book.compare_averages()
grade_book.remove_student(19)
grade_book.remove_student(22)
grade_book.remove_student(20)
grade_book.display_grades()
grade_book.calculate_averages()
grade_book.compare_averages()


