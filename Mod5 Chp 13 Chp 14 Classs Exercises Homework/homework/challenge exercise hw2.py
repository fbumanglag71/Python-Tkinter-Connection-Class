## Author: Francisco Bumanglag
## Project: Tkinter Connection Class
## Assignment: Module 5 Project 1
## Course: Python Santa Ana College
## Class: CMPR114 Jason Sim
## Date: July 10, 2023


import tkinter as tk
import sqlite3
import sys

########### PATIENT DEFINITIONS -- SAVE, UPDATE, FETCH, DELETE #########
def save_data():
    PatientID = PatientID_entry.get()
    Name = Name_entry.get()
    Birthdate = Birthdate_entry.get()
    DoctorID = DoctorID_entry.get()

    # connection to the database
    conn = sqlite3.connect('C:\\Users\\franc\\OneDrive\\Desktop\\DB4.db')
    c = conn.cursor()

    # enter data into the table called patients
    c.execute('INSERT INTO patients (Name, Birthdate, DoctorID) VALUES (?,?,?)', (Name, Birthdate, DoctorID))
    conn.commit()  # save the data permanently, saves the data on the disk.
    conn.close()  # closes the connection to the database


def update_data():
    conn = sqlite3.connect('C:\\Users\\franc\\OneDrive\\Desktop\\DB4.db')
    c = conn.cursor()
    c.execute('UPDATE patients SET Name = ?, Birthdate = ?, DoctorID = ? WHERE PatientID = ?',
              (Name_entry.get(), Birthdate_entry.get(), DoctorID_entry.get(), PatientID_entry.get()))
    conn.commit()
    conn.close()
    print('Updated info')


    
def fetch_data():

    conn = sqlite3.connect('C:\\Users\\franc\\OneDrive\\Desktop\\DB4.db')
    c = conn.cursor()
#   c.execute('SELECT * FROM patients WHERE PatientID = 1')
    c.execute('SELECT * FROM patients')
    # ONLY DISPLAYS THE DATA ON THE CONSOLE
    data = c.fetchall()  # scan all rows
    # loop through all the rows
    for row in data:
        print(row)  # print statement
    conn.close()

def delete_data():
    conn = sqlite3.connect('C:\\Users\\franc\\OneDrive\\Desktop\\DB4.db')
    c = conn.cursor()
    c.execute('DELETE FROM patients WHERE PatientID = ?', (PatientID_entry.get(),))
    conn.commit()
    conn.close()


################## OPEN THE PATIENTS FORM #####################################

# this is the start of the window, window load
patients_form = tk.Tk()
patients_form.title("Patient Intake Form")
patients_form.geometry("300x400")  # W x H in pixels, pack function


PatientID_label = tk.Label(patients_form, text="Patient ID")
PatientID_label.pack()
PatientID_entry = tk.Entry(patients_form)
PatientID_entry.pack()

Name_label = tk.Label(patients_form, text="Patient Name")
Name_label.pack()
Name_entry = tk.Entry(patients_form)
Name_entry.pack()

Birthdate_label = tk.Label(patients_form, text="Patient Birthdate")
Birthdate_label.pack()
Birthdate_entry = tk.Entry(patients_form)
Birthdate_entry.pack()

DoctorID_label = tk.Label(patients_form, text="Age")
DoctorID_label.pack()
DoctorID_entry = tk.Entry(patients_form)
DoctorID_entry.pack()


# button widgets
save_button = tk.Button(patients_form, text="Save", command=save_data)
save_button.pack()

fetch_button = tk.Button(patients_form, text="Display", command=fetch_data)
fetch_button.pack()

update_button = tk.Button(patients_form, text="Update", command=update_data)
update_button.pack()

delete_button = tk.Button(patients_form, text="Delete", command=delete_data)
delete_button.pack()


################## MINIMIZE AND HIDE FORM #####################################

def open_doctors_form():
    patients_form.iconify()  # Minimize the patients form
    doctors_form.deiconify()  # Show the second form
    
def close_doctors_form():
    doctors_form.withdraw()  # Hide the second form
    patients_form.deiconify()  # Restore the patients form
    
    
def open_rx_form():
    patients_form.iconify()  # Minimize the patients form
    rx_form.deiconify()  # Show the third form
    
def close_rx_form():
    rx_form.withdraw()  # Hide the third form
    patients_form.deiconify()  # Restore the patients form
    
