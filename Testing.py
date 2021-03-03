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


class Person:
    def __init__(self, name, surname, father_name, birth_date):
        self.name = name
        self.surname = surname
        self.father_name = father_name
        self.birth_date = birth_date

    def get_full_name(self):
        return self.surname + ' ' + self.name[:1] + '.' + self.father_name[:1] + '.'


class Student(Person):
    def __init__(self, name, surname, father_name, birth_date, class_room, father, mother):
        Person.__init__(self, name, surname, father_name, birth_date)
        self.class_room = class_room
        self.father = father
        self.mother = mother

    def get_class_room(self):
        return self.class_room

    def get_parents(self):
        return self.father.get_full_name(), self.mother.get_full_name()


class Teacher(Person):
    def __init__(self, name, surname, father_name, birth_date, classes, subject):
        Person.__init__(self, name, surname, father_name, birth_date)
        self.classes = classes
        self.subject = subject

    def get_subject(self):
        return self.subject

    def get_classes(self):
        return self.classes


class_rooms = ['4 А', '4 Б', '4 В', '5 А', '5 Б', '5 В', '6 А', '6 Б', '6 В', '7 А', '7 Б', '7 В']

parents = [Person("Иван", "Сидоров", "Игоревич", "11.08.1981"),
           Person("Татьяна", "Сидорова", "Максимовна", "15.08.1983"),
           Person("Игорь", "Иванов", "Александрович", "11.08.1981"),
           Person("Ирина", "Иванова", "Александровна", "11.08.1981"),
           Person("Николай", "Петров", "Александрович", "11.08.1981"),
           Person("Светлана", "Петрова", "Николаевна", "11.08.1981")]

students = [Student("Александр", "Иванов", "Игоревич", '10.11.1998', class_rooms[0], parents[2], parents[3]),
            Student("Петр", "Сидоров", 'Иванович', '10.01.1995', class_rooms[2], parents[0], parents[1]),
            Student("Иван", "Петров", 'Николаевич', '12.11.1999', class_rooms[1], parents[4], parents[5])]

teachers = [Teacher("Иван", "Сидоров", "Игоревич", "11.08.1981", [class_rooms[0], class_rooms[1]], 'Математика'),
            Teacher("Игорь", "Иванов", "Александрович", "15.08.1983", [class_rooms[2], class_rooms[1]], 'История'),
            Teacher("Николай", "Петров", "Александрович", "11.08.1981", [class_rooms[0], class_rooms[2]], 'Английский')]



# Получить полный список всех классов школы
st = set([val.get_class_room() for val in students])
print(class_rooms)
print(st)

# Получить список всех учеников в указанном классе(каждый ученик отображается в формате "Фамилия И.О.")
cl_room = '4 В'
st_list = [val.get_full_name() for val in students if val.get_class_room() == cl_room]
print(st_list)

# 3. Получить список всех предметов указанного ученика (Ученик --> Класс --> Учителя --> Предметы)


# 4. Узнать ФИО родителей указанного ученика
his_parents = Student.get_parents()
print(his_parents)

# 5. Получить список всех Учителей, преподающих в указанном классе
teach_list = [val.get_full_name() for val in teachers if cl_room in val.get_classes()]
print(teach_list)