class StudentsInMLOps:
    def __init__(self):
        self.total_strength = 0
        self.class_name = "MLOps"

    def enrollStudents(self, num_students):
        self.total_strength += num_students

    def dropStudents(self, num_students):
        self.total_strength -= num_students
        if self.total_strength < 0:
            self.total_strength = 0

    def getTotalStrength(self):
        return self.total_strength

    def getClassName(self):
        return self.class_name
