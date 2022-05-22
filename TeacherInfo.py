def print_teacher_info(cursor):
    """Prints all the teachers avaialble in the schoool"""
    sql_print_teacher_info="SELECT Teacher_name, Teacher_last_name, teaching_group FROM Teacher"
    cursor.execute(sql_print_teacher_info)
    myrecord = cursor.fetchall()
    for x in myrecord:
        print( "\n\n You are logged in! \n\t\t\t\t\t\tTeacher Name: {}\n \t\t\t\t \t\tTeacher Last Name: {}\n \t\t\t\t \t\tTeacher of group: {} ".format(x[0],x[1],x[2]))

def teacher_log_in(cursor):
    sql_teacher_log_in = "SELECT * FROM Teacher"
    # check username first [3]
    email_to_check = input("Insert your email: ")
    cursor.execute(sql_teacher_log_in)
        # check email inseted from user if is same as saved
    # sql_email_check="SELECT " \
    #                 "FROM Teacher " \
    #                 "WHERE Teacher_email = email_to_check"
    # x = cursor.execute(sql_email_check)
    # if x == "charlieliam@cfg.com":
    #     print("Grandeeeeeeeeeeee")


