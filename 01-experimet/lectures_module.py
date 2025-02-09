from mentor_module import Mentor

class Lectures(Mentor):
    def __init__(self, name='Anna', surname='Smith', gender="Default"):
        super().__init__(name, surname, gender)
        self.grades = {}
        self.courses_attached = []

    def add_courses_attached(self, *courses):
        if not courses:
            return False
        
        self.courses_attached.extend(courses)

    def average_grades(self):
        if not self.grades:
            return 0
        total_sum = sum(sum(grades) for grades in self.grades.values())
        total_len = sum(len(grades) for grades in self.grades.values())
        return total_sum / total_len
    
    def __str__(self):
        return (f'==========\n'
            f'Лектор\n'
            f'----------\n'
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за лекции: {self.average_grades():.2f}\n'
            f'Закреплен к курсам: {", ".join(self.courses_attached)}\n'
            f'==========\n')