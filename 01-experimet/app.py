import random

from mentor_module import Mentor
from lectures_module import Lectures
from reviewer_module import Reviewer
from student_module import Student

class App():
    genders = ['Male', 'Female']
    male_names = ["Александр", "Андрей", "Артём", "Даниил", "Дмитрий", "Егор", "Иван", "Кирилл", "Максим", "Михаил", "Никита", "Павел", "Роман", "Сергей", "Владимир", "Алексей", "Антон", "Константин", "Георгий", "Василий", "Леонид", "Олег", "Тимур", "Евгений", "Богдан", "Вадим", "Виктор", "Глеб", "Захар", "Илья", "Лев", "Макар", "Матвей", "Руслан", "Степан", "Тимофей", "Фёдор", "Ярослав"]   
    female_names = ["Варвара", "Майя", "София", "Ульяна", "Виктория", "Анна", "Ева", "Алиса", "Ольга", "Екатерина", "Василиса", "Алёна", "Евгения", "Софья", "Мария", "Вероника", "Таисия", "Арина", "Лилия", "Милана"]        
    surnames = ["Иванов", "Смирнов", "Кузнецов", "Попов", "Васильев", "Петров", "Соколов", "Михайлов", "Новиков", "Федоров", "Морозов", "Волков", "Акимов", "Кошкин", "Королев", "Андреев", "Алексеев", "Лебедев", "Антонов", "Дмитриев", "Орлов", "Макаров", "Ковалёв", "Титов", "Васькин", "Захаров", "Никифоров", "Громов", "Фролов", "Егоров", "Яковлев", "Семёнов", "Кириллов", "Белов", "Цветков", "Королёв", "Осипов", "Гусев", "Третьяков", "Брагин", "Баранов", "Крылов", "Уваров", "Жуков", "Горбунов", "Савельев", "Богданов", "Данилов", "Павлов", "Фомин"]
    courses = ["Программист", "Веб-разработчик", "Mobile-разработчик", "DevOps-инженер", "Системный администратор", "Тестировщик ПО", "Бизнес-аналитик", "Дата-сайентист", "Машинное обучение инженер", "Инженер по данным", "Архитектор программного обеспечения", "Cybersecurity специалист", "Cloud-инженер", "Product Manager", "UX/UI дизайнер", "Специалист по информационной безопасности", "Frontend-разработчик", "Backend-разработчик", "Full-stack разработчик", "Специалист по базам данных"]    

    def __init__(self):
        self.mentor = Mentor()
        self.lectures = Lectures()
        self.reviewer = Reviewer()
        self.student = Student()

    def run(self, choose):
        
        while(len(choose.split()) < 4):
            choose = input('Введите количество действующих лиц в формате: (Ментор, Лектор, Ревьюер, Студент) ')
        else:
            choose_list = list(map(int, choose.split())) 
            m_count, l_count, r_count, s_count = choose_list

            mentors = []
            lecturers = []
            reviewers = []
            students = []
            print(f"Количество Менторов: {choose_list[0]}")
            print(f"Количество Лекторов: {choose_list[1]}")
            print(f"Количество Ревьюеров: {choose_list[2]}")
            print(f"Количество Студентов: {choose_list[3]}")

            # Менторы
            for _ in range(m_count):
                mentor = {}
                mentor['gender'] = random.choice(self.genders)
                
                if mentor['gender'] == 'Male':
                    mentor['name'] = random.choice(self.male_names)
                    mentor['surname'] = random.choice(self.surnames)
                else:
                    mentor['name'] = random.choice(self.female_names)
                    mentor['surname'] = random.choice(self.surnames) + "a"

                num_courses = random.randint(5, 12)  
                mentor['courses_attached'] = random.sample(self.courses, num_courses)

                mentors.append(mentor)

            print("Созданные менторы:")
            mentor_objects = []
            for i, mentor_data in enumerate(mentors, start=1):
                mentor_instance = Mentor(
                    name=mentor_data['name'],
                    surname=mentor_data['surname'],
                    gender=mentor_data['gender']
                )
                mentor_instance.courses_attached = mentor_data['courses_attached'] 
                mentor_objects.append(mentor_instance)
                print(f"{mentor_instance}")  

            
            if mentor_objects:
                self.mentor = mentor_objects[0]


            # Лекторы
            for _ in range(l_count):
                lecturer = {}
                lecturer['gender'] = random.choice(self.genders)
                
                if lecturer['gender'] == 'Male':
                    lecturer['name'] = random.choice(self.male_names)
                    lecturer['surname'] = random.choice(self.surnames)
                else:
                    lecturer['name'] = random.choice(self.female_names)
                    lecturer['surname'] = random.choice(self.surnames) + "a"

                num_courses = random.randint(5, 12)  
                lecturer['courses_attached'] = random.sample(self.courses, num_courses)

                lecturers.append(mentor)

            print("Созданные лекторы:")
            lecturer_objects = []
            for i, lecturer_data in enumerate(lecturers, start=1):
                lecturer_instance = Lectures(
                    name=lecturer_data['name'],
                    surname=lecturer_data['surname'],
                    gender=lecturer_data['gender']
                )
                lecturer_instance.courses_attached = mentor_data['courses_attached'] 
                lecturer_objects.append(mentor_instance)
                print(f"{lecturer_instance}")  

            
            if lecturer_objects:
                self.lecturer = lecturer_objects[0]
                


