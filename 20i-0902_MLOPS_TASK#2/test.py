from main import StudentsInMLOps
import pytest

def test_enroll_students():
    class_instance = StudentsInMLOps()
    class_instance.enrollStudents(5)
    assert class_instance.getTotalStrength() == 5

def test_drop_students():
    class_instance = StudentsInMLOps()
    class_instance.enrollStudents(10)
    class_instance.dropStudents(3)
    assert class_instance.getTotalStrength() == 7

def test_class_name():
    class_instance = StudentsInMLOps()
    assert class_instance.getClassName() == "MLOps"

if __name__ == "__main__":
    pytest.main()