#function to quit the application
def quit_application():
    sys.exit()  # Exit the application


########### DOCTOR DEFINITIONS -- SAVE, UPDATE, FETCH, DELETE #########
def save_doctors_data():
    DoctorID = DoctorID2_entry.get()
    Name = Name2_entry.get()
    Birthdate = Birthdate2_entry.get()
    License = License2_entry.get()

    # connection to the database
    conn = sqlite3.connect('C:\\Users\\franc\\OneDrive\\Desktop\\DB4.db')
    c = conn.cursor()

    # enter data into the table called patients
    c.execute('INSERT INTO doctors (Name, Birthdate, License) VALUES (?,?,?)', (Name2_entry.get(), Birthdate2_entry.get(), License2_entry.get()))
    conn.commit()  # save the data permanently, saves the data on the disk.
    conn.close()  # closes the connection to the database

def update_doctors_data():
    conn = sqlite3.connect('C:\\Users\\franc\\OneDrive\\Desktop\\DB4.db')
    c = conn.cursor()
    c.execute('UPDATE doctors SET Name = ?, Birthdate = ?, License = ? WHERE DoctorID = ?',
              (Name2_entry.get(), Birthdate2_entry.get(), License2_entry.get(), DoctorID2_entry.get()))
    conn.commit()
    conn.close()
    print('Updated info')


    
def fetch_doctors_data():
    conn = sqlite3.connect('C:\\Users\\franc\\OneDrive\\Desktop\\DB4.db')
    c = conn.cursor()
    c.execute('SELECT * FROM doctors')
    # ONLY DISPLAYS THE DATA ON THE CONSOLE
    data = c.fetchall()  # scan all rows
    # loop through all the rows
    for row in data:
        print(row)  # print statement
    conn.close()


def delete_doctors_data():
    conn = sqlite3.connect('C:\\Users\\franc\\OneDrive\\Desktop\\DB4.db')
    c = conn.cursor()
    c.execute('DELETE FROM doctors WHERE DoctorID = ?', (DoctorID2_entry.get(),))
    conn.commit()
    conn.close()


#################### OPEN THE DOCTORS FORM ##################################

#THE DOCTORS FORM
doctors_form = tk.Toplevel(patients_form)
doctors_form.title("Doctors Form")
doctors_form.geometry("300x400")  # W x H in pixels, pack function
doctors_form.withdraw()  # Hide the second form initially

DoctorID2_label = tk.Label(doctors_form, text="Doctor ID")
DoctorID2_label.pack()
DoctorID2_entry = tk.Entry(doctors_form)
DoctorID2_entry.pack()

Name2_label = tk.Label(doctors_form, text="Doctors Name")
Name2_label.pack()
Name2_entry = tk.Entry(doctors_form)
Name2_entry.pack()

Birthdate2_label = tk.Label(doctors_form, text="Doctors Birthdate")
Birthdate2_label.pack()
Birthdate2_entry = tk.Entry(doctors_form)
Birthdate2_entry.pack()

License2_label = tk.Label(doctors_form, text="License")
License2_label.pack()
License2_entry = tk.Entry(doctors_form)
License2_entry.pack()

# button widgets -- save, fetch, update, delete, close
save2_button = tk.Button(doctors_form, text="Save", command=save_doctors_data)
save2_button.pack()

fetch2_button = tk.Button(doctors_form, text="Display", command=fetch_doctors_data)
fetch2_button.pack()

update2_button = tk.Button(doctors_form, text="Update", command=update_doctors_data)
update2_button.pack()

delete2_button = tk.Button(doctors_form, text="Delete", command=delete_doctors_data)
delete2_button.pack()

#create a button to close the second form (doctors)
close2_button = tk.Button(doctors_form, text="Close", command=close_doctors_form)
close2_button.pack()

############ PRESCRIPTIONS DEFINITIONS -- SAVE, UPDATE, FETCH, DELETE #########
def save_rx_data():
    PrescriptionID = PrescriptionID3_entry.get()
    PatientID = PatientID3_entry.get()
    DoctorID = DoctorID3_entry.get()
    PrescriptionDate = Prescription_Date3_entry.get()
    DrugCode = DrugCode3_entry.get()

    # connection to the database
    conn = sqlite3.connect('C:\\Users\\franc\\OneDrive\\Desktop\\DB4.db')
    c = conn.cursor()

    # enter data into the table called prescriptions
    c.execute('INSERT INTO prescriptions (PatientID, DoctorID, PrescriptionDate, DrugCode ) VALUES (?,?,?,?)', (PatientID3_entry.get(), DoctorID3_entry.get(), Prescription_Date3_entry.get(), DrugCode3_entry.get()))
    conn.commit()  # save the data permanently, saves the data on the disk.
    conn.close()  # closes the connection to the database


