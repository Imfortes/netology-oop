class Student:
    """
        Конструктор класса Student.

        :param name: Имя студента
        :param surname: Фамилия студента
        :param gender: Пол студента
        :param finished_courses: Список законченных курсов
        :param courses_in_progress: Список текущих курсов
        :param grades: Словарь (предмет: оценки) от преподавателей
        # :param ratings: Словарь оценки лекции(предмет: оценки) от ученика преподавателям
    """

    def __init__(self, name='Ivan', surname='Petrov', gender='unknown'):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        # self.ratings = {}

    def add_courses_in_progress(self, *courses):
        if not courses:
            return False
        
        self.courses_in_progress.extend(courses)
        

    def add_finished_courses(self, *courses):
        if not courses:
            return False
        
        self.finished_courses.extend(courses)

    def rate_lectors(self, course, lecturer, rating):
        if (course in self.courses_in_progress and 
            isinstance(lecturer, Lectures) and 
            course in lecturer.courses_attached 
            and 0 <= rating <= 10):
            lecturer.grades.setdefault(course, []).append(rating)

    def average_grades(self):
        if not self.grades:
            return 0
        total_sum = sum(sum(grades) for grades in self.grades.values())
        total_len = sum(len(grades) for grades in self.grades.values())
        return total_sum / total_len

    def __str__(self):
        courses_in_progress = ', '.join(self.courses_in_progress) if self.courses_in_progress else 'Нет текущих курсов'
        finished_courses = ', '.join(self.finished_courses) if self.finished_courses else 'Нет завершенных курсов'

        return (f'=========='
            f'Ментор\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {self.average_grades():.2f}\n'
            f'Курсы в процессе изучения: {courses_in_progress}\n'
            f'Завершенные курсы: {finished_courses}\n'
            f'==========\n')
        