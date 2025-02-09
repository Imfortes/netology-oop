class Student:
    """
    Конструктор класса Student.
    :param name: Имя студента
    :param surname: Фамилия студента
    :param gender: Пол студента
    :param finished_courses: Список законченных курсов
    :param courses_in_progress: Список текущих курсов
    :param grades: Словарь (предмет: оценки) от преподавателей
    :param ratings: Словарь оценки лекции (предмет: оценки) от ученика преподавателям
    :param average_grade: Средняя оценка
    :param student_list: Список всех экземпляров класса студент
    """

    student_list = []

    def __init__(self, name, surname, gender='Не указан'):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.ratings = {}
        self.average_grade = 0
        self.student_list.append(self)

    def add_courses_in_progress(self, *courses):
        if not courses:
            return False
        self.courses_in_progress.extend(courses)

    def add_finished_courses(self, *courses):
        if not courses:
            return False
        self.finished_courses.extend(courses)

    def rate_lectors(self, course, lecturer, rating):
        if (
            course in self.courses_in_progress and
            isinstance(lecturer, Lectures) and
            course in lecturer.courses_attached and
            0 <= rating <= 10
        ):
            lecturer.ratings.setdefault(course, []).append(rating) 
        else:
            return 'Ошибка: Невозможно выставить оценку'

    def average_grades(self):
        if not self.grades:
            return 0
        total_sum = sum(sum(grades) for grades in self.grades.values())
        total_count = sum(len(grades) for grades in self.grades.values())
        self.average_grade = total_sum / total_count if total_count != 0 else 0
        return self.average_grade

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Сравниваем не студентов')
            return
        return self.average_grade < other.average_grade

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Сравниваем не студентов')
            return
        return self.average_grade > other.average_grade

    def __str__(self):
        courses_in_progress = ", ".join(self.courses_in_progress) if self.courses_in_progress else "Нет курсов в процессе"
        finished_courses = ", ".join(self.finished_courses) if self.finished_courses else "Нет завершенных курсов"

        return (f'Студент:\n'
                f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_grades():.2f}\n'
                f'Курсы в процессе изучения: {courses_in_progress}\n'
                f'Завершенные курсы: {finished_courses}\n')
    
class Mentor:
    mentor_list = []
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.mentor_list.append(self)
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def add_courses_in_attached(self, *courses):
        if not courses:
            return False
        self.courses_attached.extend(courses)

    def __str__(self):
        return (
            f'Ментор:\n'
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Закреплен к курсам: {", ".join(self.courses_attached)}\n'
            )
        
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return (
            f'Ревьюер:\n'
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Закреплен к курсам: {", ".join(self.courses_attached)}\n'
            )

class Lectures(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.ratings = {}  
        self.courses_attached = []  
        self.average_grade = 0

    def average_grades(self):
        if not self.ratings:  
            return 0
        total_sum = sum(sum(grades) for grades in self.ratings.values()) 
        total_count = sum(len(grades) for grades in self.ratings.values()) 
        self.average_grade = total_sum / total_count if total_count != 0 else 0
        return self.average_grade

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Сравниваем не студентов')
            return
        return self.average_grade < other.average_grade

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Сравниваем не студентов')
            return
        return self.average_grade > other.average_grade

    def __str__(self):
        courses_attached = ", ".join(self.courses_attached) if self.courses_attached else "Нет закрепленных курсов"
        return (f'Лектор:\n'
                f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_grades():.2f}\n'
                f'Закреплен к курсам: {courses_attached}\n')



# 

lecturer_1 = Lectures('Иван', 'Васильев')
lecturer_2 = Lectures('Петр', 'Сергеев')
reviewer_1 = Reviewer('Яна', 'Сидорова')
reviewer_2 = Reviewer('Екатерина', 'Иванова')
student_1 = Student('Артем', 'Ученый')
student_2 = Student('Андрей', 'Великий')

# 

student_1.add_courses_in_progress("Дата-сайентист", "Машинное обучение инженер", "Инженер по данным", "Архитектор программного обеспечения")
student_1.add_finished_courses("Программист", "Веб-разработчик", "Mobile-разработчик", "DevOps-инженер", "Системный администратор", "Тестировщик ПО", "Бизнес-аналитик")
student_2.add_courses_in_progress("Дата-сайентист", "Машинное обучение инженер", "Инженер по данным", "Архитектор программного обеспечения", "Cybersecurity специалист")
student_2.add_finished_courses("Cloud-инженер", "Product Manager", "UX/UI дизайнер", "Специалист по информационной безопасности", "Frontend-разработчик", "Backend-разработчик", "Full-stack разработчик", "Специалист по базам данных")

