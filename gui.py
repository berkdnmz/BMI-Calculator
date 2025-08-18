from tkinter import *
import tkinter as tk
from tkinter import messagebox

class Mygui():

    def __init__(self, calculator):
        self.calculator = calculator
        self.root = tk.Tk()
        self.root.minsize(500,400)
        self.root.title("BMI Calculator")
        self.root.config(bg="#819A91")
        self.root.bind("<Escape>",self.close_root)

        #center
        self.root_height = 400
        self.root_width = 500
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        y = (screen_height - self.root_height) // 2
        x = (screen_width - self.root_width) // 2
        self.root.geometry(f"{self.root_width}x{self.root_height}+{x}+{y}")

        #title
        self.label_bmi_title = Label(self.root, text="BMI Calculator", font=("Times",25,"bold italic"), padx=70, pady=10,bg="#A7C1A8",fg="white")
        self.label_bmi_title.place(relx=0.5, rely=0.12, anchor="center")

        #height label
        self.label_height = Label(self.root, text="Enter your height (cm):", font=("Helvetica", 15, "roman bold"), padx=12, pady=10, bg="#D1D8BE", fg="#819A91")
        self.label_height.place(relx=0.5, rely=0.33, anchor="center")

        #entry height
        self.entry_height = Entry(self.root,font=("Helvetica", 12, "roman"),width=27,bg="#EEEFE0")
        self.entry_height.place(relx=0.5, rely=0.43, anchor="center")
        self.entry_height.bind("<Return>",self.enter_pressed)
        self.entry_height.focus()

        #weight label
        self.label_weight = Label(self.root, text="Enter your weight (kg):", font=("Helvetica", 15, "roman bold"), padx=12, pady=10, bg="#D1D8BE", fg="#819A91")
        self.label_weight.place(relx=0.5, rely=0.58, anchor="center")

        #entry weight
        self.entry_weight = Entry(self.root, font=("Helvetica", 12, "roman"), width=27, bg="#EEEFE0")
        self.entry_weight.place(relx=0.5, rely=0.68, anchor="center")
        self.entry_weight.bind("<Return>", self.enter_pressed)

        #result label
        self.label_result = Label(self.root,text="BMI = 20.1 : Normal", font=("Helvetica", 15, "roman bold"),padx=20, pady=10, bg="#EEEFE0", fg="#819A91")
        self.label_result_place = {'relx': 0.5, 'rely': 0.83, 'anchor': 'center'}
        self.label_result.place(self.label_result_place)
        self.label_result.place_forget()

        # Creator lable
        self.label_creator = Label(self.root, text="Created by Berk", font=("Times", 10, "bold italic"), pady=5, padx=5, bg="#A7C1A8", fg="white")
        self.label_creator.place(relx=1.0, rely=1.0, anchor="se")


    def enter_pressed(self, event=None):

        try:
            self.height = int(self.entry_height.get())
            if 50>self.height or self.height>250:
                messagebox.showerror("Error","Please enter a valid height!")
                return

        except ValueError:
            messagebox.showerror("Error","Please enter a valid height!")
            self.entry_height.delete(0, END)
            return
        except Exception as e:
            print(f"An unexpected error occurred: {type(e).__name__}:{e}")
            return
        self.entry_weight.focus()
        try:
            self.weight = int(self.entry_weight.get())
            if 30 > self.weight or self.weight > 200:
                messagebox.showerror("Error","Please enter a valid weigh!")
                return

        except ValueError:
            messagebox.showerror("Error","Please enter a valid weigh!")
            self.entry_weight.delete(0, END)
            return
        except Exception as e:
            print(f"An unexpected error occurred: {type(e).__name__}:{e}")
            return
        self.calculator.bmi_calculator(self.height, self.weight)


    def close_root(self,event=None):
        self.root.destroy()
    def run_root(self):
        self.root.mainloop()