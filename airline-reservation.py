import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
from tkinter.ttk import Combobox
from tkcalendar import *


# ===========================================create database
con = sqlite3.connect('testcode.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS registerdata(
                    firstname text primary key, 
                    midname text, 
                    surname text, 
                    contact number, 
                    email text, 
                    nin number,
                    address text, 
                    username text,
                    password text
                )
            ''')
con.commit()


# ===========================================create database ends
# ===========================================Login page begins

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # load background image for log in page
        lp_loada = Image.open('airplane3.jpg')
        lp_loada1 = lp_loada.resize((1000, 1000))
        lp_photo = ImageTk.PhotoImage(lp_loada1)
        lp_ilabel = tk.Label(self, image=lp_photo)
        lp_ilabel.image = lp_photo
        lp_ilabel.place(x=0, y=0)

        # create top frame and its labels
        top_frame = tk.Frame(self, bg='white', width=1000, height=50)
        tf_abc = tk.Label(top_frame, text='ABC Airlines', fg='blue', bg='white',font=('Arial', 20, 'bold italic'), border=0)

        #load top frame button image
        btn_img2 = Image.open('contact3.png')
        btn_img2 = btn_img2.resize((80, 16))
        btn_pht2 = ImageTk.PhotoImage(btn_img2)
        fp_bimg2 = tk.Label(top_frame, image=btn_pht2)
        fp_bimg2.image = btn_pht2

        # username and password Frame & labels
        lp_lgfrm = tk.LabelFrame(self,bg='skyblue', bd=5,font=('Arial bold', 11), width=350, height=200)
        lp_uname = tk.Label(lp_lgfrm, text='Username', font=('Arial bold', 11), bg='skyblue', fg='white')
        lp_entuname = tk.Entry(lp_lgfrm, width=15, font='Arial 10', bd=0, relief='flat')
        lp_pword = tk.Label(lp_lgfrm, text='Password',font=('Arial bold', 11), bg='skyblue', fg='white')
        lp_entpword = tk.Entry(lp_lgfrm, width=15,font='Arial 10', bd=0, relief='flat', show='*')

        # bottom frame label
        btm_frame = tk.Frame(self, bg='blue', width=1000, height=50)

        # place labels on screen
        # top frame
        top_frame.grid(row=0, sticky="we")
        tf_abc.place(x=10, y=10)
        # username & psswrd
        lp_lgfrm.place(x=270, y=200)
        lp_uname.place(x=50, y=20)
        lp_entuname.place(x=180, y=20)
        lp_pword.place(x=50, y=80)
        lp_entpword.place(x=180, y=80)
        # bottom frame
        btm_frame.place(x=0, y=650)

        # function to open contact us window
        def contactus():
            lgcwindow = tk.Tk()
            lgcwindow.configure(bg='skyblue')
            lgcwindow.title('ABC Airlines')
            lgcwindow.geometry('700x270')
            def back():
                lambda: controller.show_frame(FrontPage)
                lgcwindow.destroy()
            # =================create labels on screen
            cu_fname = tk.Label(lgcwindow, text='''
            Dear esteemed customers, we can be reached via the following; \n
            Mobile numbers : 08157753460, 08157345272, 08057794555. \n
            Mails : abcinternational@gmail.com, abc1234@yahoo.com\n
            Our care centre will be delighted to assist you always.
            ''', font=('Arial', 11, 'bold'), justify='left', bg='sky blue', fg='white')

            cu_btn = tk.Button(lgcwindow, text='Back', border=2, relief='groove', bg='sky blue', fg='white',
                               font=('Arial', 10, 'bold'), command=back)

            # =================place labels on screen
            cu_fname.place(x=10, y=10)
            cu_btn.place(x=280, y=200)

        tf_cu = tk.Button(top_frame, image=btn_pht2, border=0, relief='flat',command=contactus)
        tf_cu.place(x=800, y=15)



        # login function
        def login():
            try:
                con = sqlite3.connect('testcode.db')
                c = con.cursor()
                for row in c.execute("Select * from registerdata"):
                    dbuname = row[7]
                    dbpwrd = row[8]

            except Exception as ep:
                messagebox.showerror('', ep)

            luname = lp_entuname.get()
            lpwd = lp_entpword.get()
            check_counter = 0
            if luname == "":
                warn = "Username can't be empty"
            else:
                check_counter += 1
            if lpwd == "":
                warn = "Password can't be empty"
            else:
                check_counter += 1
            if check_counter == 2:
                if (luname == dbuname and lpwd == dbpwrd):
                    messagebox.showinfo(
                        'Login Status', 'Logged in Successfully!')
                    controller.show_frame(FrontPage)

                else:
                    messagebox.showerror(
                        'Login Status', 'invalid username or password')
            else:
                messagebox.showerror('', warn)

        # Login submit details button
        lp_btn = tk.Button(lp_lgfrm, text='Log In', bg="skyblue", fg='white',font=('Arial bold', 10),relief='flat',
                           command=login)
        lp_btn.place(x=100, y=120)

        # ====================================================Register Window===========================================

        # register button function for new user account
        def regwindow():
            rwindow = tk.Tk()
            rwindow.configure(bg='skyblue')  # for background color
            rwindow.title('Register')
            rwindow.geometry('700x270')

            #=================create labels on screen
            rg_fname = tk.Label(rwindow, text='Firstname',font=('Arial', 11,'bold'), bg='sky blue',fg='white')
            rg_entfname = tk.Entry(rwindow, width=15, font='Arial 10', relief='flat')
            rg_mname = tk.Label(rwindow, text='Middlename',font=('Arial', 11,'bold'), bg='sky blue',fg='white')
            rg_entmname = tk.Entry(rwindow,width=15, font='Arial 10', relief='flat')
            rg_sname = tk.Label(rwindow, text='Surname',font=('Arial', 11,'bold'), bg='sky blue',fg='white')
            rg_entsname = tk.Entry(rwindow,width=15, font='Arial 10', relief='flat')
            rg_phne = tk.Label(rwindow, text='Contact', font=('Arial', 11,'bold'), bg='sky blue',fg='white')
            rg_entphne = tk.Entry(rwindow,width=15, font='Arial 10', relief='flat')
            rg_mail = tk.Label(rwindow, text='Mail', font=('Arial', 11,'bold'), bg='sky blue',fg='white')
            rg_entmail = tk.Entry(rwindow,width=15, font='Arial 10', relief='flat')
            rg_nin = tk.Label(rwindow, text='NIN', font=('Arial', 11,'bold'), bg='sky blue',fg='white')
            rg_entnin = tk.Entry(rwindow,width=15, font='Arial 10', relief='flat')
            rg_addr = tk.Label(rwindow, text='Address',font=('Arial', 11,'bold'), bg='sky blue',fg='white')
            rg_entaddr = tk.Entry(rwindow,width=50, font='Arial 10', relief='flat')
            rg_uname = tk.Label(rwindow, text='Username', font=('Arial', 11,'bold'), bg='sky blue',fg='white')
            rg_entuname = tk.Entry(rwindow,width=15, font='Arial 10', relief='flat')
            rg_pword = tk.Label(rwindow, text='Password', font=('Arial', 11,'bold'), bg='sky blue',fg='white')
            rg_entpword = tk.Entry( rwindow, width=15, font='Arial 10', relief='flat', show='*')  # 45.40(show='*')
            rg_cpword = tk.Label(rwindow, text='Confirm ',font=('Arial', 11,'bold'), bg='sky blue',fg='white')
            rg_entcpword = tk.Entry(rwindow, width=15, font='Arial 10', relief='flat', show='*')

            #=================place labels on screen
            rg_fname.place(x=10, y=10)
            rg_entfname.place(x=100, y=10)
            rg_mname.place(x=230, y=10)
            rg_entmname.place(x=340, y=10)
            rg_sname.place(x=470, y=10)
            rg_entsname.place(x=550, y=10)
            rg_phne.place(x=10, y=50)
            rg_entphne.place(x=100, y=50)
            rg_mail.place(x=230, y=50)
            rg_entmail.place(x=340, y=50)
            rg_nin.place(x=470, y=50)
            rg_entnin.place(x=550, y=50)
            rg_addr.place(x=10, y=100)
            rg_entaddr.place(x=100, y=100)
            rg_uname.place(x=10, y=150)
            rg_entuname.place(x=100, y=150)
            rg_pword.place(x=230, y=150)
            rg_entpword.place(x=340, y=150)
            rg_cpword.place(x=470, y=150)
            rg_entcpword.place(x=550, y=150)

            # function to submit customer register details
            def register():
                check_counter = 0
                warn = ""
                if rg_entfname.get() == "":
                    warn = "Name can't be empty"
                else:
                    check_counter += 1

                if rg_entmname.get() == "":
                    warn = "Mname can't be empty"
                else:
                    check_counter += 1

                if rg_entsname.get() == "":
                    warn = "Sname can't be empty"
                else:
                    check_counter += 1

                if rg_entphne.get() == "":
                    warn = "Phone can't be empty"
                else:
                    check_counter += 1

                if rg_entmail.get() == "":
                    warn = "Mail can't be empty"
                else:
                    check_counter += 1

                if rg_entnin.get() == "":
                    warn = "NIN can't be empty"
                else:
                    check_counter += 1

                if rg_entaddr.get() == "":
                    warn = "Address can't be empty"
                else:
                    check_counter += 1

                if rg_entuname.get() == "":
                    warn = "Username can't be empty"
                else:
                    check_counter += 1

                if rg_entpword.get() == "":
                    warn = "Password can't be empty"
                else:
                    check_counter += 1

                if rg_entcpword.get() == "":
                    warn = "Re-enter password can't be empty"
                else:
                    check_counter += 1

                if rg_entpword.get() != rg_entcpword.get():
                    warn = "Passwords didn't match!"
                else:
                    check_counter += 1

                if check_counter != 11:
                    messagebox.showerror('Error', warn)

                else:
                    try:
                        con = sqlite3.connect('testcode.db')
                        cur = con.cursor()
                        cur.execute('''INSERT INTO registerdata VALUES (:firstname,:midname,:surname, :email,:nin,  
                                       :contact, :address, :username, :password )''',
                                    {
                                        'firstname': rg_entfname.get(),
                                        'midname': rg_entmname.get(),
                                        'surname': rg_entsname.get(),
                                        'contact': rg_entphne.get(),
                                        'email': rg_entmail.get(),
                                        'nin':  rg_entnin.get(),
                                        'address': rg_entaddr.get(),
                                        'username': rg_entuname.get(),
                                        'password': rg_entpword.get(),
                                    })
                        con.commit()
                        messagebox.showinfo('confirmation', 'Record Saved')
                        controller.show_frame(LoginPage)
                    except Exception as ep:
                        messagebox.showerror('', ep)

            # Rg submit button
            rg_btn = tk.Button(rwindow, text='Submit', bg="skyblue",fg='white', font=('Arial bold', 10), command=register)
            rg_btn.place(x=300, y=200)

            rwindow.mainloop()

        # register button
        lp_btn = tk.Button(lp_lgfrm, text='Sign Up', bg="skyblue", fg='white',font=('Arial bold', 10),relief='flat',
                           command=regwindow)
        lp_btn.place(x=200, y=120)


# ====================================================Login Page=========================================================
# ====================================================Front Page=========================================================

class FrontPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # load images
        fp_imga = Image.open('airplane28.jpeg')
        fp_imgb = Image.open('airplane-inside3.jpeg')
        fp_imgc = Image.open('airplane-window0.jpeg')
        fp_imgd = Image.open('airplane-handshake7.jpeg')
        btn_img1 = Image.open('book-now1.jpg')
        btn_img2 = Image.open('contact3.png')

        # resize images to fit screen
        fp_img1 = fp_imga.resize((500,250))
        fp_img2 = fp_imgb.resize((500,250))
        fp_img3 = fp_imgc.resize((500,250))
        fp_img4 = fp_imgd.resize((500,250))
        btn_img1 = btn_img1.resize((90, 16))
        btn_img2 = btn_img2.resize((80, 16))

        # convert to python image format
        fp_pht1 = ImageTk.PhotoImage(fp_img1)
        fp_pht2 = ImageTk.PhotoImage(fp_img2)
        fp_pht3 = ImageTk.PhotoImage(fp_img3)
        fp_pht4 = ImageTk.PhotoImage(fp_img4)
        btn_pht1 = ImageTk.PhotoImage(btn_img1)
        btn_pht2 = ImageTk.PhotoImage(btn_img2)

        # create all main frames
        top_frame = tk.Frame(self, bg='white', width=1000, height=50)
        cntr_frame = tk.Frame(self, bg='cyan', width=1000, height=500)
        btm_frame = tk.Frame(self, bg='blue', width=1000, height=50)

        # create all sub frames
        cf_lu = tk.Frame(cntr_frame, bg='#141414', width=500, height=250)
        cf_ru = tk.Frame(cntr_frame, bg='#ffcc66', width=500, height=250)
        cf_ld = tk.Frame(cntr_frame, bg='#25dae9', width=500, height=250)
        cf_rd = tk.Frame(cntr_frame, bg='#f86263', width=500, height=250)

        # place images in label widgets
        fp_ilbl1 = tk.Label(cf_lu, image=fp_pht1, padx=100)
        fp_ilbl2 = tk.Label(cf_ru, image=fp_pht2)
        fp_ilbl3 = tk.Label(cf_ld, image=fp_pht3)
        fp_ilbl4 = tk.Label(cf_rd, image=fp_pht4)
        fp_bimg1 = tk.Label(top_frame, image=btn_pht1)
        fp_bimg2 = tk.Label(top_frame, image=btn_pht2)

        # equate image function to python photo
        fp_ilbl1.image = fp_pht1
        fp_ilbl2.image = fp_pht2
        fp_ilbl3.image = fp_pht3
        fp_ilbl4.image = fp_pht4
        fp_bimg1.image = btn_pht1
        fp_bimg2.image = btn_pht2

        # place image labels on screen
        fp_ilbl1.place(x=0, y=0)
        fp_ilbl2.place(x=0, y=0)
        fp_ilbl3.place(x=0, y=0)
        fp_ilbl4.place(x=0, y=0)


        # top frame labels
        tf_abc = tk.Label(top_frame, text = 'ABC Airlines', fg='blue', bg='white',
                          font=('Arial', 20, 'bold italic'),border = 0 )
        tf_bf = tk.Button(top_frame, image=btn_pht1, border = 0, relief = 'flat',
                          command = lambda: controller.show_frame(ReservationPage))

        # centre frame labels
        cf_lulbl = tk.Label(cf_lu, text = 'No Airline flies better......',fg='navyblue', bg='skyblue',
                          font=('Arial', 15, 'bold italic') )
        cf_rulbl = tk.Label(cf_ru, text="Comfort at it's peak.", fg='navyblue', bg='skyblue',
                            font=('Arial', 15, 'bold italic'))
        cf_ldlbl = tk.Label(cf_ld, text="Views like no other. ", fg='navyblue', bg='white',
                            font=('Arial', 15, 'bold italic'))
        cf_rdlbl = tk.Label(cf_rd, text="A Trial will convince you !!!", fg='navyblue', bg='white',
                            font=('Arial', 15, 'bold italic'))

        # place main frames on screen
        top_frame.grid(row=0,  sticky="we")
        cntr_frame.grid(row=1,  sticky='we')
        btm_frame.grid(row=5, sticky='we')

        # place sub frames on screen
        cf_lu.grid(row=0, column=0,  sticky="we")
        cf_ru.grid(row=0, column=1, sticky="we")
        cf_ld.grid(row=1, column=0, sticky="we")
        cf_rd.grid(row=1, column=1, sticky="we")

        # place top frame labels on screen
        tf_abc.place(x=10,y=10)
        tf_bf.place(x=600,y=15)

        # place centre frame labels on screen
        cf_lulbl.place(x=2, y=220)
        cf_rulbl.place(x=2, y=220)
        cf_ldlbl.place(x=2, y=220)
        cf_rdlbl.place(x=2, y=220)

        def contactus():
            cwindow = tk.Tk()
            cwindow.configure(bg='skyblue')
            cwindow.title('ABC Airlines')
            cwindow.geometry('700x270')

            def Back():
                lambda: controller.show_frame(FrontPage)
                cwindow.destroy()
            #=================create labels on screen
            cu_fname = tk.Label(cwindow, text='''
            Dear esteemed customers, we can be reached via the following; \n
            Mobile numbers : 08157753460, 08157345272, 08057794555. \n
            Mails : abcinternational@gmail.com, abc1234@yahoo.com\n
            Our care centre will be delighted to assist you always.
            ''',font=('Arial', 11,'bold'), justify='left', bg='sky blue',fg='white')

            cu_btn = tk.Button(cwindow, text= 'Back', border=2, relief='groove',bg='sky blue',fg='white',
                              font=('Arial', 10,'bold'),command=Back)

            #=================place labels on screen
            cu_fname.place(x=10, y=10)
            cu_btn.place(x=280, y=200)

        tf_cu = tk.Button(top_frame, image=btn_pht2, border = 0, relief = 'flat',
                         command = contactus)
        tf_cu.place(x=800,y=15)

# ====================================================Front Page=========================================================
# ====================================================Reservation Page=========================================================

class ReservationPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # page background colour
        self.configure(bg='navyblue')

        # connect to database
        con = sqlite3.connect('testcode.db')
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS reservationdata (
                            firstname text primary key, midname text, surname text, contact number, email text, 
                            address text,  class text,ticket text, age text, departure text,destination text,
                             date number,time text, amount number ) '''
                    )
        con.commit()

        # summary bill page window
        def bill():
            widow = tk.Tk()
            widow.configure(bg='navyblue')  # for background color
            widow.title('Bill page')
            widow.geometry('600x400')

            def quit():
                lambda: controller.show_frame(ReservationPage)
                widow.destroy()

            #('Arial', 15, 'bold')navyblue

            # Create naming Labels to identify gotten values
            fnamebil1 = Label(widow, text="FIRST NAME :", font=('Arial', 11, 'bold'), bg='navyblue',fg='white')
            mnamebil2 = Label(widow, text="MIDDLE NAME :", font=('Arial', 11, 'bold'), bg='navyblue',fg='white')
            snamebil3 = Label(widow, text="SURNAME : ", font=('Arial', 11, 'bold'), bg='navyblue',fg='white')
            phnebil4 = Label(widow, text="PHONE NO :", font=('Arial', 11, 'bold'), bg='navyblue',fg='white')
            emailbil5 = Label(widow, text="EMAIL :", font=('Arial', 11, 'bold'), bg='navyblue',fg='white')
            clasbil6 = Label(widow, text="CLASS :", font=('Arial', 11, 'bold'), bg='navyblue',fg='white')
            ticketbil7 = Label(widow, text="TICKET :", font=('Arial', 11, 'bold'), bg='navyblue',fg='white')
            agebil8 = Label(widow, text="AGE GROUP :", font=('Arial', 11, 'bold'), bg='navyblue',fg='white')
            dptrbil9 = Label(widow, text="DEPARTURE :", font=('Arial', 11, 'bold'), bg='navyblue',fg='white')
            dstnbil10 = Label(widow, text="DESTINATION :", font=('Arial', 11, 'bold'), bg='navyblue',fg='white')
            timebil11 = Label(widow, text="TIME :", font=('Arial', 11, 'bold'), bg='navyblue',fg='white')
            datebil12 = Label(widow, text="DATE :", font=('Arial', 11, 'bold'), bg='navyblue',fg='white')

            # place naming labels on the window
            fnamebil1.place(x=10, y=50)
            mnamebil2.place(x=200, y=50)
            snamebil3.place(x=400, y=50)
            phnebil4.place(x=10, y=100)
            emailbil5.place(x=200, y=100)
            clasbil6.place(x=10, y=150)
            ticketbil7.place(x=200, y=150)
            agebil8.place(x=400, y=150)
            dptrbil9.place(x=10, y=200)
            dstnbil10.place(x=200, y=200)
            timebil11.place(x=10, y=250)
            datebil12.place(x=200, y=250)

            # Create empty Labels to print gotten values in
            fnamebil = Label(widow, text="", font=('Arial', 11, 'bold'), bg='navyblue',fg='white')
            mnamebil = Label(widow, text="", font=('Arial', 11, 'bold'), bg='navyblue',fg='white')
            snamebil = Label(widow, text="", font=('Arial', 11, 'bold'), bg='navyblue',fg='white')
            phnebil = Label(widow, text="", font=('Arial', 11, 'bold'), bg='navyblue',fg='white')
            emailbil = Label(widow, text="", font=('Arial', 11, 'bold'), bg='navyblue',fg='white')
            clasbil = Label(widow, text="", font=('Arial', 11, 'bold'), bg='navyblue',fg='white')
            ticketbil = Label(widow, text="", font=('Arial', 11, 'bold'), bg='navyblue',fg='white')
            agebil = Label(widow, text="", font=('Arial', 11, 'bold'), bg='navyblue',fg='white')
            dptrbil = Label(widow, text="", font=('Arial', 11, 'bold'), bg='navyblue',fg='white')
            dstnbil = Label(widow, text="", font=('Arial', 11, 'bold'), bg='navyblue',fg='white')
            timebil = Label(widow, text="", font=('Arial', 11, 'bold'), bg='navyblue',fg='white')
            datebil = Label(widow, text="", font=('Arial', 11, 'bold'), bg='navyblue',fg='white')
            fp_btn = tk.Button(widow, text='BACK', bg="blue",fg='white',relief='groove', font='Arial, 10',
                               command=quit)

            #place empty labels on the window
            fnamebil.place(x=100, y=50)
            mnamebil.place(x=305, y=50)
            snamebil.place(x=480, y=50)
            phnebil.place(x=100, y=100)
            emailbil.place(x=255, y=100)
            clasbil.place(x=75, y=150)
            ticketbil.place(x=270, y=150)
            agebil.place(x=505, y=150)
            dptrbil.place(x=115, y=200)
            dstnbil.place(x=315, y=200)
            timebil.place(x=60, y=250)
            datebil.place(x=250, y=250)
            fp_btn.place(x=220, y=300)


            # function to get entered values and update on created labels
            def returnEntry(arg=None):
                # get values
                fname1 = fp_efname.get()
                mname2 = fp_emname.get()
                sname3 = fp_esname.get()
                phne4 = fp_ephne.get()
                email5 = fp_email.get()
                clas6 = clas.get()
                ticket7 = ticket.get()
                age8 = age.get()
                dptr9 = fpdpt.get()
                dstn10 = fpdtn.get()
                time11 = fptme.get()
                date12 = fp_edte.get()

                # paste on created labels
                fnamebil.config(text=fname1)
                mnamebil.config(text=mname2)
                snamebil.config(text=sname3)
                phnebil.config(text=phne4)
                emailbil.config(text=email5)
                clasbil.config(text=clas6)
                ticketbil.config(text=ticket7)
                agebil.config(text=age8)
                dptrbil.config(text=dptr9)
                dstnbil.config(text=dstn10)
                timebil.config(text=time11)
                datebil.config(text=date12)

            returnEntry()
            widow.mainloop()




        # Reserve button function
        def reserve():
            try:

                #get amount from database and calculate total amount
                db = sqlite3.connect('testcode.db')
                cursor = db.cursor()
                query = "SELECT price FROM prcetable where departure = '"+fpdpt.get()+"' and destination='"+fpdtn.get()+"'"
                cursor.execute(query)
                v_dAmount = cursor.fetchone()[0] #this is the amount from database

                v_class = clas.get() #get selected class
                v_type = ticket.get() #get selected ticket
                v_age = age.get() #get selected age
                v_tAmount = 0 #default total amount

                #set toatal amount depending on selected class
                c_amnt = 0
                if v_class == "standard":
                    c_amnt = c_amnt + 1000
                elif v_class == "economy":
                    c_amnt = c_amnt + 2000
                elif v_class == "firstclass":
                    c_amnt = c_amnt + 3000

                t_amnt = 0
                if v_type == "single":
                    t_amnt = t_amnt + 300
                elif v_type == "return":
                    t_amnt = t_amnt + 600

                a_amnt = 0
                if v_age == "child":
                    a_amnt = a_amnt + 250
                elif v_age == "adult":
                    a_amnt = a_amnt + 500

                v_tAmount = v_dAmount + c_amnt + t_amnt + a_amnt


                #save to database
                con = sqlite3.connect('testcode.db')
                cur = con.cursor()
                cur.execute('''INSERT INTO reservationdata VALUES (:firstname,:midname,:surname,:contact, :email, 
                                                    :address,:class,:ticket,:age,:departure,:destination,
                                                    :date,:time,:amount )''',

                            {
                                'firstname': fp_efname.get(),
                                'midname': fp_emname.get(),
                                'surname': fp_esname.get(),
                                'contact': fp_ephne.get(),
                                'email': fp_email.get(),
                                'address': fp_eaddr.get(),
                                'class': clas.get(),
                                'ticket': ticket.get(),
                                'age': age.get(),
                                'departure': fpdpt.get(),
                                'destination': fpdtn.get(),
                                'date': fp_edte.get(),
                                'time': fptme.get(),
                                'amount': v_tAmount,

                            })
                con.commit()
                messagebox.showinfo('confirmation', 'Record Saved')
                controller.show_frame(LoginPage)

            except Exception as ep:
                messagebox.showerror('', ep)
        def reserve1():
            lambda: controller.reserve()
            controller.show_frame(PaymentPage)

        # Personal details title
        fp_pdt = tk.Label(self, text='PERSONAL DETAILS',fg='white', bg='navyblue',
                          font=('Arial', 20, 'bold italic'))
        fp_pdt.place(x=400, y=10)


        # ---------------------------------------
        # ====================first name
        fp_fname = tk.Label(self, text='FIRST NAME :', font=('Arial', 10, 'bold'), bg='navyblue',fg='white')
        fp_efname = tk.Entry(self, width=15, font=('Arial', 10, 'bold'), relief='flat')
        fp_efname.focus()
        fp_efname.bind("<Return>", lambda: controller.returnEntry)
        # =====================middle name
        fp_mname = tk.Label(self, text='MIDDLE NAME :', font=('Arial', 10, 'bold'), bg='navyblue',fg='white')
        fp_emname = tk.Entry(self, width=15, font=('Arial', 10, 'bold'), relief='flat')
        fp_emname.focus()
        fp_emname.bind("<Return>", lambda: controller.returnEntry)
        # =====================Surname
        fp_sname = tk.Label(self, text='SURNAME : ', font=('Arial', 10, 'bold'), bg='navyblue',fg='white')
        fp_esname = tk.Entry(self, width=15, font=('Arial', 10, 'bold'), relief='flat')
        fp_esname.focus()
        fp_esname.bind("<Return>", lambda: controller.returnEntry)
        #  =====================Phone no
        fp_phne = tk.Label(self, text='Phone no :', font=('Arial', 10, 'bold'), bg='navyblue',fg='white')
        fp_ephne = tk.Entry(self, width=15, font=('Arial', 10, 'bold'), relief='flat')
        fp_ephne.focus()
        fp_ephne.bind("<Return>", lambda: controller.returnEntry)
        #  =====================Email
        fp_mail = tk.Label(self, text='Email :', font=('Arial', 10, 'bold'), bg='navyblue',fg='white')
        fp_email = tk.Entry(self, width=37, font=('Arial', 10, 'bold'), relief='flat')
        fp_email.focus()
        fp_email.bind("<Return>", lambda: controller.returnEntry)
        #  =====================address
        fp_addr = tk.Label(self, text='Address :', font=('Arial', 10, 'bold'), bg='navyblue',fg='white')
        fp_eaddr = tk.Entry(self, width=75, font=('Arial', 10, 'bold'), relief='flat')
        #  =======================================================Ticket details title
        #  Ticket details title
        fp_tdt = tk.Label(self, text='Ticket details ', fg='white', bg='navyblue', font=('Arial', 20, 'bold italic'))
        # ---------------------------------------
        #  class label c/w (standard, economy, firstclass, radbuttons )
        clas = StringVar()
        fp_cls = tk.Label(self, text='Class :', font=('Arial', 10, 'bold'), bg='navyblue',fg='white')
        fp_std = tk.Radiobutton(self, text='standard', font=('Arial', 10, 'bold'), variable=clas, value='standard', bg='navyblue',fg='skyblue')
        fp_ecn = tk.Radiobutton(self, text='economy', font=('Arial', 10, 'bold'), variable=clas, value='economy', bg='navyblue',fg='skyblue')
        fp_fst = tk.Radiobutton( self, text='firstclass', font=('Arial', 10, 'bold'), variable=clas, value='firstclass', bg='navyblue',fg='skyblue')
        fp_std.select()
        # ---------------------------------------
        #  ticket type c/w (single, return radbuttons )
        ticket = StringVar()
        fp_tkt = tk.Label(self, text='ticket type', font=('Arial', 10, 'bold'), bg='navyblue',fg='white')
        fp_sng = tk.Radiobutton(self, text='single', font=('Arial', 10, 'bold'), variable=ticket, value='single', bg='navyblue',fg='skyblue')
        fp_rtn = tk.Radiobutton(self, text='return', font=('Arial', 10, 'bold'), variable=ticket, value='return', bg='navyblue',fg='skyblue')
        fp_sng.select()
        # ------------------------------------
        #  age group label c/w (adult, child radbuttons )
        age = StringVar()
        fp_agp = tk.Label(self, text='age group', font=('Arial', 10, 'bold'), bg='navyblue',fg='white')
        fp_chd = tk.Radiobutton(self, text='child', font=('Arial', 10, 'bold'), variable=age, value='child', bg='navyblue',fg='skyblue')
        fp_adt = tk.Radiobutton(self, text='adult', font=('Arial', 10, 'bold'), variable=age, value='adult', bg='navyblue',fg='skyblue')
        # ------------------------------------------------
        # ---Departure, Destination, Distance

        states = ['lagos', 'ogun', 'ibadan', 'ondo', 'osun']
        time = ['Morning', 'Evening']

        # =========================================Departure & Destination
        fp_dpt = tk.Label(self, text='Departure :', font=('Arial', 10, 'bold'), bg='navyblue',fg='white')
        fpdpt = StringVar()
        fp_edpt = Combobox(self, textvariable=fpdpt, values=states)
        fp_edpt.bind('<<ComboboxSelected>>')
        fp_edpt.current(1)
        #  Destination
        fp_dtn = tk.Label(self, text='Destination :', font=('Arial', 10, 'bold'), bg='navyblue',fg='white')
        fpdtn = StringVar()
        fp_edtn = Combobox(self, textvariable=fpdtn, values=states)
        fp_edtn.bind('<<ComboboxSelected>>')
        fp_edtn.current(1)
        # ------------------------------------
        # ===============Date & Time
        #  Time
        fp_tme = tk.Label(self, text='Time :', font=('Arial', 10, 'bold'), bg='navyblue',fg='white')
        fptme = StringVar()
        fp_etme = Combobox(self, textvariable=fptme, values=time)
        fp_etme.bind('<<ComboboxSelected>>')
        fp_etme.current(1)
        #  Date
        fp_dte = tk.Label(self, text='Select Date:', font=('Arial', 10, 'bold'), bg='navyblue',fg='white')
        fp_edte = DateEntry(self, setmode='day', date_pattern='d/m/yy' , relief='flat')


        # submit button for personal details
        fp_btn1 = tk.Button(self, text='Payment Page', bg="blue", fg='white',font=('Arial', 10, 'bold'), relief='groove',command=lambda: controller.show_frame(PaymentPage))
        fp_btn2 = tk.Button(self, text='Reserve', bg="blue", fg='white',font=('Arial', 10, 'bold'), relief='groove',command=reserve)
        fp_btn3 = tk.Button(self, text='Confirm Entry', bg="blue",fg='white', font=('Arial', 10, 'bold'), relief='groove',command=bill)



        #  ==========================Personal details title
        fp_fname.place(x=100, y=50)
        fp_efname.place(x=200, y=53)
        fp_mname.place(x=400, y=50)
        fp_emname.place(x=525, y=50)
        fp_sname.place(x=700, y=50)
        fp_esname.place(x=800, y=50)
        fp_phne.place(x=100, y=100)
        fp_ephne.place(x=200, y=100)
        fp_mail.place(x=400, y=100)
        fp_email.place(x=470, y=100)
        fp_addr.place(x=100, y=150)
        fp_eaddr.place(x=200, y=150)
        #  ==========================Ticket details title
        fp_tdt.place(x=400, y=200)
        #  ==========================class (standard, economy, firstclass, radbuttons )
        fp_cls.place(x=100, y=250)
        fp_std.place(x=200, y=250)
        fp_ecn.place(x=300, y=250)
        fp_fst.place(x=400, y=250)
        # ===========================ticket (single, return radbuttons )
        fp_tkt.place(x=100, y=300)
        fp_sng.place(x=200, y=300)
        fp_rtn.place(x=300, y=300)
        # ===========================age (adult, child radbuttons )
        fp_agp.place(x=100, y=350)
        fp_chd.place(x=200, y=350)
        fp_adt.place(x=300, y=350)
        fp_chd.select()
        # ===========================Departure & Destination
        fp_dpt.place(x=100, y=400)
        fp_edpt.place(x=200, y=400)
        fp_dtn.place(x=400, y=400)
        fp_edtn.place(x=500, y=400)
        # ===========================time, date, amount & Destination
        fp_tme.place(x=100, y=450)
        fp_etme.place(x=200, y=450)
        fp_dte.place(x=400, y=450)
        fp_edte.place(x=500, y=450)
        # ===========================confirm, reserve, next page
        fp_btn1.place(x=464, y=550)
        fp_btn2.place(x=400, y=550)
        fp_btn3.place(x=300, y=550)
