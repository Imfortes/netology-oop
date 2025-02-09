from mentor_module import Mentor

class Reviewer(Mentor):
    def __init__(self, name='Mike', surname='Brown'):
        super().__init__(name, surname)

    def graded():
        pass

    def __str__(self):
        return (f'=========='
            f'Ревьюер\n'
            f'----------\n'
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'=====\n')