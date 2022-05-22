import mysql.connector
import TeacherInfo
import attendance
from mysql.connector import Error

try:
	mydatabase = mysql.connector.connect(
		host = "localhost",
		database="SchoolRegister",
		user="root",
		password="ASRA1103"
	)
	if mydatabase.is_connected():
		db_info=mydatabase.get_server_info()
		print("Connected to MySql Server version", db_info)
		cursor = mydatabase.cursor()
		TeacherInfo.print_teacher_info(cursor)
		# email check function
		# TeacherInfo.teacher_log_in(cursor)
		year_group_input = input("What year group do you teach?")
		if year_group_input== "reception" or year_group_input == "year 1"or year_group_input == "year 2"or year_group_input == "year 3" or year_group_input == "year 4"or year_group_input == "year 5"or year_group_input == "year 6"or year_group_input == "year 7"or year_group_input == "year 8"or year_group_input == "year 9"or year_group_input == "year 10":
			# year group on correct range
			attendance.attendance_of_the_day_fill_in(year_group_input,cursor)
		else:
			print("Year group it s not valid!")

except Error as e:
	print("Error while connecting to MySql ",e)
finally:
	if mydatabase.is_connected():
		cursor.close()
		mydatabase.close()
		print("MySql connection is closed")
#print(mydatabase)