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


class Persons:
    def __init__(self, surname, name, patronymic):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

    def full_name(self):
        return self.surname + " " + self.name + " " + self.patronymic


class Student(Persons):
    def __init__(self, surname, name, patronymic, father, mother, class_room):
        Persons.__init__(self, surname, name, patronymic)
        self.class_room = class_room
        self.father = father
        self.mother = mother

    def student_parent(self):
        return "Отец " + self.father.full_name() + "\nМать " + self.mother.full_name()

    def class_room(self):
        return self.class_room

    def student_full_name(self):
        return self.surname + " " + self.name + " " + self.patronymic


class Teacher(Persons):
    def __init__(self, surname, name, patronymic, subject, class_room1, class_room2):
        Persons.__init__(self, surname, name, patronymic)
        self.subject = subject
        self.class_room1 = class_room1
        self.class_room2 = class_room2

    def teacher_full_name(self):
        return self.surname + " " + self.name + " " + self.patronymic

    def subjects(self):
        return self.subject

    def clas_rooms(self):
        return self.class_room1 + " " + self.class_room2


class_rooms = ['4 А', '5 Б', '6 В', '7 А']

parents = [Persons("Шестакова", "Мария", "Вениаминовна"),
           Persons("Носкова", "Надежда", "Максимовна"),
           Persons("Федорова", "Александра", "Васильева"),
           Persons("Михеева", "Светлана", "Давидовна"),
           Persons("Смирнова", "Елизавета", "Антоновна"),
           Persons("Пугачева", "Ирина", "Александрова"),
           Persons("Шестаков", "Александр", "Владимирович"),
           Persons("Носков", "Николай", "Максимович"),
           Persons("Федоров", "Виктор", "Вадимович"),
           Persons("Михеев", "Алексей", "Григорьевич"),
           Persons("Смирнов", "Василий", "Анатольевич"),
           Persons("Пугачев", "Генадий", "Владимирович"),
           Persons("Воробьев", "Олег", "Трофимович"),
           Persons("Воробьева", "Эльвира", "Борисовна"),
           Persons("Шуленков", "Дмитрий", "Адамович"),
           Persons("Шуленкова", "Ольга", "Дмитреевна")]

students = [Student("Шестаков", "Виктор", "Александрович", parents[6], parents[0], class_rooms[0]),
            Student("Носкова", "Анастасия", "Николаевна", parents[7], parents[1], class_rooms[1]),
            Student("Михеева", "Екатерина", "Алексеевна", parents[9], parents[3], class_rooms[2]),
            Student("Смирнов", "Анатолий", "Васильевич", parents[10], parents[4], class_rooms[0]),
            Student("Федоров", "Ринат", "Викторович", parents[8], parents[2], class_rooms[1]),
            Student("Пугачев", "Вадим", "Генадьевич", parents[11], parents[5], class_rooms[2]),
            Student("Воробьев", "Генадий", "Олегович", parents[12], parents[13], class_rooms[3]),
            Student("Шуленкова", "Алеся", "Дмитреевна", parents[14], parents[15], class_rooms[3])]

teahcers = [Teacher("Попова", "Татьяна", "Михайловна", "Алгебра", class_rooms[2], class_rooms[3]),
            Teacher("Гришунина", "Валентина", "Игоревна", "Физика", class_rooms[2], class_rooms[3]),
            Teacher("Морозв", "Вадим", "Витальевич", "История", class_rooms[0], class_rooms[1]),
            Teacher("Герасимов", "Виктор", "Григорьевич", "Биология", class_rooms[0], class_rooms[1])]