def update_rx_data():
    conn = sqlite3.connect('C:\\Users\\franc\\OneDrive\\Desktop\\DB4.db')
    c = conn.cursor()
    c.execute('UPDATE prescriptions SET PatientID = ?, DoctorID = ?, PrescriptionDate = ?, DrugCode = ? WHERE PrescriptionID = ?',
              (PatientID3_entry.get(), DoctorID3_entry.get(), Prescription_Date3_entry.get(), DrugCode3_entry.get(), PrescriptionID3_entry.get()))
    conn.commit()
    conn.close()
    print('Updated info')
    

def fetch_rx_data():
    conn = sqlite3.connect('C:\\Users\\franc\\OneDrive\\Desktop\\DB4.db')
    c = conn.cursor()
    c.execute('SELECT * FROM prescriptions')
    # ONLY DISPLAYS THE DATA ON THE CONSOLE
    data = c.fetchall()  # scan all rows
    # loop through all the rows
    for row in data:
        print(row)  # print statement
    conn.close()


def delete_rx_data():
    conn = sqlite3.connect('C:\\Users\\franc\\OneDrive\\Desktop\\DB4.db')
    c = conn.cursor()
    c.execute('DELETE FROM prescriptions WHERE PrescriptionID = ?', (PrescriptionID3_entry.get(),))
    conn.commit()
    conn.close()
    
######################## OPEN THE RX FORM ###################################

#THE PRESCRIPTIONS FORM
rx_form = tk.Toplevel(patients_form)
rx_form.title("Prescriptions Form")
rx_form.geometry("300x400")  # W x H in pixels, pack function
rx_form.withdraw()  # Hide the third form initially

PrescriptionID3_label = tk.Label(rx_form, text="Prescription ID")
PrescriptionID3_label.pack()
PrescriptionID3_entry = tk.Entry(rx_form)
PrescriptionID3_entry.pack()

PatientID3_label = tk.Label(rx_form, text="Patients ID")
PatientID3_label.pack()
PatientID3_entry = tk.Entry(rx_form)
PatientID3_entry.pack()

DoctorID3_label = tk.Label(rx_form, text="Doctors ID")
DoctorID3_label.pack()
DoctorID3_entry = tk.Entry(rx_form)
DoctorID3_entry.pack()

Prescription_Date3_label = tk.Label(rx_form, text="Prescription Date")
Prescription_Date3_label.pack()
Prescription_Date3_entry = tk.Entry(rx_form)
Prescription_Date3_entry.pack()

DrugCode3_label = tk.Label(rx_form, text="Drug Code")
DrugCode3_label.pack()
DrugCode3_entry = tk.Entry(rx_form)
DrugCode3_entry.pack()

# button widgets -- save, fetch, update, delete, close
save3_button = tk.Button(rx_form, text="Save", command=save_rx_data)
save3_button.pack()

fetch3_button = tk.Button(rx_form, text="Display", command=fetch_rx_data)
fetch3_button.pack()

update3_button = tk.Button(rx_form, text="Update", command=update_rx_data)
update3_button.pack()

delete3_button = tk.Button(rx_form, text="Delete", command=delete_rx_data)
delete3_button.pack()

#create a button to close the third form (prescriptions)
close_third_button = tk.Button(rx_form, text="Close", command=close_rx_form)
close_third_button.pack()

#########################################################

#create a button on the patients form to open the second form (doctors)
open_button = tk.Button(patients_form, text="Open Doctors Form", command=open_doctors_form)
open_button.pack()

#create a button to the patients form to open the third form (prescriptions)
open_third_button = tk.Button(patients_form, text="Open Prescriptions Form", command=open_rx_form)
open_third_button.pack()

#create a button on the patients form to quit the application
quit_button = tk.Button(patients_form, text="Quit", command=quit_application)
quit_button.pack()


#CALL THE MAIN FORM
patients_form.mainloop()  # continue to run on the main window screen (patients)