if __name__ == "__main__":    
    app = App()    

    print('Добро пожаловать.')
    print('Далее вам нужно будет ввести число действующих лиц в числовом формате через пробел, например: 1 3 5 7')
    print('Далее будет отображено соотвествующее количество Менторов, Лекторов, Ревьюеров и Студентов')

    choose = input('Введите количество действующих лиц в числовом формате через пробел: (Ментор, Лектор, Ревьюер, Студент) ')

    app.run(choose)


# best_student = Student('Ruoy', 'Eman', 'Male')
# best_student.courses_in_progress += ['Python']
 
# second_student = Student('Alex', 'Imf', 'Male')
# second_student.add_courses_in_progress('Fullstack developer', 'DevOps')
# second_student.add_courses_in_progress('English')
# second_student.add_courses_in_progress('')
# second_student.finished_courses += ['Введение в программирование', 'Git']

# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
# cool_mentor.courses_attached += ['English']
# cool_mentor.courses_attached += ['DevOps']
# cool_mentor.courses_attached += ['Git']
# cool_mentor.courses_attached += ['Fullstack developer']
# cool_mentor.courses_attached += ['Введение в программирование']
 
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 7)
# cool_mentor.rate_hw(best_student, 'Python', 8)
# cool_mentor.rate_hw(second_student, 'Fullstack developer', 10)
# cool_mentor.rate_hw(second_student, 'DevOps', 10)
# cool_mentor.rate_hw(second_student, 'DevOps', 8)
# cool_mentor.rate_hw(second_student, 'Введение в программирование', 9)
# cool_mentor.rate_hw(second_student, 'Git', 7)
 

# lector_1 = Lectures('Enlightened', 'Mind')
# lector_1.add_courses_attached('Python', 'Math')
# second_student.rate_lectors('Python', lector_1, 8)
# second_student.rate_lectors('Math', lector_1, 7)
# lector_1.rate_hw(second_student, 'Python', 7)
# lector_1.rate_hw(second_student, 'Python', 9)
# lector_1.rate_hw(second_student, 'Math', 9)



# second_student.rate_lectors('Python', lector_1, 9)
# second_student.rate_lectors('Python', lector_1, 9)
# print(best_student.grades)
# print(best_student)
# print(second_student.grades)
# print(second_student)
# print(lector_1)


# # Создаем объекты
# student = Student('Ivan', 'Petrov', 'male')
# lecturer = Lectures('Anna', 'Smirnova')

# # Настройка курсов
# student.add_courses_in_progress('Python', 'Math')
# lecturer.courses_attached = ['Python', 'Math']

# # Выставляем оценки лектору
# student.rate_lectors('Python', lecturer, 9)
# student.rate_lectors('Python', lecturer, 8)
# student.rate_lectors('Math', lecturer, 7)
# lecturer.rate_hw(student, 'Python', 7)
# lecturer.rate_hw(student, 'Python', 9)
# lecturer.rate_hw(student, 'Math', 9)
# lecturer.rate_hw(student, 'Math', 6)

# # Проверяем результат
# print(lecturer)
# print(student)