lecturer_1.add_courses_in_attached("Дата-сайентист", "Машинное обучение инженер", "Инженер по данным", "Архитектор программного обеспечения", "Cybersecurity специалист", "Product Manager", "UX/UI дизайнер", "Специалист по информационной безопасности")
lecturer_2.add_courses_in_attached("Дата-сайентист", "Машинное обучение инженер", "Инженер по данным", "Архитектор программного обеспечения", "Cybersecurity специалист", "Product Manager", "UX/UI дизайнер", "Специалист по информационной безопасности")
reviewer_1.add_courses_in_attached("Дата-сайентист", "Машинное обучение инженер", "Инженер по данным", "Архитектор программного обеспечения", "Cybersecurity специалист", "Product Manager", "UX/UI дизайнер", "Специалист по информационной безопасности")
reviewer_2.add_courses_in_attached("Дата-сайентист", "Машинное обучение инженер", "Инженер по данным", "Архитектор программного обеспечения", "Cybersecurity специалист", "Product Manager", "UX/UI дизайнер", "Специалист по информационной безопасности")

# 

reviewer_1.rate_hw(student_1, 'Дата-сайентист', 8)
reviewer_1.rate_hw(student_1, 'Машинное обучение инженер', 8)
reviewer_1.rate_hw(student_1, 'Инженер по данным', 8)
reviewer_1.rate_hw(student_1, 'Архитектор программного обеспечения', 8)

reviewer_2.rate_hw(student_1, 'Дата-сайентист', 10)
reviewer_2.rate_hw(student_1, 'Машинное обучение инженер', 9)
reviewer_2.rate_hw(student_1, 'Инженер по данным', 10)
reviewer_2.rate_hw(student_1, 'Архитектор программного обеспечения', 9)

lecturer_1.rate_hw(student_1, 'Дата-сайентист', 6)
lecturer_1.rate_hw(student_1, 'Машинное обучение инженер', 7)
lecturer_1.rate_hw(student_1, 'Инженер по данным', 8)
lecturer_1.rate_hw(student_1, 'Архитектор программного обеспечения', 9)

lecturer_2.rate_hw(student_1, 'Дата-сайентист', 10)
lecturer_2.rate_hw(student_1, 'Машинное обучение инженер', 9)
lecturer_2.rate_hw(student_1, 'Инженер по данным', 8)
lecturer_2.rate_hw(student_1, 'Архитектор программного обеспечения', 7)

student_1.rate_lectors('Дата-сайентист', lecturer_1, 8)
student_1.rate_lectors('Машинное обучение инженер', lecturer_1, 9)
student_1.rate_lectors('Инженер по данным', lecturer_1, 10)
student_1.rate_lectors('Архитектор программного обеспечения', lecturer_1, 7)

student_1.rate_lectors('Дата-сайентист', lecturer_2, 6)
student_1.rate_lectors('Машинное обучение инженер', lecturer_2, 9)
student_1.rate_lectors('Инженер по данным', lecturer_2, 7)
student_1.rate_lectors('Архитектор программного обеспечения', lecturer_2, 8)

student_2.rate_lectors('Дата-сайентист', lecturer_1, 8)
student_2.rate_lectors('Машинное обучение инженер', lecturer_1, 9)
student_2.rate_lectors('Инженер по данным', lecturer_1, 10)
student_2.rate_lectors('Архитектор программного обеспечения', lecturer_1, 7)
student_2.rate_lectors('Cybersecurity специалист', lecturer_1, 7)

student_2.rate_lectors('Дата-сайентист', lecturer_2, 6)
student_2.rate_lectors('Машинное обучение инженер', lecturer_2, 9)
student_2.rate_lectors('Инженер по данным', lecturer_2, 7)
student_2.rate_lectors('Архитектор программного обеспечения', lecturer_2, 8)
student_2.rate_lectors('Cybersecurity специалист', lecturer_2, 8)

# 

reviewer_1.rate_hw(student_2, 'Дата-сайентист', 8)
reviewer_1.rate_hw(student_2, 'Машинное обучение инженер', 8)
reviewer_1.rate_hw(student_2, 'Инженер по данным', 8)
reviewer_1.rate_hw(student_2, 'Архитектор программного обеспечения', 8)
reviewer_1.rate_hw(student_2, 'Cybersecurity специалист', 8)

