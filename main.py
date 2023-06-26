
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress:
            if course in lecturer.lecture_grades:
                lecturer.lecture_grades[course] += [grade]
            else:
                lecturer.lecture_grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade(self):
        res = 0
        for grade in self.grades.values():
            res = sum(grade) / len(grade)
        return res

    def __lt__(self, other):
        if isinstance(other, Student):
            return self._average_grade() < other._average_grade()
        return print('Нет такого студента!')

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self._average_grade()}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {" ".join(self.finished_courses)}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} '


class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_grades = {}

    def _average_grade(self):
        sum_ = 0
        len_ = 0
        for grade in self.lecture_grades.values():
            sum_ += sum(grade)
            len_ += len(grade)
        return round((sum_ / len_), 2)

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self._average_grade() < other._average_grade()
        return print('Нет такого лектора!')

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции:{self._average_grade()}.'


class Reviewer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def student_rating(stud_list, course):
    rate = []
    for i in stud_list:
        if isinstance(i, Student):
            for j in i.grades[course]:
                rate.append(j)
    return round(sum(rate)/len(rate), 1)


def lecturer_rating(lec_list, course):
    rate = []
    for i in lec_list:
        if isinstance(i, Lecturer):
            for j in i.lecture_grades[course]:
                rate.append(j)
    return round(sum(rate)/len(rate), 1)


some_l = Lecturer('A', 'B')
some_l2 = Lecturer('C', 'D')
some_s = Student('Aa', 'Bb')
some_s2 = Student('Cc', 'Dd')
some_r = Reviewer('Ee', 'Gg')
some_r2 = Reviewer('Ii', 'Jj')

some_l.courses_attached += ['Python']
some_l.courses_attached += ['C++']
some_l2.courses_attached += ['Python']
some_l2.courses_attached += ['SQL']
some_s2.courses_in_progress += ['Python']
some_s2.courses_in_progress += ['C++']
some_s.courses_in_progress += ['Python']
some_s.courses_in_progress += ['SQL']
some_s2.finished_courses += ['SQL']
some_s.finished_courses += ['Javascript']

some_r.courses_attached += ['Python']
some_r.courses_attached += ['C++']
some_r2.courses_attached += ['Python']

some_s.rate_lect(some_l, 'C++', 9)
some_s.rate_lect(some_l, 'Python', 7)
some_s2.rate_lect(some_l2, 'Python', 8)
some_s2.rate_lect(some_l2, 'SQL', 8)

some_s2.rate_lect(some_l, 'C++', 9)
some_s2.rate_lect(some_l, 'Python', 7)
some_s2.rate_lect(some_l, 'Python', 8)
some_s2.rate_lect(some_l, 'Java', 9)

some_r.rate_hw(some_s2, 'Python', 5)
some_r.rate_hw(some_s2, 'Python', 1)

some_r2.rate_hw(some_s, 'Python', 8)
some_r2.rate_hw(some_s, 'Python', 9)

print(f"Лектор:\n{some_l}")
print(f"Студент:\n{some_s2}")
print(f"Ревьюер:\n{some_r}")

stud_list = [some_s, some_s2]
lec_list = [some_l, some_l2]
rew_list = [some_r, some_r2]

print(f"Средняя оценка по студентам: {student_rating(stud_list, 'Python')}")
print(f"Средняя оценка по лекторам: {lecturer_rating(lec_list, 'Python')}")


