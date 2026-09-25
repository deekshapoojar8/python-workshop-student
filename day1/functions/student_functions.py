def input_student():
    student_name = input("Enter student name:")
    marks_python = float(input("Enter marks for python:"))
    marks_math = float(input("Enter marks for mathematics:"))
    marks_comm = float(input("Enter marks for communication:"))
    dict_student_info = {
        "name":student_name,
        "python_marks":marks_python,
        "math_mark":marks_math,
        "comm_mark":marks_comm
        }
    return dict_student_info

    #TODO:
def calculate_percentage(marks_python,marks_math,marks_comm):
    total = (marks_comm+marks_math+marks_python)
    percentage = (total/300)*100
    return percentage
# percentage = 0

if __name__== "__main__":
    print("\n -- result --")
    student_info = input_student()
    #name,python_m,math_m,comm_m = input_student()
    print(student_info)
    print("student:", student_info["name"])
    print("percentage",calculate_percentage(
        student_info["python_marks"],
        student_info["math_mark"],
        student_info["comm_mark"]))

    