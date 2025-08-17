from tkinter import *
import tkinter as tk

class Mygui():

    def __init__(self):
        self.root = tk.Tk()
        self.root.minsize(500,400)
        self.root.geometry("500x400")
        self.root.title("BMI Calculator")
        self.root.config(bg="#819A91")
        self.root.bind("<Escape>",self.close_root)

        #title
        self.label_bmi_title = Label(self.root, text="BMI Calculator", font=("Times",25,"bold italic"), padx=70, pady=10,bg="#A7C1A8",fg="white")
        self.label_bmi_title.place(relx=0.5, rely=0.12, anchor="center")

        #height label
        self.label_height = Label(self.root, text="Enter your height (cm):", font=("Helvetica", 15, "roman bold"), padx=12, pady=10, bg="#D1D8BE", fg="#819A91")
        self.label_height.place(relx=0.5, rely=0.34, anchor="center")

        #entry height
        self.label_entry_height = Entry(self.root,font=("Helvetica", 12, "roman"),width=27,bg="#EEEFE0")
        self.label_entry_height.place(relx=0.5, rely=0.44, anchor="center")

        #weight label
        self.label_weight = Label(self.root, text="Enter your weight (kg):", font=("Helvetica", 15, "roman bold"), padx=12, pady=10, bg="#D1D8BE", fg="#819A91")
        self.label_weight.place(relx=0.5, rely=0.59, anchor="center")

        #entry weight
        self.label_entry_weight = Entry(self.root, font=("Helvetica", 12, "roman"), width=27, bg="#EEEFE0")
        self.label_entry_weight.place(relx=0.5, rely=0.69, anchor="center")

        #result label
        self.label_result = Label(self.root,text="BMI = 20.1 : Normal", font=("Helvetica", 15, "roman bold"),padx=20, pady=10, bg="#EEEFE0", fg="#819A91")
        self.label_result.place(relx=0.5, rely=0.87, anchor="center")
        self.label_result.place_forget()



    def close_root(self,event=None):
        self.root.destroy()
    def run_root(self):
        self.root.mainloop()