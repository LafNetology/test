class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.grades_list = []

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lect_grades:
                lecturer.lect_grades[course] += [grade]
            else:
                lecturer.lect_grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grade(self):
        for values in self.grades.values():
            for x in values:
                self.grades_list.append(x)

        if not len(self.grades_list):
            print("Нет оценок")
        else:
            res = sum(self.grades_list) / len(self.grades_list)
            return res

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {round(self.avg_grade(), 1)}' \
              f'\nКурсы в процессе изучения: {(", ").join(self.courses_in_progress)}' \
              f'\nЗавершенные курсы: {(", ").join(self.finished_courses)}'
        return res

    def __gt__(self, other):
        if not isinstance(other, Student):
            print("Такой студент не найден")
            return
        return self.avg_grade() > other.avg_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lect_grades = {}
        self.lect_grades_list = []

    def avg_lect_grade(self):
        for values in self.lect_grades.values():
            for i in values:
                self.lect_grades_list.append(i)

        if not len(self.lect_grades_list):
            print("Нет оценок")
        else:
            res = sum(self.lect_grades_list) / len(self.lect_grades_list)
            return res

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(self.avg_lect_grade(), 1)}'
        return res

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print("Такой лектор не найден")
            return
        return self.avg_lect_grade() > other.avg_lect_grade()


class Reviewer(Mentor):
    def __int__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование', 'Git', 'ООП']

worst_student = Student('Jack', 'Daniels', 'male')
worst_student.courses_in_progress += ['Python', 'Git', 'ООП']
worst_student.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python', 'Git', 'ООП']

nervous_reviewer = Reviewer('Edward', 'McGregor')
nervous_reviewer.courses_attached += ['Python', 'Git', 'ООП']

good_lecturer = Lecturer('Mike', 'Milky')
good_lecturer.courses_attached += ['Python', 'Git', 'ООП']

bad_lecturer = Lecturer('John', 'Bad')
bad_lecturer.courses_attached += ['Python', 'Git', 'ООП']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Git', 9)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_reviewer.rate_hw(worst_student, 'Python', 4)
cool_reviewer.rate_hw(worst_student, 'Git', 3)
cool_reviewer.rate_hw(worst_student, 'ООП', 4)

students = [best_student, worst_student]
lectors = [good_lecturer, bad_lecturer]

def avg_stud_grade_in_course(students, course):
    all_grades_in_course = []
    for x in students:
        if course in x.grades:
            for y in x.grades[course]:
                all_grades_in_course.append(y)
        avg_grade_in_course = round(sum(all_grades_in_course) / len(all_grades_in_course), 1)
    return avg_grade_in_course
    # не понимаю, как здесь прописать условие "else:" для несуществующих курсов,
    # постоянно получаю ошибку о неправильном отступе, хотя уже, кажется, все варианты перепробовала

print(best_student.grades)
print(worst_student.grades)
print(avg_stud_grade_in_course(students, 'Python'))


best_student.rate_hw(bad_lecturer, 'Python', 4)
best_student.rate_hw(bad_lecturer, 'Git', 6)
best_student.rate_hw(bad_lecturer, 'Python', 5)
best_student.rate_hw(good_lecturer, 'Python', 9)

worst_student.rate_hw(good_lecturer, 'Python', 7)
worst_student.rate_hw(good_lecturer, 'Python', 8)
worst_student.rate_hw(good_lecturer, 'Python', 6)
worst_student.rate_hw(bad_lecturer, 'ООП', 5)

def avg_lect_grade_in_course(lectors, course):
    all_grades_in_course = []
    for x in lectors:
        if course in x.lect_grades:
            for y in x.lect_grades[course]:
                all_grades_in_course.append(y)
        avg_grade_in_course = round(sum(all_grades_in_course) / len(all_grades_in_course), 1)
    return avg_grade_in_course


print(bad_lecturer.lect_grades)
print(good_lecturer.lect_grades)
print(avg_lect_grade_in_course(lectors, 'Python'))


print(best_student)
print(worst_student)
print(cool_reviewer)
print(nervous_reviewer)
print(bad_lecturer)
print(good_lecturer)
print(best_student < worst_student)
print(good_lecturer > bad_lecturer)
