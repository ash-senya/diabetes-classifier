import tkinter
import tkinter.messagebox
import customtkinter

import joblib

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")  

diabetes_model = joblib.load('diabetes-classifier-model.pkl')


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        self.title("diabetes predictor")
        self.geometry(f"{700}x{550}")

        

        self.values_frame = customtkinter.CTkFrame(self,width=550,height=500,corner_radius=0)

        self.values_frame.grid(row=0,column=0,rowspan=4,sticky="nsew")

        self.label = customtkinter.CTkLabel(self.values_frame,
                                            text="Diabetes predictor",
                                            font=customtkinter.CTkFont(size=20, weight="bold"),
                                            anchor='n')
        
        self.label.grid(row=0,column=0,padx=90, pady=(20,25))

        #=================SEX=================
        self.sex_label = customtkinter.CTkLabel(self.values_frame,
                                           text="Enter sex:",
                                           font=customtkinter.CTkFont(size=14, weight="bold"),
                                           anchor='w')
        
        self.sex_label.grid(row=1,column=0, padx=(0,200), pady=(0,20))

        self.user_sex_menu = customtkinter.CTkOptionMenu(self.values_frame,
                                                         values=["female","male"],
                                                         command=self.change_user_sex_event)
        
        self.user_sex_menu.grid(row=1,column=0,padx=(150,0),pady=(0,20))

        #=================AGE=================
        self.age_label = customtkinter.CTkLabel(self.values_frame,
                                           text="Enter age:",
                                           font=customtkinter.CTkFont(size=14, weight="bold"),
                                           anchor='w')
        
        self.age_label.grid(row=2,column=0, padx=(0,180), pady=(0,20))

        self.user_age_entry = customtkinter.CTkEntry(self.values_frame,
                                                        width=150,
                                                        height=20,
                                                        placeholder_text="Example: 27")      

        self.user_age_entry.grid(row=2,column=0,padx=(150,0),pady=(0,20))

        #=================PREGNANCIES=================

        self.pregnancies_label = customtkinter.CTkLabel(self.values_frame,
                                           text="Enter pregnancies:",
                                           font=customtkinter.CTkFont(size=14, weight="bold"),
                                           anchor='w')
        
        self.pregnancies_label.grid(row=3,column=0, padx=(0,180), pady=(0,20))

        self.user_pregnancies_entry = customtkinter.CTkEntry(self.values_frame,
                                                        width=150,
                                                        height=20,
                                                        placeholder_text="Example: 2")      

        self.user_pregnancies_entry.grid(row=3,column=0,padx=(150,0),pady=(0,20))
        
        #=================HEIGHT=================
        self.height_label = customtkinter.CTkLabel(self.values_frame,
                                           text="Enter height:",
                                           font=customtkinter.CTkFont(size=14, weight="bold"),
                                           anchor='w')
        
        self.height_label.grid(row=4,column=0, padx=(0,180), pady=(0,20))

        self.user_height_entry = customtkinter.CTkEntry(self.values_frame,
                                                        width=150,
                                                        height=20,
                                                        placeholder_text="Example: 1.63")      

        self.user_height_entry.grid(row=4,column=0,padx=(150,0),pady=(0,20))

        #=================WEIGHT=================
        self.weight_label = customtkinter.CTkLabel(self.values_frame,
                                           text="Enter weight:",
                                           font=customtkinter.CTkFont(size=14, weight="bold"),
                                           anchor='w')
        
        self.weight_label.grid(row=5,column=0, padx=(0,180), pady=(0,20))

        self.user_weight_entry = customtkinter.CTkEntry(self.values_frame,
                                                        width=150,
                                                        height=20,
                                                        placeholder_text="Example: 72.5")      

        self.user_weight_entry.grid(row=5,column=0,padx=(150,0),pady=(0,20))

        #=================GLUCOSE=================
        self.glucose_label = customtkinter.CTkLabel(self.values_frame,
                                           text="Enter glucose:",
                                           font=customtkinter.CTkFont(size=14, weight="bold"),
                                           anchor='w')
        
        self.glucose_label.grid(row=6,column=0, padx=(0,175), pady=(0,20))

        self.user_glucose_entry = customtkinter.CTkEntry(self.values_frame,
                                                        width=150,
                                                        height=20,
                                                        placeholder_text="Example: 60")      

        self.user_glucose_entry.grid(row=6,column=0,padx=(150,0),pady=(0,20))

        #=================BLOOD=================
        self.blood_label = customtkinter.CTkLabel(self.values_frame,
                                           text="Enter blood pressure:",
                                           font=customtkinter.CTkFont(size=14, weight="bold"),
                                           anchor='w')
        
        self.blood_label.grid(row=7,column=0, padx=(0,175), pady=(0,20))

        self.user_blood_entry = customtkinter.CTkEntry(self.values_frame,
                                                        width=150,
                                                        height=20,
                                                        placeholder_text="Example: 72")      

        self.user_blood_entry.grid(row=7,column=0,padx=(150,0),pady=(0,20))

        #=================INSULIN=================
        self.insulin_label = customtkinter.CTkLabel(self.values_frame,
                                           text="Enter insulin:",
                                           font=customtkinter.CTkFont(size=14, weight="bold"),
                                           anchor='w')
        
        self.insulin_label.grid(row=8,column=0, padx=(0,175), pady=(0,20))

        self.user_insulin_entry = customtkinter.CTkEntry(self.values_frame,
                                                        width=150,
                                                        height=20,
                                                        placeholder_text="Example: 18")      

        self.user_insulin_entry.grid(row=8,column=0,padx=(150,0),pady=(0,20))

        #=================SKIN=================
        self.skin_label = customtkinter.CTkLabel(self.values_frame,
                                           text="Enter skin thickness:",
                                           font=customtkinter.CTkFont(size=14, weight="bold"),
                                           anchor='w')
        
        self.skin_label.grid(row=9,column=0, padx=(0,175), pady=(0,20))

        self.user_skin_entry = customtkinter.CTkEntry(self.values_frame,
                                                        width=150,
                                                        height=20,
                                                        placeholder_text="Example: 23")      

        self.user_skin_entry.grid(row=9,column=0,padx=(150,0),pady=(0,20))

        #=================PEDIGREE=================
        self.pedigree_label = customtkinter.CTkLabel(self.values_frame,
                                           text="Enter pedigree func. :",
                                           font=customtkinter.CTkFont(size=14, weight="bold"),
                                           anchor='w')
        
        self.pedigree_label.grid(row=10,column=0, padx=(0,175), pady=(0,20))

        self.user_pedigree_entry = customtkinter.CTkEntry(self.values_frame,
                                                        width=150,
                                                        height=20,
                                                        placeholder_text="Example: 0.16")      

        self.user_pedigree_entry.grid(row=10,column=0,padx=(150,0),pady=(0,20))

        #=================TEXTBOX=================

        self.text_box = customtkinter.CTkTextbox(self,
                                                 width=250,
                                                 height=350)
        self.text_box.insert('0.0','wait for data...')
        
        self.text_box.grid(row=1,column=1, padx=(50,0))

        #=================ANALYSIS=================
        self.analysis_button = customtkinter.CTkButton(self,text="Analysis",
                                                       height=40,width=100,
                                                       font=customtkinter.CTkFont(size=18, weight="bold"),
                                                       command=self.analysis_user,
                                                       anchor='center')
        
        self.analysis_button.grid(row=3,column=1,padx=(50,0), pady=(0,0))

        
        
        
    def change_user_sex_event(self, new_sex: str):
        customtkinter.set_appearance_mode(new_sex)
        if new_sex == 'male':
            self.user_pregnancies_entry.configure(state='disabled')
        else:
            self.user_pregnancies_entry.configure(state='normal')

    def predict(self):
        if self.user_sex_menu.get() == "female":
            pregancies = int(self.user_pregnancies_entry.get())
        else:
            pregancies = 0
        glucose = int(self.user_glucose_entry.get())
        blood_pressure = int(self.user_blood_entry.get())
        skin_thickness = int(self.user_blood_entry.get())
        insulin = int(self.user_insulin_entry.get())
        bmi = round(float(self.user_weight_entry.get()) /  (float(self.user_height_entry.get()) ** 2),1)
        diabetes_pedigree_function = float(self.user_pedigree_entry.get())
        age = int(self.user_age_entry.get())
        
        
        result = diabetes_model.predict([[pregancies,glucose,blood_pressure,skin_thickness,insulin,bmi,diabetes_pedigree_function,age]])

        return (result[0])
    
    def analysis_user(self):
        is_diabetes = self.predict()
        if is_diabetes == 0:
            self.text_box.delete("0.0", "end")
            self.text_box.insert('0.0','Most likely you do not have diabetes. The entered data indicates this. We recommend making an appointment with your doctor for further evaluation if you still feel unwell.Take care of your health!')
        else:
            self.text_box.delete("0.0", "end")
            self.text_box.insert('0.0','Evidence indicates that you most likely have diabetes. We do not recommend that you neglect this and advise you to sign up for blood donation and see a doctor for further examination and begin a course of treatment. Take care of yourself!')


if __name__ == "__main__":
    app = App()
    app.mainloop()
