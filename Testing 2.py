# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class ClassRoom:
    def __init__(self, class_room):
        self.class_room = {'class_num': int(class_room.split()[0]),'class_letter': class_room.split()[1]}

    def get_name(self):
        return str(self.class_room['class_num']) + ' ' + self.class_room['class_letter']


class Persons:
    def __init__(self, surname, name, patronymic):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

    def full_name(self):
        return self.surname + " " + self.name + " " + self.patronymic


class Student:
    def __init__(self, surname, name, patronymic, father, mother, class_room):
        Persons.__init__(self, surname, name, patronymic)
        self.class_room = class_room
        self.father = father
        self.mother = mother

    def student_parent(self):
        return "Отец " + self.father.full_name() + "\nМать " + self.mother.full_name()

    def class_room(self):
        return self.class_room

    # def student_full_name:
    #     return


class_rooms = ['4 А', '4 Б', '4 В']

parents = [Persons("Шестакова", "Мария", "Вениаминовна"),
            Persons("Носкова", "Надежда", "Максимовна"),
            Persons("Федорова", "Александра","Васильева"),
            Persons("Михеева", "Светлана", "Давидовна"),
            Persons("Смирнова", "Елизавета", "Антоновна"),
            Persons("Пугачева", "Ирина", "Александрова"),
            Persons("Шестаков", "Александр", "Владимирович"),
            Persons("Носков", "Николай", "Максимович"),
            Persons("Федоров", "Виктор", "Вадимович"),
            Persons("Михеев", "Алексей", "Григорьевич"),
            Persons("Смирнов", "Василий", "Анатольевич"),
            Persons("Пугачев", "Генадий", "Владимирович")]

students = [Student("Шестаков", "Виктор", "Александрович", parents[6], parents[0], class_rooms[0]),
            Student("Носкова", "Анастасия", "Николаевна", parents[7], parents[1], class_rooms[1]),
            Student("Михеева", "Екатерина", "Алексеевна", parents[9], parents[3], class_rooms[2]),
            Student("Смирнов", "Анатолий", "Васильевич", parents[10], parents[4], class_rooms[0]),
            Student("Федоров", "Ринат", "Викторович", parents[8], parents[2], class_rooms[1]),
            Student("Пугачев", "Вадим", "Генадьевич",parents[11], parents[5], class_rooms[2])]

print("{}".format(Student.student_parent(students[2]),))