###############example to create a class for each form and call from main 



import tkinter as tk
import sqlite3

class PatientForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient Intake Form")
        self.root.geometry("300x400")
        
        self.PatientID_label = tk.Label(root, text="Patient ID")
        self.PatientID_label.pack()
        self.PatientID_entry = tk.Entry(root)
        self.PatientID_entry.pack()
        
        # Other form elements...
        
        self.save_button = tk.Button(root, text="Save", command=self.save_data)
        self.save_button.pack()
        
        # Other buttons...
        
    def save_data(self):
        # Save patient data to the database
        pass
        
    # Other methods...
        

class DoctorsForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Doctors Form")
        self.root.geometry("300x400")
        
        self.DoctorID_label = tk.Label(root, text="Doctor ID")
        self.DoctorID_label.pack()
        self.DoctorID_entry = tk.Entry(root)
        self.DoctorID_entry.pack()
        
        # Other form elements...
        
        self.save_button = tk.Button(root, text="Save", command=self.save_data)
        self.save_button.pack()
        
        # Other buttons...
        
    def save_data(self):
        # Save doctor data to the database
        pass
        
    # Other methods...
        

class PrescriptionForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Prescriptions Form")
        self.root.geometry("300x400")
        
        self.PrescriptionID_label = tk.Label(root, text="Prescription ID")
        self.PrescriptionID_label.pack()
        self.PrescriptionID_entry = tk.Entry(root)
        self.PrescriptionID_entry.pack()
        
        # Other form elements...
        
        self.save_button = tk.Button(root, text="Save", command=self.save_data)
        self.save_button.pack()
        
        # Other buttons...
        
    def save_data(self):
        # Save prescription data to the database
        pass
        
    # Other methods...

def main():
    root = tk.Tk()
    
    patient_form = PatientForm(root)
    doctors_form = DoctorsForm(root)
    prescription_form = PrescriptionForm(root)
    
    # Additional main form elements...
    
    root.mainloop()

if __name__ == "__main__":
    main()



