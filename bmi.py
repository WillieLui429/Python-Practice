from Patient_Info import Patient
Name = input("Enter your name: ")
Age = input("Enter your age: ")
Height = input("Enter your height (in inches): ")
Weight = input("Enter your weight (in pounds): ")

pat_1 =Patient(Name,Age,Weight,Height)
pat_1.display()