class Calculator():
    def __init__(self,gui):
        self.gui = gui
        self.height = 0
        self.weight = 0
        if gui:
            gui.calculator = self

    def bmi_calculator(self,height : int,weight: int):
        self.height = float(height/100) #cm to metre
        self.weight = float(weight)
        self.bmi = self.weight / (self.height**2)
        self.bmi_status = self.get_bmi_status(self.bmi)
        self.gui.label_result.config(text=f"BMI = {self.bmi:.2f} : {self.bmi_status}")
        self.gui.label_result.place(self.gui.label_result_place)

    def get_bmi_status(self,bmi : float):
        if bmi < 16:
            return "Severe Thinness"
        elif 16 <= bmi < 17:
            return "Moderate Thinness"
        elif 17 <= bmi <18.5:
            return "Mild Thinness"
        elif 18.5 <= bmi < 25:
            return "Normal"
        elif 25 <= bmi < 30:
            return "Overweight"
        elif 30 <= bmi <35:
            return "Obese Class I"
        elif 35 <= bmi < 40:
            return "Obese Class II"
        else:
            return "Obese Class III"
