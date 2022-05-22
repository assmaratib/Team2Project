from datetime import datetime

def attendance_of_the_day_fill_in(year_group, cursor):
    """Students attendance being updated, by printing full name student and asking teacher
    to insert Yes or NO to the question """

    sql_attendance = "SELECT Student_name, Student_last_name, Year_group FROM Students"
    cursor.execute(sql_attendance)
    myrecord = cursor.fetchall()
    for x in myrecord:
        if x[2]==year_group:
            print("STUDENT FULL NAME: {} - {}" .format(x[0],x[1]))
            student_attendance= input("press x if this person is in the classroom, if not type write --absent--")
            #### add notes input option
            if student_attendance=='X' or student_attendance=='x':
                # inserisci nel database Attendance
                sql_attendance_insert = "INSERT INTO Attendance (Student_ID, Data_attendance, Attendance_status) VALUES (%s, %s, %s, %s);"
                tuple1 = (x[0],datetime.today().strftime('%Y-%m-%d'),student_attendance)
        else:
            print("No students in this class")
