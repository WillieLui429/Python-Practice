class Patient:
    import decimal

    def __init__(self,Name,Age,Weight, Height):
        self.Name = Name
        self.Age = Age
        self.Weight = Weight
        self.Height = Height

    def bmi_cal(cls):
        bmi = (float(cls.Weight) * 703)/pow(float(cls.Height),2)
        return bmi

    def bmi_eval(cls):
        bmi = cls.bmi_cal()
        if bmi < 18.5:
            ws = "Underweight"
        elif bmi > 18.5 and bmi < 24.9:
            ws = "Normal weight"
        elif bmi > 25 and bmi < 29.9:
            ws = "Overwight"
        elif bmi > 30:
            ws = "Obese"

        return ws

    def display(cls):
        print("Name: " + cls.Name)
        print("Age: " + cls.Age)
        print("Weight: " + cls.Weight +" lbs")
        print("Height: " + cls.Height +" in")
        print("BMI: " + str(cls.bmi_cal()))
        print("Weight Status: " + cls.bmi_eval())
