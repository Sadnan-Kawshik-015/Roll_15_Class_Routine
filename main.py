import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


class Course:

    def __int__(self):
        pass

    def __init__(self, semester, course_name, credit):
        self.teacher_name = None
        self.semester = semester
        self.course_name = course_name
        self.credit = credit

    def get_semester(self):
        return self.semester

    def set_semester(self, semester):
        self.semester = semester

    def get_course_name(self):
        return self.course_name

    def set_course_name(self, course_name):
        self.course_name = course_name

    def get_credit(self):
        return self.credit

    def set_credit(self, credit):
        self.credit = credit

    def get_teacher_name(self):
        return self.teacher_name

    def set_teacher_name(self, teacher_name):
        self.teacher_name = teacher_name


class Teacher:

    def __int__(self):
        pass

    def __init__(self, initial, fullname, designation):
        self.free_slot = None
        self.courses = []
        self.initial = initial
        self.fullname = fullname
        self.designation = designation

    def get_initial(self):
        return self.initial

    def set_initial(self, initial):
        self.initial = initial

    def get_fullname(self):
        return self.fullname

    def set_fullname(self, fullname):
        self.fullname = fullname

    def get_designation(self):
        return self.designation

    def set_designation(self, designation):
        self.designation = designation

    def get_free_slot(self):
        return self.free_slot

    def set_free_slot(self, free_slot):
        self.free_slot = []


class Routine:

    def __int__(self):
        pass

    def __init__(self, semester, course_name, teacher_name, slot_day, slot_time):
        self.teacher_name = []
        self.semester = semester
        self.course_name = []
        self.slot_day = slot_day
        self.slot_time = slot_time

    def get_semester(self):
        return self.semester

    def set_semester(self, semester):
        self.semester = semester

    def get_courses(self):
        return self.course_name

    def get_teacher_name(self):
        return self.teacher_name


file = 'Input.xlsx'
df = pd.ExcelFile(file)

courses_list = []
teachers = []
dictionary = {}
courses_name_list = []
time_dictionary = {}

# print(df.sheet_names)

under_grad_frame = df.parse('UndergradCurriculum (Pre-fed)')

teacher_details_frame = df.parse('TeacherDetails')
assigned_course_frame = df.parse('AssignedCourses')
valid_time_slots_frame = df.parse('ValidTimeSlots')

# print(under_grad_frame.columns)


for i in under_grad_frame.itertuples():
    # print(i[0], i[1], i[2], i[3])
    courses_list.append(Course(i[1], i[2], i[3]))
    courses_name_list.append(i[2])

# print(teacher_details_frame.columns)

for i in teacher_details_frame.itertuples():
    # print(i[0], i[1], i[2], i[3])
    teachers.append(Teacher(i[1], i[2], i[3]))

# for i in teachers :
# print("Initial : "+i.get_initial()+"\nFull Name : "+i.get_fullname()+"\nDesignation : "+i.get_designation())

for i in assigned_course_frame.itertuples():
    dictionary[i[1]] = [i[2], i[3], i[4], i[5], i[6]]

for key in dictionary.keys():
    dictionary[key] = [x for x in dictionary[key] if pd.isnull(x) == False]
    # print(dictionary[key])

for key, i in zip(dictionary.keys(), teachers):
    if key == i.get_initial():
        i.courses = dictionary[key]

# for i in teachers:
#   print("Initial : " + i.get_initial())
#  print(i.courses)

# print(valid_time_slots_frame.columns)

for i in valid_time_slots_frame.itertuples():
    time_dictionary[i[1]] = [i[3], i[4], i[5], i[6], i[7]]

for key, i in zip(time_dictionary.keys(), teachers):
    if key == i.get_initial():
        i.free_slot = time_dictionary[key]

#for i in teachers:
 #   print("Initial : " + i.get_initial())
  #  print(i.courses)
   # print(i.free_slot)


def routine(sem):
    for i, j in zip(courses_list, teachers):
        if i.get_semester() == sem :
            for k in


routine(1)
