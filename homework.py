import statistics

# This object represents a school assignment that a student will work on.
class __Assignment:
    """
    Constructs an assignment with the given assignment name and a float that indicates the level of difficulty of the assignment.
    :param name: The name of the assignment
    :param difficulty: The level of difficulty of the assignment
    """
    def __init__(self, name: str, difficulty: float):
        self.name = name
        self.difficulty = difficulty

    """
    Returns the name of the assignment as specified in the constructor.
    :return: The assignment name
    """
    def get_name(self):
        return self.name

    """
    Returns the level of difficulty of the assignment as specified in the constructor.
    :return: The assignment level
    """
    def get_difficulty(self):
        return self.difficulty

    """
    Returns the name of the assignment as specified in the constructor.
    :return: The assignment name
    """
    def __str__(self):
        return self.get_name()

# An object that represents the result of an assignment.
class __AssignmentResult:
    """
    This will contain the ID of the student, the assignment
    that the student worked on and the grade the student received on the assignment.
    :param id: The ID of the student that created this Assignment result
    :param assignment: The Assignment that the student worked on.
    :param grade: A number between 0-1 representing the numerical grade the student received
    """
    def __init__(self, id:int, assignment:object, grade: float):
        self.id = id
        self.assignment = assignment
        self.grade = grade

    """
    Returns the ID of the student as specified in the constructor.
    :return: The student's ID
    """
    def get_id(self):
        return self.id
   
    """
    Returns the grade as specified in the constructor.
    :return: The grade the student received for this assignment
    """
    def get_grade(self):
        return self.grade

    """
    Returns the assignment as specified in the constructor.
    :return: The assignment that the student worked on to create this result
    """    
    def get_assignment(self):
        assignment = __Assignment(self.assignment.get_name(), self.assignment.get_difficulty())
        return assignment

