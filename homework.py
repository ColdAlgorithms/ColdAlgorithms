import statistics

class __Assignment:
    def __init__(self, name: str, difficulty: float):
        self.name = name
        self.difficulty = difficulty

    def get_name(self):
        return self.name

    def get_difficulty(self):
        return self.difficulty

    def __str__(self):
        return self.get_name()

class __AssignmentResult:
    def __init__(self, id:int, assignment:object, grade: float):
        self.id = id
        self.assignment = assignment
        self.grade = grade

    def get_id(self):
        return self.id
    
    def get_grade(self):
        return self.grade

    def get_assignment(self):
        assignment = __Assignment(self.assignment.get_name(), self.assignment.get_difficulty())
        return assignment

class __Student:
    def __init__(self, id: int, first_name: str, last_name: str, town:str, grades=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.town = town
        if grades == None:
            self.grades = []
        else:
            self.grades = grades

    """
    This constructor should also create data structure for holding the students grades for all of there assignments. Additionally it should create a variable that holds the student's energy level which will be a number between 0 and 1.
    """
    def get_id(self):
        return self.id

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, name:str):
        self.first_name = name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, name: str):
        self.last_name = name

    def get_town(self):
        return self.town

    def set_town(self, town: str):
        self.town = town

    def __str__(self):
        return (self.first_name+" "+self.last_name)

    def get_grade(self):
        if len(self.grades)==0:
            self.grade = .0
        elif len(self.grades)>=2:
            to_calculate = self.grades
            to_calculate.remove(min(to_calculate))
            self.grade = float(sum(to_calculate)/len(to_calculate))
        else:
            self.grade = float(self.grades[0])
        return self.grade
    assignments = []
    results = []
    def assign(self, assignment:object):
        self.assignments.append(assignment)
        if (self.get_energy()* assignment.get_difficulty())>0:
            grade = 1 - (self.get_energy()* assignment.get_difficulty())
        else:
            grade = 0
        self.grades.append(grade)
        if self.energy > self.energy*assignment.get_difficulty():
            self.energy = self.energy - self.energy*assignment.get_difficulty()
        else:
            self.energy = 0
        AssignmentResult = __AssignmentResult(self.get_id(), assignment, grade)
        self.results.append(AssignmentResult)
        return AssignmentResult

    def sleep(self, hours:float):
        if self.get_energy()+self.get_energy()*hours*.1 > 1:
            self.energy = 1
        else:
            self.energy += self.get_energy()*hours*.1

    def get_energy(self):
        return self.energy

class __Course:
    def __init__(self, students: list):
        self.students = students

    def get_mean_grade(self):
            sum = 0
            for student in self.students:
                sum += student.get_grade()
            mean_grade = float(sum/len(self.students))
            return mean_grade

    def get_max_grade(self):
        students_grades = []
        for student in self.students:
            students_grades.append(student.get_grade())
        max_grade = float(max(students_grades))
        return max_grade

    def get_min_grade(self):
        students_grades = []
        for student in self.students:
            students_grades.append(student.get_grade())
        min_grade = float(min(students_grades))
        return min_grade

    def get_median_grade(self):
        students_grades = []
        for student in self.students:
            students_grades.append(student.get_grade())
        median_grade = float(statistics.median(students_grades))
        return median_grade

    def get_grade_variance(self):
        students_grades = []
        for student in self.students:
            students_grades.append(student.get_grade())
        grade_variance = float(statistics.variance(students_grades))
        return grade_variance
        
    def get_grade_std_dev(self):
        students_grades = []
        for student in self.students:
            students_grades.append(student.get_grade())
        std_dev = float(statistics.stdev(students_grades))
        return std_dev

    def assign(self, name: str, difficulty: float):
        assignment = __Assignment(name, difficulty)
        for student in self.students:
            student.assign(assignment)
        return None
