from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as pop
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
from tkinter import filedialog
from io import BytesIO
import pyrebase
import requests
import sys
import xlsxwriter

# -----------------------------------------------------------------------------------------------------------------------------------------------
      
firebaseConfig = {
  "apiKey": "AIzaSyDt8x7ql-9kt22YoAoaDDrLPBDWig80b0o",
  "authDomain": "bhoranj-19369.firebaseapp.com",
  "databaseURL": "https://bhoranj-19369-default-rtdb.firebaseio.com",
  "projectId": "bhoranj-19369",
  "storageBucket": "bhoranj-19369.appspot.com",
  "messagingSenderId": "102070647406",
  "appId": "1:102070647406:web:bae681ed038a51f76c047f",
  "measurementId": "G-EZQHGN13DE"
}


firebase = pyrebase.initialize_app(firebaseConfig)

database = firebase.database()

storage = firebase.storage()

# -----------------------------------------------------------------------------------------------------------------------------------------------
   
def interface():
    u = username_entry.get()
    p = password_entry.get()
    if u == "bhoranj" and p ==  "1501":
        window.destroy()
        mainwin()
    elif u =="" and p == "":
         pop.showerror("Why empty ?","Enter the username and password !!")

    else:
        pop.showerror("Wrong input !!","You enter wrong password ! Check your username and password")
         
        
def mainwin():
        global main_win

        main_win = Tk()

        main_win.title("GSSS BHORANJ")

        main_win.state("zoomed")
        main_win.geometry(f"{main_win.winfo_screenwidth()}x{main_win.winfo_screenheight()}")
        main_win.minsize(main_win.winfo_screenwidth(), main_win.winfo_screenheight())
        

        main_win.configure(background="maroon")
        
        bg_framek = Image.open("school.jpg")
        photok = ImageTk.PhotoImage(bg_framek)
        bg_panek = Label(main_win, image=photok)
        bg_panek.image = photok
        bg_panek.pack(fill=BOTH, expand=True)

        def quite():
                ask = pop.askyesno("Wanna Quit ??","Do you really want to quit ??")
                if ask:
                        main_win.destroy()
                else:
                        pass
                    
        main_frame = Frame(main_win,height=140,width=950,bg="black")
        main_frame.place(x=300,y=620)
                    
                    

        lgn_buttonp = Image.open("btn1.png")
        photop = ImageTk.PhotoImage(lgn_buttonp)
        lgn_button_labelp = Label(main_frame,bg_panek, image=photop,bg="black")
        lgn_button_labelp.image = photop
        lgn_button_labelp.place(x=5, y=35)

#-------------------------------MAIN BUTTONS OF MAIN WINDOW --------------------------------------------------------------------------
    
        Q = Button(lgn_button_labelp,text="STAFF",font=("yu gothic ui", 13, "bold"),bg="#3047ff",
                   command=teacher,width=25,bd=0, cursor='hand2', activebackground='#3047ff', fg='white')
        Q.place(x=30,y=13)
        
        
        
        lgn_buttonw = Image.open("btn1.png")
        photow = ImageTk.PhotoImage(lgn_buttonw)
        lgn_button_labelw = Label(main_frame,bg_panek, image=photow,bg="black")
        lgn_button_labelw.image = photow
        lgn_button_labelw.place(x=305, y=35)
        
        
        student = Button(main_frame,text="Students",font=("yu gothic ui", 13, "bold"),bg="#3047ff",
                   command=child,width=25,bd=0, cursor='hand2', activebackground='#3047ff', fg='white')
        student.place(x=335,y=50)
        
        
        

        lgn_buttonz = Image.open("btn1.png")
        photoz = ImageTk.PhotoImage(lgn_buttonz)
        lgn_button_labelz = Label(main_frame,bg_panek, image=photoz,bg="black")
        lgn_button_labelz.image = photoz
        lgn_button_labelz.place(x=605, y=35)
        
        
        excel = Button(main_frame,text="Excel Data",font=("yu gothic ui", 13, "bold"),bg="#3047ff",
                   command=saving,width=25,bd=0, cursor='hand2', activebackground='#3047ff', fg='white')
        excel.place(x=635,y=47)
        
        main_win.mainloop()


def saving():
        
    main_win.destroy()
    
   
    global save_win,klass , Non, datass, Boys, Girls, General, Resevered, IRdP, Name, Roll, Dob, Father, Mother, Mobile, GenderE, Category, Aadhar, BPl, acc
    global jiya
    # Create a new window
    
    save_win = Tk()
    save_win.title("Excel Sheet")
    save_win.state("zoomed")
    save_win.config(bg="#06283D")
    save_win.geometry(f"{save_win.winfo_screenwidth()}x{save_win.winfo_screenheight()}")
    save_win.minsize(save_win.winfo_screenwidth(), save_win.winfo_screenheight())
        

    Label(save_win, text="Email :  anshitrangra07@outlook.com", width=10, height=3, bg="#f0687c", anchor="e").pack(side=TOP, fill=X)
    Label(save_win, text="Excel Sheet", width=10, height=3, bg="#c36464", fg="#fff", font="arial 20 bold").pack(side=TOP, fill=X)

    classs_options = ["6th", "7th", "8th", "9th", "10th", "10+1 (Science)", "10+1 (Commerce)", "10+1 (Arts)", "10+2 (Science)", "10+2 (Commerce)", "10+2 (Arts)"]
    lst = Listbox(save_win,font="arial 14 bold",width=17,height=11,selectmode=MULTIPLE,bg="lightgreen")
    lst.place(x=1300,y=175)
    for itemss in classs_options:
        lst.insert(END,itemss)
      
    def jiya():
        selected_indices = lst.curselection()
        jia = [lst.get(index) for index in selected_indices]
        return jia
    # 1st frame of window ==============================================================
    svg = LabelFrame(save_win, text="Excel Sheet Types", font=20, bd=2, width=400, bg="#EDEDED", fg="#06283D", height=600, relief=GROOVE)
    svg.place(x=25, y=180)

    #Checkbuttons

    datass = BooleanVar()
    all_cb = Checkbutton(svg, text="All Data",variable=datass ,font="arial 15", bg="#EDEDED", fg="#06283D")
    all_cb.place(x=100,y=60)


    Boys = BooleanVar()
    boys_cb = Checkbutton(svg, text="Boys",variable=Boys ,font="arial 15", bg="#EDEDED", fg="#06283D")
    boys_cb.place(x=100,y=120)


    Girls = BooleanVar()
    girls_cb = Checkbutton(svg, text="Girls",variable=Girls ,font="arial 15", bg="#EDEDED", fg="#06283D")
    girls_cb.place(x=100,y=180)


    General = BooleanVar()
    General_cb = Checkbutton(svg, text="General category",variable=General ,font="arial 15", bg="#EDEDED", fg="#06283D")
    General_cb.place(x=100,y=240)


    Resevered = BooleanVar()
    reveresed_cb = Checkbutton(svg, text="Reservation category",variable=Resevered ,font="arial 15", bg="#EDEDED", fg="#06283D")
    reveresed_cb.place(x=100,y=300)


    IRdP = BooleanVar()
    irdp_cb = Checkbutton(svg, text="IRDP/BPL",variable=IRdP ,font="arial 15", bg="#EDEDED", fg="#06283D")
    irdp_cb.place(x=100,y=360)
    
    Non = BooleanVar()
    non_cb = Checkbutton(svg, text="Non-IRDP/BPL",variable=Non ,font="arial 15", bg="#EDEDED", fg="#06283D")
    non_cb.place(x=100,y=420)



    # 2nd frame of window ==============================================================
    svg2 = LabelFrame(save_win, text="Excel Data Requirement", font=20, bd=2, width=400, bg="#EDEDED", fg="#06283D", height=600, relief=GROOVE)
    svg2.place(x=450, y=180)

    # Labels


    Name = BooleanVar()
    name_cb = Checkbutton(svg2, text="Name",variable=Name ,font="arial 15", bg="#EDEDED", fg="#06283D")
    name_cb.place(x=100,y=60)


    Roll = BooleanVar()
    roll_cb = Checkbutton(svg2, text="Roll no.",variable=Roll ,font="arial 15", bg="#EDEDED", fg="#06283D")
    roll_cb.place(x=100,y=120)


    Dob = BooleanVar()
    dob_cb = Checkbutton(svg2, text="Date of Birth",variable=Dob ,font="arial 15", bg="#EDEDED", fg="#06283D")
    dob_cb.place(x=100,y=180)


    Father = BooleanVar()
    father_cb = Checkbutton(svg2, text="Father's name",variable=Father ,font="arial 15", bg="#EDEDED", fg="#06283D")
    father_cb.place(x=100,y=240)


    Mother = BooleanVar()
    mother_cb = Checkbutton(svg2, text="Mother's name",variable=Mother ,font="arial 15", bg="#EDEDED", fg="#06283D")
    mother_cb.place(x=100,y=300)

    Mobile = BooleanVar()
    mobile_cb = Checkbutton(svg2, text="Mobile no.",variable=Mobile ,font="arial 15", bg="#EDEDED", fg="#06283D")
    mobile_cb.place(x=100,y=360)



    # 3rd frame of window ==============================================================
    svg3 = LabelFrame(save_win, text="Excel Data Requirement", font=20, bd=2, width=400, bg="#EDEDED", fg="#06283D", height=600, relief=GROOVE)
    svg3.place(x=875, y=180)

    # Checkbuttons


    GenderE = BooleanVar()
    gender_cb = Checkbutton(svg3, text="Gender",variable=GenderE ,font="arial 15", bg="#EDEDED", fg="#06283D")
    gender_cb.place(x=100,y=60)


    Category = BooleanVar()
    category_cb = Checkbutton(svg3, text="Category",variable=Category ,font="arial 15", bg="#EDEDED", fg="#06283D")
    category_cb.place(x=100,y=120)


    Aadhar = BooleanVar()
    aadhar_cb = Checkbutton(svg3, text="Aadhar no.",variable=Aadhar ,font="arial 15", bg="#EDEDED", fg="#06283D")
    aadhar_cb.place(x=100,y=180)


    BPl = BooleanVar()
    Bpl_cb = Checkbutton(svg3, text="IRDP/BPL",variable=BPl ,font="arial 15", bg="#EDEDED", fg="#06283D")
    Bpl_cb.place(x=100,y=240)


    acc = BooleanVar()
    acc_cb = Checkbutton(svg3, text="Account no.",variable=acc ,font="arial 15", bg="#EDEDED", fg="#06283D")
    acc_cb.place(x=100,y=300)


    klass = BooleanVar()
    klass_cb = Checkbutton(svg3, text="Class",variable=klass ,font="arial 15", bg="#EDEDED", fg="#06283D")
    klass_cb.place(x=100,y=360)


    Button(save_win, text="Staff's Excel",command=staff_excel,font=17,width=17,height=2,bg="lightblue").place(x=1300,y=450)
    Button(save_win, text="Download",command=download,font=17,width=17,height=2,bg="lightgreen").place(x=1300,y=550)
    Button(save_win, text="Back",command=Nback,font=17,width=17,height=2,bg="gray").place(x=1300,y=650)



    save_win.mainloop()
    
    
