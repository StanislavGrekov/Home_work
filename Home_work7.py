from tkinter.ttk import Style

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in self.courses_in_progress and course in lecture.courses_attached:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        print('Имя студент:',self.name,'\n','Фамилия студента:',self.surname,'\n', 'Средняя оценка за домашние задания:', self.__average_value(), '\n','Завершенные курсы:', self.finished_courses)

    def __average_value(self): # Модификатор доступа __private
        list = []
        number_of_elements = 0
        for element in self.grades.values():
            list.extend(element)
            amount = sum(list)
            for i in element: number_of_elements +=1
            result = round((amount/number_of_elements), 1)
        return result    
    
    def __lt__(self, other):
        return self.__average_value() > other.__average_value()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.courses_attached = []
        self.grades = {}

    def __str__(self):
        print('Имя лектора:',self.name,'\n','Фамилия лектора:',self.surname,'\n', 'Средняя оценка за лекции:', self.average_value())

    def average_value(self):
        number_of_elements = 0
        for element in self.grades.values():
            amount = sum(element)
            for i in element: number_of_elements +=1
            result = round((amount/number_of_elements), 1)
        return result

    def __lt__(self, other):
        return self.average_value() < other.average_value()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.courses_attached = []
        self.grades = {}

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        print('Имя эксперта:',self.name,'\n','Фамилия эксперта:',self.surname)
        return

#Объявили экземпляр класса Наставник и добавили ему Pyton в список курсов
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

#Объявили экземпляр класса Эксперт и добавили ему Pyton в список курсов
reviewer1 = Reviewer('Киса', 'Воробьянинов')
reviewer1.courses_attached += ['Python']
reviewer2 = Reviewer('Шура', 'Балаганов')
reviewer2.courses_attached += ['Git']

#Объявили экземпляр класса Лектр и добавили ему Pyton в список курсов
lecturer1 = Lecturer('Полиграф', 'Шариков')
lecturer2 = Lecturer('Александр', 'Корейко')
lecturer1.courses_attached += ['Python']
lecturer2.courses_attached += ['Git']

#Объявили экземпляры класса Студент и добавили ему Pyton, Git в курс который он проходит
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['English Vocabulary']

best_student1 = Student('Адам', 'Козлевич', 'your_gender')
best_student1.courses_in_progress += ['Python']
best_student1.courses_in_progress += ['Git']
best_student1.finished_courses += ['German Vocabulary']

#Эксперт выставил оценки студенту 
reviewer1.rate_hw(best_student, 'Python', 8)
reviewer1.rate_hw(best_student, 'Python', 7)
reviewer1.rate_hw(best_student, 'Python', 10)
reviewer2.rate_hw(best_student, 'Git', 9)
reviewer2.rate_hw(best_student, 'Git', 8)
reviewer2.rate_hw(best_student, 'Git', 5)

reviewer1.rate_hw(best_student1, 'Python', 8)
reviewer1.rate_hw(best_student1, 'Python', 6)
reviewer1.rate_hw(best_student1, 'Python', 5)
reviewer2.rate_hw(best_student1, 'Git', 6)
reviewer2.rate_hw(best_student1, 'Git', 9)
reviewer2.rate_hw(best_student1, 'Git', 10)

#Студенты выставили оценки лекторам
best_student.rate_hw(lecturer1,'Python', 7)
best_student.rate_hw(lecturer1,'Python', 9)
best_student.rate_hw(lecturer1,'Python', 9)
best_student.rate_hw(lecturer2,'Git', 8)
best_student.rate_hw(lecturer2,'Git', 9)
best_student.rate_hw(lecturer2,'Git', 10)

#Задание № 3. Полиморфизм и магические методы
print()
#Переопределение магичскиого метода __str__
reviewer1.__str__()
print()
lecturer1.__str__()
print()
best_student.__str__()
print()
#Переопределение магичскиого метода __lt__
print(f'Средний бал у лектора {lecturer1.name} больше чем у {lecturer2.name} : {lecturer1 > lecturer2}')
print(f'Средний бал у студента {best_student.name} меньше чем у {best_student1.name} : {best_student < best_student1}')
print()

#Задание № 4. Полевые испытания
list_student = [best_student, best_student1]
list_lecturer = [lecturer1, lecturer2]

def average_rating_student(list_student, course):
    list_for_grades = []
    number_of_elements = 0
    for student in list_student:
        for key, values in student.grades.items():
            if key == course:
                list_for_grades.extend(values)
    amount = sum(list_for_grades)
    for i in list_for_grades: number_of_elements +=1
    result = round((amount/number_of_elements), 1)
    print(f'Средняя оценка за домашние задания студентов в разрезе курсов: Курс: {course}, результат: {result}')
      
average_rating_student(list_student, 'Git')
print()
def average_rating_lecturer(list, course):
    list_for_grades = []
    number_of_elements = 0
    for lecturer in list:
        for key, values in lecturer.grades.items():
            if key == course:
                list_for_grades.extend(values)
    amount = sum(list_for_grades)
    for i in list_for_grades: number_of_elements +=1
    result = round((amount/number_of_elements), 1)
    print(f'Средняя оценка за лекции всех лекторов в разрезе курсов: Курс: {course}, результат: {result}')
      
average_rating_lecturer(list_lecturer, 'Python')