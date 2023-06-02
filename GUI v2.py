import os
import sqlite3
from sqlite3 import Error
from tkinter import *

def main():

    """create labels and input fields for adding new students"""
    label1 = Label(root, text="Student ID:")
    label1.grid(row=0, column=0)
    entry1 = Entry(root)
    entry1.grid(row=0, column=1)

    label2 = Label(root, text="GPA:")
    label2.grid(row=1, column=0)
    entry2 = Entry(root)
    entry2.grid(row=1, column=1)

    label3 = Label(root, text="Student Name:")
    label3.grid(row=2, column=0)
    entry3 = Entry(root)
    entry3.grid(row=2, column=1)

    label4 = Label(root, text="School Name:")
    label4.grid(row=3, column=0)
    entry4 = Entry(root)
    entry4.grid(row=3, column=1)
    
    
    """create a button to add new students to the database """
    def add_student():
    
        student_id = entry1.get()
        gpa = entry2.get()
        student_name = entry3.get()
        school_name = entry4.get()
        cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?)", (student_id, gpa, student_name, school_name))
        conn.commit()
    #end add_student

    button1 = Button(root, text="Add Student", command=add_student)
    button1.grid(row=4, column=1)

    """create labels and input fields for editing student IDs """
    label5 = Label(root, text="Student ID:")
    label5.grid(row=5, column=0)
    entry5 = Entry(root)
    entry5.grid(row=5, column=1)


    """create a button to update student IDs in the database """
    def edit_student():
    
        student_id = entry5.get()
        cursor.execute("UPDATE students SET student_id = (?)WHERE student_id = 1", (student_id))
        conn.commit()
    #end edit_student

    """create a button that updates student IDs"""
    button2 = Button(root, text="Edit Student", command=edit_student)
    button2.grid(row=9, column=1)

    """create a label and a listbox to display the survey results"""
    label8 = Label(root, text="Student Results:")
    label8.grid(row=9, column=0)
    listbox1 = Listbox(root)
    listbox1.grid(row=10, column=0, columnspan=2)

#end main

def create_connection(db_file):
    
    """create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

"""create a database connection by linking it to a .db file in files """
database = r"C:\Downloads\sqlthingy.db"
conn = create_connection(database)
cursor = conn.cursor()
    
#end create_connection

def create_table(conn, create_table_sql):
    
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

"""creates the GUI window""" 
root = Tk()
root.title("Student Database")
    
#end create_table
   

"""create a button to display the survey results"""
def show_results():
    
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()
    for result in results:
        listbox1.insert(END, result)

    button3 = Button(root, text="Show Results", command=show_results)
    button3.grid(row=11, column=1)

    """run the GUI loop"""
    root.mainloop()

    """close the connection to the database"""
    conn.close()

#end show_results


if __name__ == '__main__':
    main()


    