reviewer_2.rate_hw(student_2, 'Дата-сайентист', 10)
reviewer_2.rate_hw(student_2, 'Машинное обучение инженер', 9)
reviewer_2.rate_hw(student_2, 'Инженер по данным', 10)
reviewer_2.rate_hw(student_2, 'Архитектор программного обеспечения', 9)
reviewer_2.rate_hw(student_2, 'Cybersecurity специалист', 9)

lecturer_1.rate_hw(student_2, 'Дата-сайентист', 6)
lecturer_1.rate_hw(student_2, 'Машинное обучение инженер', 7)
lecturer_1.rate_hw(student_2, 'Инженер по данным', 8)
lecturer_1.rate_hw(student_2, 'Архитектор программного обеспечения', 9)
lecturer_1.rate_hw(student_2, 'Cybersecurity специалист', 9)

lecturer_2.rate_hw(student_2, 'Дата-сайентист', 10)
lecturer_2.rate_hw(student_2, 'Машинное обучение инженер', 9)
lecturer_2.rate_hw(student_2, 'Инженер по данным', 8)
lecturer_2.rate_hw(student_2, 'Архитектор программного обеспечения', 7)
lecturer_2.rate_hw(student_2, 'Cybersecurity специалист', 7)

# 

print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)
print(student_1)
print(student_2)

# 

def calc_average_students(students, course):
    student_courses = []
    for student in students:
        for k, v in student.grades.items():
            if k == course:
                student_courses.extend(v)
    summa = sum(student_courses)
    average_grade = summa / len(student_courses)
    return average_grade

def calc_average_lectures(lectures, course):
    lecture_courses = []
    for lecture in lectures:
        if isinstance(lecture, Lectures) and course in lecture.ratings:
            lecture_courses.extend(lecture.ratings[course])
    
    if not lecture_courses:  
        return 0  
    
    summa = sum(lecture_courses)
    average_grade = summa / len(lecture_courses)
    return average_grade

print(f'Средняя оценка за ДЗ по всем студентам курса "Дата-сайентист": {calc_average_students(Student.student_list, 'Дата-сайентист')}')
print(f'Средняя оценка за ДЗ по всем студентам курса "Инженер по данным": {calc_average_students(Student.student_list, 'Инженер по данным')}')
print(f'Средняя оценка за ДЗ по всем студентам курса "Cybersecurity специалист": {calc_average_students(Student.student_list, 'Cybersecurity специалист')}')

print(f'Средняя оценка за лекции по всем лекторам курса "Дата-сайентист": {calc_average_lectures(Mentor.mentor_list, "Дата-сайентист")}')
print(f'Средняя оценка за лекции по всем лекторам курса "Инженер по данным": {calc_average_lectures(Mentor.mentor_list, "Инженер по данным")}')
print(f'Средняя оценка за лекции по всем лекторам курса "Cybersecurity специалист": {calc_average_lectures(Mentor.mentor_list, "Cybersecurity специалист")}')

# reviewer = Reviewer('Uniq', 'Reviewer')
# reviewer.courses_attached += ['Python']
# reviewer.rate_hw(best_student, 'Python', 2)
# reviewer.rate_hw(best_student, 'Python', 3)
# reviewer.rate_hw(best_student, 'Python', 6)

# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']

# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 9)
# cool_mentor.rate_hw(best_student, 'Python', 8)

# print(best_student)

#     # Создаем объекты
# student = Student('Ivan', 'Petrov', 'male')
# lecturer = Lectures('Anna', 'Smirnova')

# # Настройка курсов
# student.add_courses_in_progress('Python', 'Math', 'English')
# lecturer.courses_attached = ['Python', 'Math']

# # Выставляем оценки лектору
# student.rate_lectors('Python', lecturer, 9)
# student.rate_lectors('Python', lecturer, 8)
# student.rate_lectors('Math', lecturer, 7)

# cool_mentor.rate_hw(student, 'Python', 10)
# cool_mentor.rate_hw(student, 'Python', 9)
# cool_mentor.rate_hw(student, 'Python', 8)
# cool_mentor.rate_hw(student, 'Math', 8)



# # Создаем объект лектора
# lecturer_1 = Lectures('Ivan', 'Petrov')
# lecturer_1.courses_attached = ['Python', 'Math']

# # Вызываем функцию для выставления оценок
# student.rate_lectors('Python', lecturer_1, 9)
# student.rate_lectors('Python', lecturer_1, 8)
# student.rate_lectors('Math', lecturer_1, 7)


# # Проверяем результат
# print(lecturer)
# print(student)
# print(lecturer_1)
# print(reviewer)
# print(best_student < student)
# print(best_student > student)