def staff_excel():
    confirm_save = messagebox.askyesno("Choice", "Do you really want to staff's save data in Excel ?")
    if confirm_save:
        file_pathX = filedialog.asksaveasfilename(defaultextension=".xlsx", initialfile="Staff.xlsx", filetypes=[("Excel files", "*.xlsx")])
        if file_pathX:
            workbook = xlsxwriter.Workbook(file_pathX)
            worksheet = workbook.add_worksheet()
            bold = workbook.add_format({'bold': True})
            headings = ["Name", "Post", "DOB", "Gender", "Category", "Mobile no.", "Aadhar no."]
            for col, heading in enumerate(headings):
                worksheet.write(0, col, heading, bold)
            
            # Fetch staff data from Firebase
            staff_details = database.child("Staff").get().val()
            
            row = 1  # Start writing data from row 2
            for staff_id, details in staff_details.items():
                worksheet.write(row, 0, details.get("nameB", ""))
                worksheet.write(row, 1, details.get("post", ""))
                worksheet.write(row, 2, details.get("dob", ""))
                worksheet.write(row, 3, details.get("gender", ""))
                worksheet.write(row, 4, details.get("category", ""))
                worksheet.write(row, 5, details.get("mobile", ""))
                worksheet.write(row, 6, details.get("aadhar", ""))
                row += 1
            
            workbook.close()
            messagebox.showinfo("Success", "Your data has been saved successfully!")
        else:
            messagebox.showwarning("Warning", "No file selected. Data not saved.")
    else:
        messagebox.showinfo("Info", "Data not saved.")