if __name__ == '__main__':
    while True:
        step = input("\n[1] - Получить список всех классов школы\n"
                     "[2] - Получить список всех учеников в указанном классе\n"
                     "[3] - Получить список всех предметов указанного ученика\n"
                     "[4] - Узнать ФИО родителей указанного ученика\n"
                     "[5] - Получить список всех Учителей, преподающих в указанном классе\n"
                     "[6] - Выход\n"
                     "\nУкажите номер действия: ")
        if step == 0:
            pass

        elif step == "1":
            print("\nКлассы в школе: {}\n".format(class_rooms))

        elif step == "2":
            while True:
                step_class = input("[1] - 4 А\n"
                                   "[2] - 5 Б\n"
                                   "[3] - 6 В\n"
                                   "[4] - 7 А\n"
                                   "[5] - Назад\n"
                                   "\nУкажите номер действия: ")
                if step_class == "1":
                    print("\nВ классе учаться: \n{} \n{}\n".format(
                        Student.student_full_name(students[0]),
                        Student.student_full_name(students[3])))

                elif step_class == "2":
                    print("\nВ классе учаться: \n{} \n{}\n".format(
                        Student.student_full_name(students[1]),
                        Student.student_full_name(students[4])))

                elif step_class == "3":
                    print("\nВ классе учаться: \n{} \n{}\n".format(
                        Student.student_full_name(students[2]),
                        Student.student_full_name(students[5])))

                elif step_class == "4":
                    print("\nВ классе учаться: \n{} \n{}\n".format(
                        Student.student_full_name(students[6]),
                        Student.student_full_name(students[7])))

                elif step_class == "5":
                    break

        elif step == "3":
            while True:
                step_subject = input("[1] - {}\n"
                                     "[2] - {}\n"
                                     "[3] - {}\n"
                                     "[4] - {}\n"
                                     "[5] - {}\n"
                                     "[6] - {}\n"
                                     "[7] - {}\n"
                                     "[8] - {}\n"
                                     "[9] - Назад\n"
                                     "\nУкажите номер действия: ".format(Student.student_full_name(students[0]),
                                                                         Student.student_full_name(students[1]),
                                                                         Student.student_full_name(students[2]),
                                                                         Student.student_full_name(students[3]),
                                                                         Student.student_full_name(students[4]),
                                                                         Student.student_full_name(students[5]),
                                                                         Student.student_full_name(students[6]),
                                                                         Student.student_full_name(students[7]), ))
                if step_subject == "1":
                    print("\nУченик - {} \nКласс - {} \nПреподователи: \n{} \n{} \nПредметы - {}, {}\n".format(
                        Student.student_full_name(students[0]),
                        Student.class_room(students[0]),
                        Teacher.teacher_full_name(teahcers[2]),
                        Teacher.teacher_full_name(teahcers[3]),
                        Teacher.subjects(teahcers[2]),
                        Teacher.subjects(teahcers[3])))

                if step_subject == "2":
                    print("\nУченик - {} \nКласс - {} \nПреподователи: \n{} \n{} \nПредметы - {}, {}\n".format(
                        Student.student_full_name(students[1]),
                        Student.class_room(students[1]),
                        Teacher.teacher_full_name(teahcers[2]),
                        Teacher.teacher_full_name(teahcers[3]),
                        Teacher.subjects(teahcers[2]),
                        Teacher.subjects(teahcers[3])))

                if step_subject == "3":
                    print("\nУченик - {} \nКласс - {} \nПреподователи: \n{} \n{} \nПредметы - {}, {}\n".format(
                        Student.student_full_name(students[2]),
                        Student.class_room(students[2]),
                        Teacher.teacher_full_name(teahcers[0]),
                        Teacher.teacher_full_name(teahcers[1]),
                        Teacher.subjects(teahcers[0]),
                        Teacher.subjects(teahcers[1])))

                if step_subject == "4":
                    print("\nУченик - {} \nКласс - {} \nПреподователи: \n{} \n{} \nПредметы - {}, {}\n".format(
                        Student.student_full_name(students[3]),
                        Student.class_room(students[3]),
                        Teacher.teacher_full_name(teahcers[2]),
                        Teacher.teacher_full_name(teahcers[3]),
                        Teacher.subjects(teahcers[2]),
                        Teacher.subjects(teahcers[3])))

                if step_subject == "5":
                    print("\nУченик - {} \nКласс - {} \nПреподователи: \n{} \n{} \nПредметы - {}, {}\n".format(
                        Student.student_full_name(students[4]),
                        Student.class_room(students[4]),
                        Teacher.teacher_full_name(teahcers[2]),
                        Teacher.teacher_full_name(teahcers[3]),
                        Teacher.subjects(teahcers[2]),
                        Teacher.subjects(teahcers[3])))

                if step_subject == "6":
                    print("\nУченик - {} \nКласс - {} \nПреподователи: \n{} \n{} \nПредметы - {}, {}\n".format(
                        Student.student_full_name(students[5]),
                        Student.class_room(students[5]),
                        Teacher.teacher_full_name(teahcers[0]),
                        Teacher.teacher_full_name(teahcers[1]),
                        Teacher.subjects(teahcers[0]),
                        Teacher.subjects(teahcers[1])))

                if step_subject == "7":
                    print("\nУченик - {} \nКласс - {} \nПреподователи: \n{} \n{} \nПредметы - {}, {}\n".format(
                        Student.student_full_name(students[6]),
                        Student.class_room(students[6]),
                        Teacher.teacher_full_name(teahcers[0]),
                        Teacher.teacher_full_name(teahcers[1]),
                        Teacher.subjects(teahcers[0]),
                        Teacher.subjects(teahcers[1])))

                if step_subject == "8":
                    print("\nУченик - {} \nКласс - {} \nПреподователи: \n{} \n{} \nПредметы - {}, {}\n".format(
                        Student.student_full_name(students[7]),
                        Student.class_room(students[7]),
                        Teacher.teacher_full_name(teahcers[0]),
                        Teacher.teacher_full_name(teahcers[1]),
                        Teacher.subjects(teahcers[0]),
                        Teacher.subjects(teahcers[1])))

                if step_subject == "9":
                    break

        if step == "4":
            while True:
                step_parant = input("\n[1] - {}\n"
                                    "[2] - {}\n"
                                    "[3] - {}\n"
                                    "[4] - {}\n"
                                    "[5] - {}\n"
                                    "[6] - {}\n"
                                    "[7] - {}\n"
                                    "[8] - {}\n"
                                    "[9] - Назад\n"
                                    "\nУкажите номер действия: ".format(Student.student_full_name(students[0]),
                                                                        Student.student_full_name(students[1]),
                                                                        Student.student_full_name(students[2]),
                                                                        Student.student_full_name(students[3]),
                                                                        Student.student_full_name(students[4]),
                                                                        Student.student_full_name(students[5]),
                                                                        Student.student_full_name(students[6]),
                                                                        Student.student_full_name(students[7]), ))
                if step_parant == "1":
                    print("\n{}\n".format(Student.student_parent(students[0])))

                if step_parant == "2":
                    print("\n{}\n".format(Student.student_parent(students[1])))

                if step_parant == "3":
                    print("\n{}\n".format(Student.student_parent(students[2])))

                if step_parant == "4":
                    print("\n{}\n".format(Student.student_parent(students[3])))

                if step_parant == "5":
                    print("\n{}\n".format(Student.student_parent(students[4])))

                if step_parant == "6":
                    print("\n{}\n".format(Student.student_parent(students[5])))

                if step_parant == "7":
                    print("\n{}\n".format(Student.student_parent(students[6])))

                if step_parant == "8":
                    print("\n{}\n".format(Student.student_parent(students[7])))

                if step_parant == "9":
                    break

        if step == "5":
            while True:
                step_teahcer = input("\n[1] - 4 А\n"
                                     "[2] - 5 Б\n"
                                     "[3] - 6 В\n"
                                     "[4] - 7 А\n"
                                     "[5] - Назад\n"
                                     "\nУкажите номер действия: ")
                if step_teahcer == "1":
                    print("\nПреподаватели: \nПредмет - {}: {} \nПредмет - {}: {}".format(
                        Teacher.subjects(teahcers[0]),
                        Teacher.teacher_full_name(teahcers[0]),
                        Teacher.subjects(teahcers[1]),
                        Teacher.teacher_full_name(teahcers[1])))

                if step_teahcer == "2":
                    print("\nПреподаватели: \nПредмет - {}: {} \nПредмет - {}: {}".format(
                        Teacher.subjects(teahcers[0]),
                        Teacher.teacher_full_name(teahcers[0]),
                        Teacher.subjects(teahcers[1]),
                        Teacher.teacher_full_name(teahcers[1])))

                if step_teahcer == "3":
                    print("\nПреподаватели: \nПредмет - {}: {} \nПредмет - {}: {}".format(
                        Teacher.subjects(teahcers[2]),
                        Teacher.teacher_full_name(teahcers[2]),
                        Teacher.subjects(teahcers[3]),
                        Teacher.teacher_full_name(teahcers[3])))

                if step_teahcer == "4":
                    print("\nПреподаватели: \nПредмет - {}: {} \nПредмет - {}: {}".format(
                        Teacher.subjects(teahcers[2]),
                        Teacher.teacher_full_name(teahcers[2]),
                        Teacher.subjects(teahcers[3]),
                        Teacher.teacher_full_name(teahcers[3])))

                if step_teahcer == "5":
                    break

        elif step == "6":
            print("\nЗавершение работы")
            break
