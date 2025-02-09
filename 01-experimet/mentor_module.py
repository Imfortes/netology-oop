class Mentor:
    def __init__(self, name='John', surname='Doe', gender="Default"):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'==========\n'
            f'Ментор\n'
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Закреплен к курсам: {", ".join(self.courses_attached)}\n'
            f'==========\n')