def download():
   
    excel_data = {
    "datass": datass,
    "Boys": Boys,
    "Girls": Girls,
    "General": General,
    "Resevered": Resevered,
    "IRdP": IRdP,
    "Non" : Non,
    "Name": Name,
    "Roll": Roll,
    "Dob": Dob,
    "Father": Father,
    "Mother": Mother,
    "Mobile": Mobile,
    "Gender": GenderE,
    "Category": Category,
    "Aadhar": Aadhar,
    "BPl" : BPl,
    "Class" : klass,
    "Account" : acc
}
    
    head = {
    "Name": Name,
    "Roll no.": Roll,
    "DOB": Dob,
    "Father's name": Father,
    "Mother's name": Mother,
    "Mobile no.": Mobile,
    "Gender": GenderE,
    "Category": Category,
    "Aadhar no.": Aadhar,
    "IRDP/BPl" : BPl,
    "Class" : klass,
    "Account no." : acc
}
    heada = {
    "name": Name,
    "roll": Roll,
    "dob": Dob,
    "father": Father,
    "mother": Mother,
    "mobile": Mobile,
    "gender": GenderE,
    "category": Category,
    "aadhar": Aadhar,
    "bpl" : BPl,
    "class" : klass,
    "account" : acc
}
    
    file_pathE = filedialog.asksaveasfilename(defaultextension=".xlsx", initialfile="Students.xlsx", filetypes=[("Excel files", "*.xlsx")])
    
    if file_pathE:
        workbook = xlsxwriter.Workbook(file_pathE)
        worksheet = workbook.add_worksheet()
        bold = workbook.add_format({'bold': True})


        requirement = []
        for ji in excel_data:
            cvc = excel_data[ji].get()
            if cvc == True:
                requirement.append(ji)
            else:
                pass
        
        requirement_h = []
        for jio in head:
            cvv = head[jio].get()
            if cvv == True:
                requirement_h.append(jio)
            else:
                pass
            
        requirement_d = []
        for jio in heada:
            cvv = heada[jio].get()
            if cvv == True:
                requirement_d.append(jio)
            else:
                pass
        
        if "datass" in requirement:
            headingsS = [ "Name", "Roll No", "DOB", "Father name", "Mother name", "Mobile no.", "Gender", "Category", "Aadhar", "IRDP/BPL", "Class", "Account No."]
            for col, headinga in enumerate(headingsS):
                worksheet.write(0, col, headinga, bold)
           
        else:     
            for col, headinga in enumerate(requirement_h):
                worksheet.write(0, col, headinga, bold)
                
        anshit = jiya()
        row = 1  # Initialize row outside the loop

        if datass.get() == True:
            
            for mmm in anshit:
                    
                students_details = database.child("Students").child(mmm).get().val()
                if students_details:
                    for student_id, details in students_details.items():
                        col = 0
                        for  look in heada:
                            worksheet.write(row, col, details.get(look, ""))
                            col += 1  # Move to the next column
                        row += 1  # Move to the next row for the next child detail
        
        elif General.get() == True and Girls.get() == True:
            for mxm in anshit:
                students_details = database.child("Students").child(mxm).get().val()
                if students_details:
                    for student_id, details in students_details.items():
                        if details.get("category") == "General" and details.get("gender") == "Female":
                            col = 0
                            for loook in requirement_d:
                                worksheet.write(row, col, details.get(loook, ""))
                                col += 1  # Move to the next column
                            row += 1  # Move to the next row for the next child detail
                else:
                    pop.showerror("No Response",f"No students found for class {mxm}")
           
        
        
        elif Boys.get() == True and Non.get() == True:
            for mxm in anshit:
                students_details = database.child("Students").child(mxm).get().val()
                if students_details:
                    for student_id, details in students_details.items():
                        if details.get("gender") == "Male" and details.get("bpl") == "No":
                            col = 0
                            for loook in requirement_d:
                                worksheet.write(row, col, details.get(loook, ""))
                                col += 1  # Move to the next column
                            row += 1  # Move to the next row for the next child detail
                else:
                    pop.showerror("No Response",f"No students found for class {mxm}")

           
                    
        elif Girls.get() == True and Non.get() == True:
            for mxm in anshit:
                students_details = database.child("Students").child(mxm).get().val()
                if students_details:
                    for student_id, details in students_details.items():
                        if details.get("gender") == "Female" and details.get("bpl") == "No":
                            col = 0
                            for loook in requirement_d:
                                worksheet.write(row, col, details.get(loook, ""))
                                col += 1  # Move to the next column
                            row += 1  # Move to the next row for the next child detail
                else:
                    pop.showerror("No Response",f"No students found for class {mxm}")

                    
                    
        elif Boys.get() == True and IRdP.get() == True:
            for mxm in anshit:
                students_details = database.child("Students").child(mxm).get().val()
                if students_details:
                    for student_id, details in students_details.items():
                        if details.get("gender") == "Male" and details.get("bpl") == "Yes":
                            col = 0
                            for loook in requirement_d:
                                worksheet.write(row, col, details.get(loook, ""))
                                col += 1  # Move to the next column
                            row += 1  # Move to the next row for the next child detail
                else:
                    pop.showerror("No Response",f"No students found for class {mxm}")

           
                    
        elif Girls.get() == True and IRdP.get() == True:
            for mxm in anshit:
                students_details = database.child("Students").child(mxm).get().val()
                if students_details:
                    for student_id, details in students_details.items():
                        if details.get("gender") == "Female" and details.get("bpl") == "Yes":
                            col = 0
                            for loook in requirement_d:
                                worksheet.write(row, col, details.get(loook, ""))
                                col += 1  # Move to the next column
                            row += 1  # Move to the next row for the next child detail
                else:
                    pop.showerror("No Response",f"No students found for class {mxm}")

                    
                    
                    
        elif General.get() == True and Non.get() == True:
            for mxm in anshit:
                students_details = database.child("Students").child(mxm).get().val()
                if students_details:
                    for student_id, details in students_details.items():
                        if details.get("category") == "General" and details.get("bpl") == "No":
                            col = 0
                            for loook in requirement_d:
                                worksheet.write(row, col, details.get(loook, ""))
                                col += 1  # Move to the next column
                            row += 1  # Move to the next row for the next child detail
                else:
                    pop.showerror("No Response",f"No students found for class {mxm}")

           
                    
        elif Resevered.get() == True and Non.get() == True:
            for mxm in anshit:
                students_details = database.child("Students").child(mxm).get().val()
                if students_details:
                    for student_id, details in students_details.items():
                        if details.get("category") == "General" and details.get("bpl") == "No":
                            col = 0
                            for loook in requirement_d:
                                worksheet.write(row, col, details.get(loook, ""))
                                col += 1  # Move to the next column
                            row += 1  # Move to the next row for the next child detail
                else:
                    pop.showerror("No Response",f"No students found for class {mxm}")

                    
                    
        elif General.get() == True and IRdP.get() == True:
            for mxm in anshit:
                students_details = database.child("Students").child(mxm).get().val()
                if students_details:
                    for student_id, details in students_details.items():
                        if details.get("category") == "General" and details.get("bpl") == "Yes":
                            col = 0
                            for loook in requirement_d:
                                worksheet.write(row, col, details.get(loook, ""))
                                col += 1  # Move to the next column
                            row += 1  # Move to the next row for the next child detail
                else:
                    pop.showerror("No Response",f"No students found for class {mxm}")

           
                    
        elif Resevered.get() == True and IRdP.get() == True:
            for mxm in anshit:
                students_details = database.child("Students").child(mxm).get().val()
                if students_details:
                    for student_id, details in students_details.items():
                        if details.get("category") == "General" and details.get("bpl") == "Yes":
                            col = 0
                            for loook in requirement_d:
                                worksheet.write(row, col, details.get(loook, ""))
                                col += 1  # Move to the next column
                            row += 1  # Move to the next row for the next child detail
                else:
                    pop.showerror("No Response",f"No students found for class {mxm}")

                    
                               
        elif General.get() == True and Boys.get() == True:
            for mxm in anshit:
                students_details = database.child("Students").child(mxm).get().val()
                if students_details:
                    for student_id, details in students_details.items():
                        if details.get("category") == "General" and details.get("gender") == "Male":
                            col = 0
                            for loook in requirement_d:
                                worksheet.write(row, col, details.get(loook, ""))
                                col += 1  # Move to the next column
                            row += 1  # Move to the next row for the next child detail
                else:
                    pop.showerror("No Response",f"No students found for class {mxm}")

                    
                    
        elif Resevered.get() == True and Girls.get() == True:
            for mxm in anshit:
                students_details = database.child("Students").child(mxm).get().val()
                if students_details:
                    for student_id, details in students_details.items():
                        if details.get("category") != "General" and details.get("gender") == "Female":
                            col = 0
                            for loook in requirement_d:
                                worksheet.write(row, col, details.get(loook, ""))
                                col += 1  # Move to the next column
                            row += 1  # Move to the next row for the next child detail
                else:
                    pop.showerror("No Response",f"No students found for class {mxm}")

           
                    
        elif Resevered.get() == True and Boys.get() == True:
            for mxm in anshit:
                students_details = database.child("Students").child(mxm).get().val()
                if students_details:
                    for student_id, details in students_details.items():
                        if details.get("category") != "General" and details.get("gender") == "Male":
                            col = 0
                            for loook in requirement_d:
                                worksheet.write(row, col, details.get(loook, ""))
                                col += 1  # Move to the next column
                            row += 1  # Move to the next row for the next child detail
                else:
                    pop.showerror("No Response",f"No students found for class {mxm}")

                                  
        elif Boys.get() == True:
            for mxm in anshit:
                students_details = database.child("Students").child(mxm).get().val()
                if students_details:
                    for student_id, details in students_details.items():
                        if details.get("gender") == "Male":
                            col = 0
                            for loook in requirement_d:
                                worksheet.write(row, col, details.get(loook, ""))
                                col += 1  # Move to the next column
                            row += 1  # Move to the next row for the next child detail
                else:
                    pop.showerror("No Response",f"No students found for class {mxm}")

                    
        elif Girls.get() == True:
            for mxm in anshit:
                students_details = database.child("Students").child(mxm).get().val()
                if students_details:
                    for student_id, details in students_details.items():
                        if details.get("gender") == "Female":
                            col = 0
                            for loook in requirement_d:
                                worksheet.write(row, col, details.get(loook, ""))
                                col += 1  # Move to the next column
                            row += 1  # Move to the next row for the next child detail
                else:
                    pop.showerror("No Response",f"No students found for class {mxm}")

              
        
                                    
        elif General.get() == True:
            for mxm in anshit:
                students_details = database.child("Students").child(mxm).get().val()
                if students_details:
                    for student_id, details in students_details.items():
                        if details.get("category") == "General":
                            col = 0
                            for loook in requirement_d:
                                worksheet.write(row, col, details.get(loook, ""))
                                col += 1  # Move to the next column
                            row += 1  # Move to the next row for the next child detail
                else:
                    pop.showerror("No Response",f"No students found for class {mxm}")

                    
        elif Resevered.get() == True:
            for mxm in anshit:
                students_details = database.child("Students").child(mxm).get().val()
                if students_details:
                    for student_id, details in students_details.items():
                        if details.get("category") != "General":
                            col = 0
                            for loook in requirement_d:
                                worksheet.write(row, col, details.get(loook, ""))
                                col += 1  # Move to the next column
                            row += 1  # Move to the next row for the next child detail
                else:
                    pop.showerror("No Response",f"No students found for class {mxm}")

                    
                    
        elif IRdP.get() == True:
            for mxm in anshit:
                students_detail = database.child("Students").child(mxm).get().val()
                if students_detail:
                    for student_id, detail in students_detail.items():
                        if detail.get("bpl") == "Yes":
                            col = 0
                            for lock in requirement_d:
                                worksheet.write(row, col, detail.get(lock, ""))
                                col += 1  # Move to the next column
                            row += 1  # Move to the next row for the next child detail
                else:
                    pop.showerror("No Response",f"No students found for class {mxm}")

                    
        elif Non.get() == True:
            for mxm in anshit:
                students_detail = database.child("Students").child(mxm).get().val()
                if students_detail:
                    for student_id, detail in students_detail.items():
                        if detail.get("bpl") == "No":
                            col = 0
                            for lock in requirement_d:
                                worksheet.write(row, col, detail.get(lock, ""))
                                col += 1  # Move to the next column
                            row += 1  # Move to the next row for the next child detail
                else:
                    pop.showerror("No Response",f"No students found for class {mxm}")




        else:    
            for atom in anshit:
                try:
                    children_details = database.child("Students").child(atom).get().val()
                    if children_details:  
                        for id, details in children_details.items():
                            col = 0  
                            for itemx in requirement_d:
                                # Write details to worksheet
                                worksheet.write(row, col, details.get(itemx, ""))
                                col += 1  # Move to the next column
                            row += 1  # Move to the next row for the next child detail
                    else:
                        pop.showerror("No columns","No columns found for spreadsheet.")
                except Exception as e:
                    pop.showerror("Database error","Error fetching data ")

        
        workbook.close()
        messagebox.showinfo("Success", "Your data has been saved successfully!")
                
        
                
        
            
    

        
        
        
        
        
    
            


    
      
        
def Nback():
    save_win.destroy()
    mainwin()
    

        