# ====================================================Reservation Page=========================================================
# ====================================================Payment Page=======================================================

class PaymentPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # configure page background colour
        self.configure(bg='navyblue')

        def verifyotp():
            messagebox.showinfo('ABC Airline OTP', 'Your OTP is 12345')
            controller.show_frame(PaymentPage)

        def makepayment():
            messagebox.showinfo('ABC Airline Debit Card Payment', 'Payment made Successfully!')
            controller.show_frame(PaymentPage)

        # ===================================  Create labels =====================================
        # =======================Make payment title :
        sp_lbl = tk.Label(self, text='PAYMENT PAGE', font=('Arial', 15, 'bold '), bg='navyblue', fg='white')
        # =======================Ways to make payment :
        sp_wmp = tk.Label(self, text='Ways to make payment :', font=('Arial', 11, 'bold '), bg='navyblue', fg='white')
        sp_bt = tk.Label(self, text='1. Bank transfer', font=('Arial', 11, 'bold '), bg='navyblue', fg='white')
        sp_dc = tk.Label(self, text='2. Debit card ', font=('Arial', 11, 'bold '), bg='navyblue', fg='white')
        sp_op = tk.Label(self, text='3. Online 3D payment ', font=('Arial', 11, 'bold '), bg='navyblue', fg='white')
        # =======================1. Bank transfer
        sp_sbta = tk.Label(self, text='1. Bank transfer', font=('Arial', 11, 'bold '), bg='navyblue', fg='white')
        sp_sbtb = tk.Label(self, text='Kindly make payment to ABC airlines account details below ', font=('Arial', 11, 'bold '), bg='navyblue', fg='white')
        sp_sbtf = tk.Label(self, text='Please, send the evidence of payment to abctraveltransfer@abc.com.ng',font=('Arial', 11, 'bold '), bg='navyblue', fg='white')
        sp_sbtc = tk.Label(self, text='Account name : ABC TRAVEL TRANSFER ', font=('Arial', 11, 'bold '), bg='navyblue', fg='white')
        sp_sbtd = tk.Label(self, text='Bank : ECO BANK ', font=('Arial', 11, 'bold '), bg='navyblue', fg='white')
        sp_sbte = tk.Label(self, text='Account no :  1005234769', font=('Arial', 11, 'bold '), bg='navyblue', fg='white')
        # =======================2. Debit card :
        spesdca = StringVar
        spesdcb = StringVar
        spesdcc = StringVar
        spesdcd = StringVar
        sp_sdc = tk.Label(self, text='2. Debit card ', font=('Arial', 11, 'bold '), bg='navyblue', fg='white')
        sp_sdca = tk.Label(self, text='first 4 digits :', font=('Arial', 11, 'bold '), bg='navyblue', fg='white')
        sp_esdca = tk.Entry(self, text=spesdca, font=('Arial', 11, 'bold '), relief='flat')
        sp_sdcb = tk.Label(self, text='last 4 digits :', font=('Arial', 11, 'bold '), bg='navyblue', fg='white')
        sp_esdcb = tk.Entry(self, text=spesdcb, font=('Arial', 11, 'bold '),  relief='flat')
        sp_sdcc = tk.Label(self, text='ATM VS code :', font=('Arial', 11, 'bold '), bg='navyblue', fg='white')
        sp_esdcc = tk.Entry(self, text=spesdcc, font=('Arial', 11, 'bold '),  relief='flat')
        sp_sdcd = tk.Label(self, text='click verify to confirm details and receive OTP :', font=('Arial', 11, 'bold '), bg='navyblue', fg='white')
        sp_sdcb1 = tk.Button(self, text='VERIFY', font=('Arial', 10, 'bold '), bg='blue', fg='white',relief='groove', command=verifyotp)
        sp_sdce = tk.Label(self, text='Enter OTP value and click make payment below.', font=('Arial', 11, 'bold '), bg='navyblue', fg='white')
        sp_esdce = tk.Entry(self, text=spesdcd, font=('Arial', 10, 'bold '),  relief='flat')
        sp_sdcf = tk.Button(self, text='Make Payment', font=('Arial', 10, 'bold '), bg='blue', fg='white',relief='groove',command=makepayment)
        # =======================3. 3D online payment  :
        sp_lbl3da = tk.Label(self, text='3. 3D online payment ', font=('Arial', 11, 'bold '), bg='navyblue', fg='white')
        sp_lbl3db = tk.Label(self, text='click the link below to make online payment.	', font=('Arial', 11, 'bold '), bg='navyblue', fg='white')
        sp_lbl3dc = tk.Label(self, text='https://abctravle.abc.com/usp=installed_webapp/onlinetransfer_thirdparty',
                          font=('Arial', 11, 'bold '), bg='navyblue', fg='white')
        # =======================Next page button:
        sp_btn = tk.Button(self, text='Front Page', bg="blue", fg='white',relief='groove',font=('Arial', 10,'bold'),
                           command=lambda: controller.show_frame(FrontPage))

        #=======================Put labels on screen======================================================
        # Make payment title :
        sp_lbl.place(x=400, y=10)
        # =====================Ways to make payment :
        sp_wmp.place(x=100, y=50)
        sp_bt.place(x=100, y=75)
        sp_dc.place(x=100, y=100)
        sp_op.place(x=100, y=125)
        # =====================Bank transfer
        sp_sbta.place(x=100, y=175)
        sp_sbtb.place(x=100, y=200)
        sp_sbtf.place(x=100, y=225)
        sp_sbtc.place(x=100, y=250)
        sp_sbtd.place(x=100, y=275)
        sp_sbte.place(x=100, y=300)
        # =====================2. Debit card :
        sp_sdc.place(x=100, y=350)
        sp_sdca.place(x=100, y=375)
        sp_esdca.place(x=200, y=375)
        sp_sdcb.place(x=400, y=375)
        sp_esdcb.place(x=500, y=375)
        sp_sdcc.place(x=700, y=375)
        sp_esdcc.place(x=800, y=375)
        sp_sdcd.place(x=100, y=410)
        sp_sdcb1.place(x=500, y=410)
        sp_sdce.place(x=100, y=445)
        sp_esdce.place(x=500, y=445)
        sp_sdcf.place(x=500, y=485)
        # 3. =====================3D online payment  :
        sp_lbl3da.place(x=100, y=525)
        sp_lbl3db.place(x=100, y=550)
        sp_lbl3dc.place(x=100, y=575)
        # =====================submit button
        sp_btn.place(x=440, y=625)

# ====================================================Payment Page================================================
# ====================================================Application window================================================

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # create a window
        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=700)
        window.grid_columnconfigure(0, minsize=1000)

        #create frames for each page and put in dict
        self.frames = {}
        for F in (LoginPage, FrontPage, ReservationPage, PaymentPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(LoginPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title('ABC AIRLINES')

app = Application()
app.state('zoomed')
app.maxsize(3000, 2000)
app.mainloop()