# This class represents a single student
class __Student:
    """
    This creates a student object with the specified ID first and last name and home town. This constructor should
    also create data structure for holding the students grades for all of there assignments. Additionally it should
    create a variable that holds the student's energy level which will be a number between 0 and 1.
    :param id: The student's identifiaction number
    :param fist_name: The student's first name
    :param last_name: The student's last name
    :param town: The student's home town
    """
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
    Returns the ID of the student as specified in the constructor.
    :return: The student's ID

    This constructor should also create data structure for holding the students grades for all of there assignments. Additionally it should create a variable that holds the student's energy level which will be a number between 0 and 1.
    """
    def get_id(self):
        return self.id

    """
    Returns the first name of the student.
    :return: The student's first name
    """
    def get_first_name(self):
        return self.first_name

    """
    Changes the student first name to the specified value of the name parameter.
    :param name: The value that the first name of the student will equal.
    """
    def set_first_name(self, name:str):
        self.first_name = name

    """
    Returns the last name of the student.
    :return: The student's last name
    """
    def get_last_name(self):
        return self.last_name

    """
    Changes the student last name to the specified value of the name parameter.
    :param name: The value that the last name of the student will equal.
    """
    def set_last_name(self, name: str):
        self.last_name = name

    """
    Returns the hometown of the student.
    :return: The student's town name
    """
    def get_town(self):
        return self.town

    """
    Changes the student's hometown to the specified value of the town parameter.
    :param name: The value that the hometown of the student will equal.
    """    
    def set_town(self, town: str):
        self.town = town
        
    """
    Returns a string containing the student's first and last name separated by a space.
    :return: Returns a string of the full name of the student
    """
    def __str__(self):
        return (self.first_name+" "+self.last_name)

    """
    get_grade(self)->float:
    Calculates a an average grade based off of the student's past assignment's grades. The lowest grade is not
    included in the grade calculation if the student has been assigned to two or more assignments in the past.
    See assign() for more detains. If the student has not been assigned any assignments in the pass this should
    return 0.
    :return: A number between 0-1 indicating the student's grade
    """
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
    
    """
    assign(self, assignment:Assignment) -> AssignmentResult:
    This function is to simulate the process of the student receiving an assignment, then working on the
    assignment, then submitting the assignment and finally receiving grade for the assignment. This function will
    receive an assignment then a grade should be calculated using the following formula:
    grade = 1 - (Student's current energy X Assignment difficulty level). The min grade a student may receive is 0% (0)

    After the grade is calculated the student's energy should be decreased by percentage difficulty.
    Example if the student has 80% (.8) energy and the assignment is a difficultly level .2 there final energy
    should be 64% (.64) = .8 - (.8 * .2). The min energy a student may have is 0% (0)

    Finally the grade calculated should be stored internally with in this class so it can be retrieved later.
    Then an Assignment Result object should be created with the student's ID, the assignment
    received as a parameter, and the grade calculated. This newly created Assignment Result object
    should be returned.

    :return: The an AssignmentResult outlining this process
    """
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

     """
    This function restore the student's energy as a rate of 10% per hour. So if they sleep for 8 hours there energy
    will be restored by 80%. If they have 50% (.5) energy and sleep for 8 hours the will wake up with 90% energy
    = (.5 * (1+.8)). The max energy a s student may have is 100% (1)
    :param hours: The number of hours a student will sleep for. Example: .2 is equal to 12 minutes or 20% of an hour.
    :return: None
    """   
    def sleep(self, hours:float):
        if self.get_energy()+self.get_energy()*hours*.1 > 1:
            self.energy = 1
        else:
            self.energy += self.get_energy()*hours*.1

    """
    Returns the current energy of the student. A number between 0 and 1
    :return: The energy of the student.
    """
    def get_energy(self):
        return self.energy

# This class represents a course that a group of students is enrolled in. They will be assigned assignments when enrolled in this course. This object will be used to calculate aggregate student statistics.
class __Course:
    """
    Constructs a course with the specified list of students
    :param students: A list containing one or more students
    """
    def __init__(self, students: list):
        self.students = students

    """
    Returns the numerical value of the class mean (average) grade.
    :return: The average student grade
    """        
    def get_mean_grade(self):
            sum = 0
            for student in self.students:
                sum += student.get_grade()
            mean_grade = float(sum/len(self.students))
            return mean_grade

    """
   Returns the highest grade in the class.
   The grades used in the calculation come from the student.get_grade(), it does not care if a grade was earned
    when the student was in another class.
   :return: The highest grade in the class
   """        
    def get_max_grade(self):
        students_grades = []
        for student in self.students:
            students_grades.append(student.get_grade())
        max_grade = float(max(students_grades))
        return max_grade

    """
   Returns the lowest grade in the class.
   The grades used in the calculation come from the student.get_grade(), it does not care if a grade was earned
    when the student was in another class.
   :return: The lowest grade in the class
   """    
    def get_min_grade(self):
        students_grades = []
        for student in self.students:
            students_grades.append(student.get_grade())
        min_grade = float(min(students_grades))
        return min_grade

    """
    Calculates and returns the median (middle value) of all the student's grades in this course

    The grades used in the calculation come from the student.get_grade(), it does not care if a grade was earned
    when the student was in another class.
    :return: The median grade
    """
    def get_median_grade(self):
        students_grades = []
        for student in self.students:
            students_grades.append(student.get_grade())
        median_grade = float(statistics.median(students_grades))
        return median_grade

    """
    Calculates and returns the sample variance of all the student's grades in this course

    The grades used in the calculation come from the student.get_grade(), it does not care if a grade was earned
    when the student was in another class.
    :return: The sample variance of the grades
    """
    def get_grade_variance(self):
        students_grades = []
        for student in self.students:
            students_grades.append(student.get_grade())
        grade_variance = float(statistics.variance(students_grades))
        return grade_variance

    """
    Calculates and returns the sample standard deviation of all the student's grades in this course.

    The grades used in the calculation come from the student.get_grade(), it does not care if a grade was earned
    when the student was in another class.
    :return: The sample standard deviation of the grades
    """
    def get_grade_std_dev(self):
        students_grades = []
        for student in self.students:
            students_grades.append(student.get_grade())
        std_dev = float(statistics.stdev(students_grades))
        return std_dev

    """
    This creates an assignment using the parameters specified, then assigns it to all of the students in this
    course, by calling the assign method on each student. Subsequent invocations to the statistics methods above
    should reflect the changes made by this method after it is called. In other words if a very difficult
    assignment is assigned the course mean should be less after.
    :param name: The name of the assignment
    :param difficulty: The level of difficulty of the assignment
    :return: None
    """
    def assign(self, name: str, difficulty: float):
        assignment = __Assignment(name, difficulty)
        for student in self.students:
            student.assign(assignment)
        return None