def teacher():
    global staff_win
    global lstaff
    global objs, objs2
            
            
    try:
            main_win.destroy()
    except:
            pass
        
    staff_win = Tk()
    staff_win.title("Staff")
    staff_win.state("zoomed")
    staff_win.config(bg="#06283D")
    staff_win.geometry(f"{staff_win.winfo_screenwidth()}x{staff_win.winfo_screenheight()}")
    staff_win.minsize(staff_win.winfo_screenwidth(), staff_win.winfo_screenheight())
           

            
           
    Label(staff_win, text="Email :  anshitrangra07@outlook.com", width=10, height=3, bg="#f0687c", anchor="e").pack(side=TOP, fill=X)
    Label(staff_win, text="Staff", width=10, height=3, bg="#c36464", fg="#fff", font="arial 20 bold").pack(side=TOP, fill=X)

            
        # 1st frame of window ==============================================================
    objs = LabelFrame(staff_win, text="Staff's details", font=20, bd=2, width=900, bg="#EDEDED", fg="#06283D", height=260, relief=GROOVE)
    objs.place(x=400, y=200)

        # Labels
    Label(objs, text="Name", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=30, y=50)
    Label(objs, text="Profession", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=30, y=100)
    Label(objs, text="DOB", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=30, y=150)
    Label(objs, text="Gender", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=500, y=50)
    Label(objs, text="Category", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=500, y=100)
    Label(objs, text="Mobile no.", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=500, y=150)

        # 2nd frame of window ==============================================================
    objs2 = LabelFrame(staff_win, text="Staff's details", font=20, bd=2, width=900, bg="#EDEDED", fg="#06283D", height=260, relief=GROOVE)
    objs2.place(x=400, y=485)

        # Labels
    Label(objs2, text="Aadhar no.", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=30, y=50)

    lstaff = Listbox(staff_win, width=20, height=18, font="comicsansms 25 bold")
    lstaff.pack(side=LEFT, anchor=NW)

    try:
        data = database.child("Staff").get()
        for te in data:
            lstaff.insert(END,te.val().get("nameB"))  
    except:
        pop.showerror("connection","check your inernet connection")
        sys.exit()
            
    lstaff.bind("<<ListboxSelect>>",show_detail_staff)

    picFM = Frame(staff_win, bd=3, bg="black", width=200, height=245, relief=GROOVE)
    picFM.place(x=1310, y=200)
            
    

    Button(staff_win, text="Add Staff", command=up_staff, width=19, height=2, font="arial 12 bold", bg="lightblue").place(x=1310, y=490)
    Button(staff_win, text="Delete", command=del_staff, width=19, height=2, font="arial 12 bold", bg="lightgreen").place(x=1310, y=570)
    Button(staff_win, text="Back", command=backS, width=19, height=2, font="arial 12 bold", bg="gray").place(x=1310, y=650)

        
    
    
    staff_win.mainloop()
    
    
    
def clear_windowX():
    # Destroy all widgets in the canvas
    for widget in objs.winfo_children():
        widget.destroy()
        
    for widget in objs2.winfo_children():
        widget.destroy()
    


def show_detail_staff(event):
    global image_label2
    
    selected_staff_name = None
    sel_staff = lstaff.curselection()
    if sel_staff:
        selected_staff_name = lstaff.get(sel_staff[0])
    else:
        return

    detail = database.child("Staff").child(selected_staff_name).get().val()

    if detail is None:
        return

    namee = detail.get("nameB")
    post = detail.get("post")
    dob = detail.get("dob")
    gender = detail.get("gender")
    category = detail.get("category")
    mobile = detail.get("mobile")
    aadhar = detail.get("aadhar")
    
    try:
        clear_windowX()
    except:
        pass 

    


    label_widgets = []

    for widget in label_widgets:
        widget.destroy()
    label_widgets.clear()

    Label(objs, text="Name", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=30, y=50)
    Label(objs, text="Profession", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=30, y=100)
    Label(objs, text="DOB", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=30, y=150)
    Label(objs, text="Gender", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=500, y=50)
    Label(objs, text="Category", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=500, y=100)
    Label(objs, text="Mobile no.", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=500, y=150)

    Label(objs, text=namee, font="arial 15", bg="#EDEDED", fg="#06283D").place(x=190, y=50)
    Label(objs, text=post, font="arial 15", bg="#EDEDED", fg="#06283D").place(x=190, y=100)
    Label(objs, text=dob, font="arial 15", bg="#EDEDED", fg="#06283D").place(x=190, y=150)
    Label(objs, text=gender, font="arial 15", bg="#EDEDED", fg="#06283D").place(x=680, y=50)
    Label(objs, text=category, font="arial 15", bg="#EDEDED", fg="#06283D").place(x=680, y=100)
    Label(objs, text=mobile, font="arial 15", bg="#EDEDED", fg="#06283D").place(x=680, y=150)

    Label(objs2, text="Aadhar no.", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=30, y=50)
    Label(objs2, text=aadhar, font="arial 15", bg="#EDEDED", fg="#06283D").place(x=190, y=50)

    try:
        image_label2.destroy()
        tk_image2 = None
    except:
        pass 

    if " "  in namee:
        murl = f"https://firebasestorage.googleapis.com/v0/b/bhoranj-19369.appspot.com/o/Staffs%2F{namee}%20pic?alt=media"
    else:
        murl = f"https://firebasestorage.googleapis.com/v0/b/bhoranj-19369.appspot.com/o/Staffs%2F{namee.replace(' ','%20')}%20pic?alt=media"


    response = requests.get(murl)
    if staff_win.winfo_exists():
        try:
            # Load image from response content
            tk_image2 = ImageTk.PhotoImage(Image.open(BytesIO(response.content)).resize((200, 245)))
            image_label2 = Label(staff_win, image=tk_image2)
            image_label2.image = tk_image2  # Retain a reference to the image to prevent garbage collection
            image_label2.place(x=1310, y=200)
        except Exception as e:
            pop.showerror("Load on image","Error loading image:", e)
    else:
        pop.showerror("What ?","Root window does not exist.")


                
def up_staff():
        global root
        staff_win.destroy()

        
        def enter_data():
                global nameB
                nameB = entry_name.get()
                dob = dob_cal.get()
                aadhar = adhar.get()
                post = entry_post.get()
                mobile = entry_mobile.get()
                category = category_var.get()
                storage.child("Staffs").child(f"{nameB} pic").put(file_path)
                url = storage.child("Staff").child(f"{nameB} pic").get_url(None)

                vv = messagebox.askyesno("Really??", "Do you really want to add data?")
                if vv:
                        data = f"Name: {nameB}\nAadhar: {aadhar}\nDOB: {dob}\nPost: {post}\nMobile: {mobile}\nGender: {GenderX}\nCategory: {category}\nPhoto: Done"
                        messagebox.showinfo("Data", data)

                        
                        try:
                                query = {
                                        "nameB": nameB,
                                        "dob" : dob,
                                        "post": post,
                                        "aadhar":aadhar,
                                        "mobile": mobile,
                                        "gender": GenderX,
                                        "category": category,
                                        "photo": url    
                                }
                                
                                database.child("Staff").child(nameB).set(query)
                                messagebox.showinfo("Success", "Data inserted successfully!")
                                
                        except Exception as e:
                                messagebox.showerror("Error", f"Error inserting data: {e}")
                                
                else:
                       pass




       

        root = Tk()
        root.title("Adding student")
        root.state("zoomed")
        root.config(bg="#06283D")
        root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        root.minsize(root.winfo_screenwidth(), root.winfo_screenheight())
           

        def selection():
            global GenderX
            value=radio.get()
            if value ==1:
                GenderX = "Male"
            else:
                GenderX = "Female"

        Label(root,text="Email :  anshitrangra07@outlook.com",width=10,height=3,bg="#f0687c",anchor="e",).pack(side=TOP,fill=X)
        Label(root,text="Staff Registration ",width=10,height=3,bg="#c36464",fg="#fff",font="arial 20 bold").pack(side=TOP,fill=X)

        # 1st frame of window ==============================================================

        obj = LabelFrame(root,text="Staff's details",font=20,bd=2,width=1100,bg="#EDEDED",fg="#06283D",height=260,relief=GROOVE)
        obj.place(x=30,y=200)

        # /////////////////////////////////?????????????????????????? LABELS  {{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}
        # Labels
        Label(obj, text="Name", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=30, y=50)
        Label(obj, text="Profession", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=30, y=100)
        Label(obj, text="DOB", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=30, y=150)
        Label(obj, text="Gender", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=500, y=50)
        Label(obj, text="Category", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=500, y=100)
        Label(obj, text="Mobile no.", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=500, y=150)

                # ;''''''''''''''''''''''''''''''''''''''''DATA"""""""""""""""""""""""""""''''''''''
        name = StringVar()
        entry_name = Entry(obj,textvariable=name,width=25,font="arial 13")
        entry_name.place(x=160,y=50)
                
                
                
        def upload_photo():
            global file_path
            file_path = filedialog.askopenfilename(title="Select Photo", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
            if file_path:
                messagebox.showinfo("Photo Selected", f"Selected Photo: {file_path}")
                imgg = (Image.open(file_path))
                imgrsg = imgg.resize((200,245))
                pcg = ImageTk.PhotoImage(imgrsg)
                imgFM_label.config(image=pcg)
                imgFM_label.image = pcg



        def validate_input(new_value):
            if new_value.isdigit() or new_value == "":
                return True
            else:
                return False
        validate_cmd = root.register(validate_input)

        post = StringVar()
        entry_post = Entry(obj,textvariable=post,width=25,font="arial 13")
        entry_post.place(x=160, y=100)

        dob_cal = DateEntry(obj,bg="#06283D",width=25,font="arial 12")
        dob_cal.place(x=160,y=150)

        radio = IntVar()
        SGenderW = Radiobutton(obj,text="Male",variable=radio,font="arial 13",value=1,bg="#EDEDED",fg="#06283D",command=selection)
        SGenderW.place(x=680,y=50)

        SGenderQ = Radiobutton(obj,text="Female",variable=radio,font="arial 13",value=2,bg="#EDEDED",fg="#06283D",command=selection)
        SGenderQ.place(x=790,y=50)
        
        categories = ["General", "OBC", "SC", "ST"]
        category_var = StringVar()
        category_var.set("Select Category")
        category_comboboxA = ttk.Combobox(obj, textvariable=category_var, values=categories, font=("arial", 13), state="readonly")
        category_comboboxA.place(x=680,y=100)

                
        Mob = StringVar()
        entry_mobile = Entry(obj,textvariable=Mob,width=25,font="arial 13", validate="key", validatecommand=(validate_cmd, '%P'))
        entry_mobile.place(x=680, y=150)
        
        
        



        

        # 2nd frame of window/////////////////////////////////////////////////////////////

        obj2 = LabelFrame(root,text="Staff's details",font=20,bd=2,width=1100,bg="#EDEDED",fg="#06283D",height=260,relief=GROOVE)
        obj2.place(x=30,y=485)

        # /////////////////////////////////?????????????????????????? LABELS  {{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}
        # Labels
        Label(obj2, text="Aadhar no.", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=30, y=50)

    # ;''''''''''''''''''''''''''''''''''''''''DATA"""""""""""""""""""""""""""''''''''''

        adhar = StringVar()
        entry_adhar = Entry(obj2,textvariable=adhar,width=25,font="arial 13")
        entry_adhar.place(x=160,y=50)

        


        


        picFM = Frame(root,bd=3,bg="black",width=200,height=245,relief=GROOVE)
        picFM.place(x=1250,y=200)
                
                
        try:
            image_urlFM = "https://firebasestorage.googleapis.com/v0/b/bhoranj-19369.appspot.com/o/Theme%2Flogo.png?alt=media&token=c8a97c5e-fdea-485b-9472-b2cec28a5921"
            responseFM = requests.get(image_urlFM)
            img_dataFM = BytesIO(responseFM.content)
            imgFM = Image.open(img_dataFM)
            imgFM = imgFM.resize((200, 245))
            photoFM = ImageTk.PhotoImage(imgFM)

            # Use photoFM instead of photo in the Label creation
            imgFM_label = Label(picFM, image=photoFM, bg='#040405')
            imgFM_label.image = photoFM  
            imgFM_label.place(x=0, y=0)
        except:
            pop.showerror("Conection lost","No internet connection !")
            sys.exit()


 




        Button(root,text="Upload",width=19,height=2,font="arial 12 bold",command=upload_photo,bg="lightblue").place(x=1250,y=490)
        Button(root,text="Save",width=19,height=2,command=enter_data,font="arial 12 bold",bg="lightgreen").place(x=1250,y=570)
        Button(root,text="Back",width=19,height=2,font="arial 12 bold",command=go_back,bg="gray").place(x=1250,y=650)


        root.mainloop()



def del_staff():
     try:
        selected_indices = lstaff.curselection()
        for index in reversed(selected_indices):
            staff_name = lstaff.get(index)
                
        h = messagebox.askyesno("Delete Staff",f"Do you really want to delete data of {staff_name}")
        
     except:
        pop.showerror("Why ?","You did not select any item from listbox")
        
     if h == True:
                try:
                        lstaff.delete(selected_indices)
                        database.child("Staff").child(staff_name).remove()
                        
                        messagebox.showinfo("Data", "Data deleted sucessfully.")
                        

                except Exception as e:
                        pop.showerror("Why ?","Select a item from listbox")
                        
     else:
                pass


def child():
    global student_win
    global stl
    global selected_class_var
    global pic_frame
    global FMR, FMR2

    try:
        main_win.destroy()
    except:
        pass

    student_win = Tk()
    student_win.title("Students")
    student_win.state("zoomed")
    student_win.config(bg="#06283D")
    student_win.geometry(f"{student_win.winfo_screenwidth()}x{student_win.winfo_screenheight()}")
    student_win.minsize(student_win.winfo_screenwidth(), student_win.winfo_screenheight())
           

    
    Label(student_win, text="Email :  anshitrangra07@outlook.com", width=10, height=3, bg="#f0687c", anchor="e").pack(side=TOP, fill=X)
    Label(student_win, text="Students", width=10, height=3, bg="#c36464", fg="#fff", font="arial 20 bold").pack(side=TOP, fill=X)
    Label(student_win,text="Total Students :",width=15,height=3, bg="#c36464",fg="#fff",font="arial 20 bold").place(x=35,y=87)

    selected_class_var = StringVar()
    selected_class_var.set("Class")
    class_options = ["6th", "7th", "8th", "9th", "10th", "10+1 (Science)", "10+1 (Commerce)", "10+1 (Arts)", "10+2 (Science)", "10+2 (Commerce)", "10+2 (Arts)"]
    class_combobox = ttk.Combobox(student_win, textvariable=selected_class_var, values=class_options, font="comicsansms 20 bold", state="readonly")
    class_combobox.place(x=1080, y=87)

    # 1st frame of window ==============================================================
    FMR = LabelFrame(student_win, text="Student's details", font=20, bd=2, width=900, bg="#EDEDED", fg="#06283D", height=260, relief=GROOVE)
    FMR.place(x=400, y=200)

    # Labels
    Label(FMR, text="Name", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=30, y=50)
    Label(FMR, text="Roll No.", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=30, y=100)
    Label(FMR, text="Class", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=30, y=150)
    Label(FMR, text="Father's Name", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=500, y=50)
    Label(FMR, text="Mother's Name", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=500, y=100)
    Label(FMR, text="DOB", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=500, y=150)
    
    # 2nd frame of window ==============================================================
    FMR2 = LabelFrame(student_win, text="Student's details", font=20, bd=2, width=900, bg="#EDEDED", fg="#06283D", height=260, relief=GROOVE)
    FMR2.place(x=400, y=485)

    # Labels
    Label(FMR2, text="Gender", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=30, y=50)
    Label(FMR2, text="Mobile no.", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=30, y=100)
    Label(FMR2, text="Aadhar no.", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=30, y=150)
    Label(FMR2, text="IRDP/BPL", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=500, y=50)
    Label(FMR2, text="Category", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=500, y=100)
    Label(FMR2, text="Account No.", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=500, y=150)

    stl = Listbox(student_win, width=20, height=18, font="comicsansms 25 bold")
    stl.pack(side=LEFT, anchor=NW)
    
    class_combobox.bind("<<ComboboxSelected>>", update_listbox)
    
        
    stl.bind("<<ListboxSelect>>",update_window)
    

    pic_frame = Frame(student_win, bd=3, bg="black", width=200, height=245, relief=GROOVE)
    pic_frame.place(x=1310, y=200)

    Button(student_win, text="Add Student", command=add_student, width=19, height=2, font="arial 12 bold", bg="lightblue").place(x=1310, y=490)
    Button(student_win, text="Delete", command=del_student, width=19, height=2, font="arial 12 bold", bg="lightgreen").place(x=1310, y=570)
    Button(student_win, text="Back", command=backs, width=19, height=2, font="arial 12 bold", bg="gray").place(x=1310, y=650)

    student_win.mainloop()

    
    

def clear_window():
    # Destroy all widgets in the canvas
    for widget in FMR.winfo_children():
        widget.destroy()
        
    for widget in FMR2.winfo_children():
        widget.destroy()
    
    # Destroy all widgets in the pic_frame
    for widget in pic_frame.winfo_children():
        widget.destroy()



def save_as():
    global Sname, Sclasss
    
    # Set the default file name as the name of the student
    default_file_name = f"{Sname.replace(' ', '_')}_{Sclasss}_pic.png"
    
    # Prompt user to choose a file path for saving the image
    file_path = filedialog.asksaveasfilename(defaultextension=".png", initialfile=default_file_name, filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    
    # Check if a file path was selected
    if file_path:

        if Sclasss in ["6th", "7th", "8th", "9th", "10th"]:
            if " " not in Sname:
                image_url = f"https://firebasestorage.googleapis.com/v0/b/bhoranj-19369.appspot.com/o/{Sclasss}%20class%2F{Sname}%20{Sclasss}%20pic?alt=media"
            else:    
                image_url = f"https://firebasestorage.googleapis.com/v0/b/bhoranj-19369.appspot.com/o/{Sclasss.replace(' ','%20')}%20class%2F{Sname.replace(' ','%20')}%20{Sclasss}%20pic?alt=media"
                
        elif Sclasss in [ "10+1 (Science)", "10+1 (Commerce)", "10+1 (Arts)"]:
            dictionary = {"10+1 (Science)":"Science", "10+1 (Commerce)": "Commerce", "10+1 (Arts)": "Arts"}
            if " " not in Sname:
                image_url = f"https://firebasestorage.googleapis.com/v0/b/bhoranj-19369.appspot.com/o/10%20%20%201%20class%2F10%201%20({dictionary[Sclasss]})%2F{Sname}%20{Sclasss}%20pic?alt=media"
            else:    
                image_url = f"https://firebasestorage.googleapis.com/v0/b/bhoranj-19369.appspot.com/o/10%20%20%201%20class%2F10%201%20({dictionary[Sclasss]})%2F{Sname.replace(' ','%20')}%20{Sclasss}%20pic?alt=media"
                
        elif Sclasss in [ "10+2 (Science)", "10+2 (Commerce)", "10+2 (Arts)"]:
            dictionaryZ = {"10+2 (Science)":"Science", "10+2 (Commerce)": "Commerce", "10+2 (Arts)": "Arts"}
            if " " not in Sname:
                image_url = f"https://firebasestorage.googleapis.com/v0/b/bhoranj-19369.appspot.com/o/10%20%20%202%20class%2F10%202%20({dictionaryZ[Sclasss]})%2F{Sname}%20{Sclasss}%20pic?alt=media"
            else:    
                image_url = f"https://firebasestorage.googleapis.com/v0/b/bhoranj-19369.appspot.com/o/10%20%20%202%20class%2F10%202%20({dictionaryZ[Sclasss]})%2F{Sname.replace(' ','%20')}%20{Sclasss}%20pic?alt=media"
                
            
        # Download the image from the URL
        response = requests.get(image_url)
        
        # Check if the image was downloaded successfully
        if response.status_code == 200:
            # Save the image to the selected file path
            with open(file_path, "wb") as f:
                f.write(response.content)
            pop.showinfo("Complete","Image saved successfully!")
        else:
            pop.showerror("Operation fail !","Failed to download the image.")
    else:
        pop.showerror("Why ?","No file path selected.")
        

def right_click_event(event):
    # Define the behavior for the right-click event on pic_frame
    menuX.post(event.x_root, event.y_root)



def update_listbox(event):
    global selected_class
    selected_class = selected_class_var.get()
  
    stl.delete(0, 'end')

    try:

        
        datas = database.child("Students").child(selected_class).get()
        
        total_students_in_class = len(database.child("Students").child(selected_class).get().val() or {})
    
        Label(student_win,text=total_students_in_class,width=3, bg="#c36464",fg="#fff",font="arial 20 bold").place(x=280,y=115)
 
        for te in datas:
            
            stl.insert(END,te.val().get("name"))  
            
    except:
        
        pop.showerror("connection","check your inernet connection")
         

def update_window(event):
    global Sname, menuX, Sroll, Sdob, Sfather, Smother, Smobile, Sgender, Sclasss, Scategory, Ssubject, Saddressz, image_label, tk_image, SAadhar, SRegis, Sirdp
    
    selected_student_name = None  # Default value if no item is selected
    
    
    selected_indices = stl.curselection()
    if selected_indices:
        selected_student_name = stl.get(selected_indices[0])
    else:
        # Handle the case where no item is selected in the Listbox
        return
    
    fetchDetail = database.child("Students").child(selected_class).child(selected_student_name).get().val()
    if fetchDetail is None:
        # Handle the case where no data is found for the selected student
        return
    
    # Accessing details for the selected student
    Sname = fetchDetail.get("name")
    Sroll = fetchDetail.get("roll")
    Sdob = fetchDetail.get("dob")
    Sfather = fetchDetail.get("father")
    Smobile = fetchDetail.get("mobile")
    Smother = fetchDetail.get("mother")
    Sgender = fetchDetail.get("gender")
    Sclasss = fetchDetail.get("class")
    Scategory = fetchDetail.get("category")
    SAadhar = fetchDetail.get("aadhar")
    SRegis = fetchDetail.get("account")
    Sirdp = fetchDetail.get("bpl")
    
    

    try:
        clear_window()
    except:
        pass
    
    label_widgets = []
    
    # Clearing previous labels
    for widget in label_widgets:
        widget.destroy()
    label_widgets.clear()
    
    # Labels
    Label(FMR, text="Name", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=30, y=50)
    Label(FMR, text="Roll No.", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=30, y=100)
    Label(FMR, text="Class", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=30, y=150)
    Label(FMR, text="Father's Name", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=500, y=50)
    Label(FMR, text="Mother's Name", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=500, y=100)
    Label(FMR, text="DOB", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=500, y=150)
    
    Label(FMR, text=Sname, font="arial 15", bg="#EDEDED", fg="#06283D").place(x=160, y=50)
    Label(FMR, text=Sroll, font="arial 15", bg="#EDEDED", fg="#06283D").place(x=160, y=100)
    Label(FMR, text=Sclasss, font="arial 15", bg="#EDEDED", fg="#06283D").place(x=160, y=150)
    Label(FMR, text=Sfather, font="arial 15", bg="#EDEDED", fg="#06283D").place(x=680, y=50)
    Label(FMR, text=Smother, font="arial 15", bg="#EDEDED", fg="#06283D").place(x=680, y=100)
    Label(FMR, text=Sdob, font="arial 15", bg="#EDEDED", fg="#06283D").place(x=680, y=150)

    # Labels
    Label(FMR2, text="Gender", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=30, y=50)
    Label(FMR2, text="Mobile no.", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=30, y=100)
    Label(FMR2, text="Aadhar no.", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=30, y=150)
    Label(FMR2, text="IRDP/BPL", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=500, y=50)
    Label(FMR2, text="Category", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=500, y=100)
    Label(FMR2, text="Account No.", font="arial 15", bg="#EDEDED", fg="#06283D").place(x=500, y=150)

    Label(FMR2, text=Sgender, font="arial 15", bg="#EDEDED", fg="#06283D").place(x=160, y=50)
    Label(FMR2, text=Smobile, font="arial 15", bg="#EDEDED", fg="#06283D").place(x=160, y=100)
    Label(FMR2, text=SAadhar, font="arial 15", bg="#EDEDED", fg="#06283D").place(x=160, y=150)
    Label(FMR2, text=Sirdp, font="arial 15", bg="#EDEDED", fg="#06283D").place(x=680, y=50)
    Label(FMR2, text=Scategory, font="arial 15", bg="#EDEDED", fg="#06283D").place(x=680, y=100)
    Label(FMR2, text=SRegis, font="arial 15", bg="#EDEDED", fg="#06283D").place(x=680, y=150)
    
    # Destroy the existing photo-related widgets
    try:
        image_label.destroy()
        tk_image = None
    except:
        pass 
    
    if Sclasss in ["6th", "7th", "8th", "9th", "10th"]:
        if " " not in Sname:
            Surl = f"https://firebasestorage.googleapis.com/v0/b/bhoranj-19369.appspot.com/o/{Sclasss}%20class%2F{Sname}%20{Sclasss}%20pic?alt=media"
        else:    
            Surl = f"https://firebasestorage.googleapis.com/v0/b/bhoranj-19369.appspot.com/o/{Sclasss.replace(' ','%20')}%20class%2F{Sname.replace(' ','%20')}%20{Sclasss}%20pic?alt=media"
            
    elif Sclasss in [ "10+1 (Science)", "10+1 (Commerce)", "10+1 (Arts)"]:
        dictionary = {"10+1 (Science)":"Science", "10+1 (Commerce)": "Commerce", "10+1 (Arts)": "Arts"}
        if " " not in Sname:
            Surl = f"https://firebasestorage.googleapis.com/v0/b/bhoranj-19369.appspot.com/o/10%20%20%201%20class%2F10%201%20({dictionary[Sclasss]})%2F{Sname}%20{Sclasss}%20pic?alt=media"
        else:    
            Surl = f"https://firebasestorage.googleapis.com/v0/b/bhoranj-19369.appspot.com/o/10%20%20%201%20class%2F10%201%20({dictionary[Sclasss]})%2F{Sname.replace(' ','%20')}%20{Sclasss}%20pic?alt=media"
            
    elif Sclasss in [ "10+2 (Science)", "10+2 (Commerce)", "10+2 (Arts)"]:
        dictionaryZ = {"10+2 (Science)":"Science", "10+2 (Commerce)": "Commerce", "10+2 (Arts)": "Arts"}
        if " " not in Sname:
            Surl = f"https://firebasestorage.googleapis.com/v0/b/bhoranj-19369.appspot.com/o/10%20%20%202%20class%2F10%202%20({dictionaryZ[Sclasss]})%2F{Sname}%20{Sclasss}%20pic?alt=media"
        else:    
            Surl = f"https://firebasestorage.googleapis.com/v0/b/bhoranj-19369.appspot.com/o/10%20%20%202%20class%2F10%202%20({dictionaryZ[Sclasss]})%2F{Sname.replace(' ','%20')}%20{Sclasss}%20pic?alt=media"
            
    else:
        pop.showerror("What happens","Something went wrong")
    
    response7 = requests.get(Surl)
    if response7.status_code == 200:
        try:
            tk_image = ImageTk.PhotoImage(Image.open(BytesIO(response7.content)).resize((200, 245)))
            image_label = Label(student_win, image=tk_image)
            image_label.image = tk_image  
            image_label.place(x=1310, y=200)
        except Exception as img_err:
            pop.showerror("Image problem",f"Error displaying image: {img_err}")

    else:
        pop.showwarning("Not exist", "This photo is not exist in firebase storage")
        
    # Create a menu for the right-click event
    menuX = Menu(student_win, tearoff=0)
    menuX.add_command(label="Save as", command=save_as)
    
    # Associate the menu with the right-click event on the image label
    image_label.bind("<Button-3>", lambda event: menuX.post(event.x_root, event.y_root))


    

def add_student():

        def submit():
            name = entry_SName.get()
            roll = entry_SRoll.get()
            dob = enter_dob.get()
            gender = Gender
            mobile = SMob.get()
            father = SFather.get()
            mother = SMother.get()
            category = category_var1.get()
            aadhar = Saadhar.get()
            account = Sregis.get()
            irdp = BPL
            classs = selected_class_var2.get()
            
            if classs in ["6th", "7th", "8th", "9th", "10th"]:
                
                storage.child(f"{classs} class").child(f"{name} {classs} pic").put(file_path2)
                url = storage.child(f"{classs} class").child(f"{name} pic").get_url(None)
                
            elif classs in [ "10+1 (Science)", "10+1 (Commerce)", "10+1 (Arts)"]:
                   
                storage.child("10 + 1 class").child(classs).child(f"{name} {classs} pic").put(file_path2)
                url = storage.child(f"{classs} class").child(f"{name} pic").get_url(None)
                
            elif classs in [ "10+2 (Science)", "10+2 (Commerce)", "10+2 (Arts)"]:
                   
                storage.child("10 + 2 class").child(classs).child(f"{name} {classs} pic").put(file_path2)
                url = storage.child(f"{classs} class").child(f"{name} pic").get_url(None)
                
            else:
                pop.showerror("Wrong","Something went wrong")
                
            vv2 = messagebox.askyesno("Really??", "Do you really want to add data?")
            
            if vv2:
                        dataa = f"Name: {name}\nRoll: {roll}\nmobile: {mobile}\nFather: {father}\nMother: {mother}\nClass: {selected_class_var2}\nAadhar: {Saadhar}\nAccount no. {Sregis}\nBPL: {BPL}\nGender: {gender}\nCategory: {category}\nPhoto: Done"
                        messagebox.showinfo("Data", dataa)

                        
                        try:
                                query = {
                                        "name": name,
                                        "roll": roll,
                                        "dob" : dob,
                                        "father": father,
                                        "mobile": mobile,
                                        "mother": mother,
                                        "gender": gender,
                                        "class": classs,
                                        "account": Sregis,
                                        "aadhar": Saadhar,
                                        "category": category,
                                        "aadhar": aadhar,
                                        "account": account,
                                        "bpl" : irdp,
                                        "photo": url    
                                }
                                
                                database.child("Students").child(classs).child(name).set(query)
                                messagebox.showinfo("Success", "Data inserted successfully!")
                                
                        except Exception as e:
                                messagebox.showerror("Error", f"Error inserting data: {e}")
                                
            else:
                       pass


    
    
    
    
        try:
                student_win.destroy()
        except:
                pass
        global roots
        
        roots = Tk()
        roots.title("Adding student")
        roots.state("zoomed")
        roots.config(bg="#06283D")
        roots.geometry(f"{roots.winfo_screenwidth()}x{roots.winfo_screenheight()}")
        roots.minsize(roots.winfo_screenwidth(), roots.winfo_screenheight())
          

        def selection():
            global Gender
            value=Sradio.get()
            if value ==1:
                Gender = "Male"
            else:
                Gender = "Female"

        Label(roots,text="Email :  anshitrangra07@outlook.com",width=10,height=3,bg="#f0687c",anchor="e",).pack(side=TOP,fill=X)
        Label(roots,text="Student Registration ",width=10,height=3,bg="#c36464",fg="#fff",font="arial 20 bold").pack(side=TOP,fill=X)

        # 1st frame of window ==============================================================

        obj = LabelFrame(roots,text="Student's details",font=20,bd=2,width=1100,bg="#EDEDED",fg="#06283D",height=260,relief=GROOVE)
        obj.place(x=30,y=200)

        # /////////////////////////////////?????????????????????????? LABELS  {{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}
        Label(obj,text="Name",font="arial 15",bg="#EDEDED",fg="#06283D").place(x=30,y=50)
        Label(obj,text="Roll No.",font="arial 15",bg="#EDEDED",fg="#06283D").place(x=30,y=100)
        Label(obj,text="DOB",font="arial 15",bg="#EDEDED",fg="#06283D").place(x=30,y=150)

        Label(obj,text="Father's name",font="arial 15",bg="#EDEDED",fg="#06283D").place(x=500,y=50)
        Label(obj,text="Mother's name",font="arial 15",bg="#EDEDED",fg="#06283D").place(x=500,y=100)
        Label(obj,text="Gender",font="arial 15",bg="#EDEDED",fg="#06283D").place(x=500,y=150)

        # ;''''''''''''''''''''''''''''''''''''''''DATA"""""""""""""""""""""""""""''''''''''
        SName = StringVar()
        entry_SName = Entry(obj,textvariable=SName,width=25,font="arial 13")
        entry_SName.place(x=160,y=50)


        def validate_input(new_value):
            if new_value.isdigit() or new_value == "":
                return True
            else:
                return False
        validate_cmd = roots.register(validate_input)

        SRoll = StringVar()
        entry_SRoll = Entry(obj,textvariable=SRoll,width=25,font="arial 13", validate="key", validatecommand=(validate_cmd, '%P'))
        entry_SRoll.place(x=160, y=100)

        enter_dob = DateEntry(obj,bg="#06283D",width=25,font="arial 12")
        enter_dob.place(x=160,y=150)



        SFather = StringVar()
        entry_SFather = Entry(obj,textvariable=SFather,width=25,font="arial 13")
        entry_SFather.place(x=680,y=50)

        SMother = StringVar()
        entry_SMother = Entry(obj,textvariable=SMother,width=25,font="arial 13")
        entry_SMother.place(x=680,y=100)



        Sradio = IntVar()
        SGender1 = Radiobutton(obj,text="Male",variable=Sradio,font="arial 13",value=1,bg="#EDEDED",fg="#06283D",command=selection)
        SGender1.place(x=680,y=150)

        SGender2 = Radiobutton(obj,text="Female",variable=Sradio,font="arial 13",value=2,bg="#EDEDED",fg="#06283D",command=selection)
        SGender2.place(x=790,y=150)

        # 2nd frame of window/////////////////////////////////////////////////////////////

        obj2 = LabelFrame(roots,text="Student's details",font=20,bd=2,width=1100,bg="#EDEDED",fg="#06283D",height=260,relief=GROOVE)
        obj2.place(x=30,y=485)

        # /////////////////////////////////?????????????????????????? LABELS  {{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}
        Label(obj2,text="Class",font="arial 15",bg="#EDEDED",fg="#06283D").place(x=30,y=50)
        Label(obj2,text="Mobile no.",font="arial 15",bg="#EDEDED",fg="#06283D").place(x=30,y=100)
        Label(obj2,text="Category",font="arial 15",bg="#EDEDED",fg="#06283D").place(x=30,y=150)

        Label(obj2,text="IRDP/BPL",font="arial 15",bg="#EDEDED",fg="#06283D").place(x=500,y=50)
        Label(obj2,text="Aadhar no.",font="arial 15",bg="#EDEDED",fg="#06283D").place(x=500,y=100)
        Label(obj2,text="Account no.",font="arial 15",bg="#EDEDED",fg="#06283D").place(x=500,y=150)
        

        # ;''''''''''''''''''''''''''''''''''''''''DATA"""""""""""""""""""""""""""''''''''''

        def upload_photo():

                global file_path2

                file_path2 = filedialog.askopenfilename(title="Select Photo", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
                if file_path2:
                    messagebox.showinfo("Photo Selected", f"Selected Photo: {file_path2}")
                    img = (Image.open(file_path2))
                    imgrs = img.resize((200,245))
                    pc2 = ImageTk.PhotoImage(imgrs)
                    imgFM_label.config(image=pc2)
                    imgFM_label.image = pc2



        classs_options = ["6th", "7th", "8th", "9th", "10th", "10+1 (Science)", "10+1 (Commerce)", "10+1 (Arts)", "10+2 (Science)", "10+2 (Commerce)", "10+2 (Arts)"]
        selected_class_var2 = StringVar()
        selected_class_var2.set("Class")
        claass_combobox = ttk.Combobox(obj2, textvariable=selected_class_var2, values=classs_options, font="arial 12 ", state="readonly")
        claass_combobox.place(x=160,y=50)


        SMob = StringVar()
        entry_SMob = Entry(obj2,textvariable=SMob,width=25,font="arial 13", validate="key", validatecommand=(validate_cmd, '%P'))
        entry_SMob.place(x=160, y=100)
        
        Saadhar = StringVar()
        entry_Saadhar = Entry(obj2,textvariable=Saadhar,width=25,font="arial 13", validate="key", validatecommand=(validate_cmd, '%P'))
        entry_Saadhar.place(x=680, y=100)
        
        Sregis = StringVar()
        entry_Sregis = Entry(obj2,textvariable=Sregis,width=25,font="arial 13")
        entry_Sregis.place(x=680, y=150)


        categories = ["General", "OBC", "SC", "ST"]
        category_var1 = StringVar()
        category_var1.set("Select Category")
        category_combobox = ttk.Combobox(obj2, textvariable=category_var1, values=categories, font=("arial", 13), state="readonly")
        category_combobox.place(x=160,y=150)
        
        
        
        def mym():
            global BPL
            try:
                xx = chk_state.get()
                if xx == 1:
                    BPL = "Yes"
                else:
                    BPL = "No"
            except:
                BPL = "No"
                
        chk_state = BooleanVar(value=False)  # Initially set to False
        chk_button = Checkbutton(obj2, text="IRDP/BPL", font=("arial", 13),command=mym, variable=chk_state)
        chk_button.place(x=680, y=50)
        
        








        
        picFM = Frame(roots,bd=3,bg="black",width=200,height=245,relief=GROOVE)
        picFM.place(x=1250,y=200)

        try:
            image_urlFM = "https://firebasestorage.googleapis.com/v0/b/bhoranj-19369.appspot.com/o/Theme%2Flogo.png?alt=media&token=c8a97c5e-fdea-485b-9472-b2cec28a5921"
            responseFM = requests.get(image_urlFM)
            img_dataFM = BytesIO(responseFM.content)
            imgFM = Image.open(img_dataFM)
            imgFM = imgFM.resize((200, 245))
            photoFM = ImageTk.PhotoImage(imgFM)

            # Use photoFM instead of photo in the Label creation
            imgFM_label = Label(picFM, image=photoFM, bg='#040405')
            imgFM_label.image = photoFM  # Keep a reference to the image to prevent it from being garbage collected
            imgFM_label.place(x=0, y=0)
        except:
            pop.showerror("Conection lost","No internet connection !")
            sys.exit()



        Button(roots,text="Upload",command=upload_photo,width=19,height=2,font="arial 12 bold",bg="lightblue").place(x=1250,y=490)
        Button(roots,text="Save",command=submit,width=19,height=2,font="arial 12 bold",bg="lightgreen").place(x=1250,y=570)
        Button(roots,text="Back",command=go_back2,width=19,height=2,font="arial 12 bold",bg="gray").place(x=1250,y=650)


        roots.mainloop()

        
      
def del_student():
    try:
        selected_indices1 = stl.curselection()
        for index in reversed(selected_indices1):
            std_name = stl.get(index)

        confirm = messagebox.askyesno("Delete Student", f"Do you really want to delete data of {std_name}?")

        if confirm:
            try:
                stl.delete(selected_indices1)
                database.child("Students").child(selected_class).child(std_name).remove()
                
                # Assuming the file name in Firebase Storage is the same as the student name
                # You might need to adjust this based on your actual file naming convention
                file_name = f"{std_name} {Sclasss}.jpg"  # Change the file extension according to your files
                
                storage.delete(file_name)
                
                messagebox.showinfo("Data", "Data deleted successfully.")

            except Exception as e:
                messagebox.showerror("Error", f"Error deleting data: {e}")

    except:
        messagebox.showerror("Error", "You did not select any item from the listbox.")



#/////////////////////////////////////////////////////////////////////////////////

def go_back2():
        roots.destroy()
        child()
      
def go_back():
        root.destroy()
        teacher()

def backS():
   staff_win.destroy()
   mainwin()    
   
def backs():
       student_win.destroy()
       mainwin() 
       

#----------------------------------------------------------------------------------------------------------------------------------------------------------


def asking():
    ask = pop.askyesno("Wanna Quit ??","Do you really want to quit ??")
    if ask:
        window.destroy()
    else:
        pass



window = Tk()

# window.resizable(0, 0)
window.state('zoomed')
window.title('Login Page')
window.config(bg="black")
window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}")
window.minsize(window.winfo_screenwidth(), window.winfo_screenheight())
        

try:
    
    bg_frame = Image.open("background1.png")
    photo = ImageTk.PhotoImage(bg_frame)
    bg_panel = Label(window, image=photo)
    bg_panel.image = photo
    bg_panel.pack(fill=BOTH, expand=True)

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Login Frame
    lgn_frame = Frame(window, bg='#040405', width=950, height=600)
    lgn_frame.place(x=200, y=70)

    # Heading
    txt = "WELCOME"
    heading = Label(lgn_frame, text=txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                    fg='white', bd=5, relief=FLAT)
    heading.place(x=80, y=30, width=300, height=30)

    # Left Side Image

    side_image = Image.open("vector.png")
    photo = ImageTk.PhotoImage(side_image)
    side_image_label = Label(lgn_frame, image=photo, bg='#040405')
    side_image_label.image = photo
    side_image_label.place(x=5, y=100)

    # Sign In Image
    
    sign_in_image = Image.open("hyy.png")
    photo = ImageTk.PhotoImage(sign_in_image)
    sign_in_image_label = Label(lgn_frame, image=photo, bg='#040405')
    sign_in_image_label.image = photo
    sign_in_image_label.place(x=620, y=130)

    # Sign In label
    sign_in_label = Label(lgn_frame, text="Sign In", bg="#040405", fg="white",
                        font=("yu gothic ui", 17, "bold"))
    sign_in_label.place(x=650, y=240)

    # Username
    username_label = Label(lgn_frame, text="Username", bg="#040405", fg="#4f4e4d",
                        font=("yu gothic ui", 13, "bold"))
    username_label.place(x=550, y=300)

    username_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                        font=("yu gothic ui ", 12, "bold"), insertbackground='#6b6a69')
    username_entry.place(x=580, y=335, width=270)

    username_line = Canvas(lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
    username_line.place(x=550, y=359)

    # Username icon
    
    username_icon = Image.open("username_icon.png")
    photo = ImageTk.PhotoImage(username_icon)
    username_icon_label = Label(lgn_frame, image=photo, bg='#040405')
    username_icon_label.image = photo
    username_icon_label.place(x=550, y=332)

    # Login button
    
    lgn_button = Image.open("btn1.png")
    photo = ImageTk.PhotoImage(lgn_button)
    lgn_button_label = Label(lgn_frame, image=photo, bg='#040405')
    lgn_button_label.image = photo
    lgn_button_label.place(x=550, y=450)

    login = Button(lgn_button_label, text='LOGIN',command=interface, font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
    login.place(x=20, y=10)

    # Forgot password button
    forgot_button = Button(lgn_frame, text="Quit",command=asking ,font=("yu gothic ui", 13, "bold underline"), fg="white",
                        relief=FLAT, activebackground="#040405", borderwidth=0, background="#040405", cursor="hand2")
    forgot_button.place(x=630, y=510)




    # Password
    password_label = Label(lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
                        font=("yu gothic ui", 13, "bold"))
    password_label.place(x=550, y=380)

    password_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                        font=("yu gothic ui", 12, "bold"), show="*", insertbackground='#6b6a69')
    password_entry.place(x=580, y=416, width=244)

    password_line = Canvas(lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
    password_line.place(x=550, y=440)

    # Password icon
    
    password_icon = Image.open("password_icon.png")
    photo = ImageTk.PhotoImage(password_icon)
    password_icon_label = Label(lgn_frame, image=photo, bg='#040405')
    password_icon_label.image = photo
    password_icon_label.place(x=550, y=414)

    # Show/Hide password

    show_image = ImageTk.PhotoImage(file="show.png")
    hide_image = ImageTk.PhotoImage(file="hide.png")

    show_button = Button(lgn_frame, image=show_image, command=lambda: show_hide_password(True), relief=FLAT,
                        activebackground="white", borderwidth=0, background="white", cursor="hand2")
    show_button.place(x=860, y=420)
    
except:
    pop.showerror("No connection","No internet Connection.")
    sys.exit()

def show_hide_password(show):
    if show:
        hide_button = Button(lgn_frame, image=hide_image, command=lambda: show_hide_password(False), relief=FLAT,
                             activebackground="white", borderwidth=0, background="white", cursor="hand2")
        hide_button.place(x=860, y=420)
        password_entry.config(show='')
    else:
        show_button = Button(lgn_frame, image=show_image, command=lambda: show_hide_password(True), relief=FLAT,
                             activebackground="white", borderwidth=0, background="white", cursor="hand2")
        show_button.place(x=860, y=420)
        password_entry.config(show='*')

window.mainloop()

                        #       .   .
                        #         -