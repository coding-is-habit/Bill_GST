from tkinter import *
import random
from tkinter import messagebox


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing App")
        bg_color = "purple"
        title = Label(self.root, text="Genral Store", bd=6, relief=GROOVE, bg=bg_color, fg="white",
                      font=("times new roman", 26, "bold"), pady=2).pack(fill=X)

        self.rice = IntVar()
        self.food_oil = IntVar()
        self.pulses = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()

        self.totalprice = StringVar()
        self.totaltax = StringVar()

        self.cname = StringVar()
        self.cphone = StringVar()
        x = random.randint(1000, 9999)
        self.cbill = StringVar()
        self.cbill.set(str(x))
        self.search_bill = StringVar()

        F1 = LabelFrame(self.root, text="Customer Details", font=("times new roman", 15, "bold"), fg="gold",bg=bg_color, bd=5, relief=GROOVE)
        F1.place(x=0, y=60, relwidth=1)

        cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg="white", font=("times new roman", 16, "bold")).grid(row=0, column=0, padx=15, pady=6)
        cname_txt = Entry(F1, width=15, bd=3, relief=SUNKEN, textvariable=self.cname, font=("arial", 16)).grid(row=0,column=1,padx=15,pady=6)

        cphone_lbl = Label(F1, text="Phone Number", bg=bg_color, fg="white", font=("times new roman", 16, "bold")).grid(row=0, column=2, padx=15, pady=6)
        cphone_txt = Entry(F1, width=15, bd=3, relief=SUNKEN, textvariable=self.cphone, font=("arial", 16)).grid(row=0,column=3,padx=15,pady=6)

        cbill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg="white", font=("times new roman", 16, "bold")).grid(row=0, column=4, padx=15, pady=6)
        cbill_txt = Entry(F1, width=15, bd=3, relief=SUNKEN, textvariable=self.search_bill, font=("arial", 16)).grid(row=0, column=5, padx=15, pady=6)

        bill_btn = Button(F1, text="Search", command=self.find_bill, width=10, bd=4, font=("arial", 12, "bold")).grid(row=0, column=6, padx=15, pady=6)

        F2 = LabelFrame(self.root, text="Groceries", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color, bd=5,relief=GROOVE)
        F2.place(x=0, y=140, width=1000, height=330)
        rice_lbl = Label(F2, text="Rice", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        rice_txt = Entry(F2, width=12, textvariable=self.rice, font=("times new roman", 16), bd=3, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=5)

        food_oil_lbl = Label(F2, text="Food Oil", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        food_oil_txt = Entry(F2, width=12, textvariable=self.food_oil, font=("times new roman", 16), bd=3,relief=SUNKEN).grid(row=1, column=1, padx=10, pady=5)

        pulses_lbl = Label(F2, text="Pulses", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        pulses_txt = Entry(F2, width=12, textvariable=self.pulses, font=("times new roman", 16), bd=3,relief=SUNKEN).grid(row=2, column=1, padx=10, pady=5)

        wheat_lbl = Label(F2, text="Wheat Flour", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        wheat_txt = Entry(F2, width=12, textvariable=self.wheat, font=("times new roman", 16), bd=3,relief=SUNKEN).grid(row=3, column=1, padx=10, pady=5)

        sugar_lbl = Label(F2, text="Sugar", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        sugar_txt = Entry(F2, width=12, textvariable=self.sugar, font=("times new roman", 16), bd=3,relief=SUNKEN).grid(row=4, column=1, padx=10, pady=5)

        tea_lbl = Label(F2, text="Tea", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5,column=0,padx=10,pady=5,sticky="w")
        tea_txt = Entry(F2, width=12, textvariable=self.tea, font=("times new roman", 16), bd=3, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=5)

        #Bill Frame
        F3 = Frame(self.root, bd=5, relief=GROOVE)
        F3.place(x=975, y=140, width=375, height=330)
        bill_title = Label(F3, text="Bill Area", font="Arial 15", bd=5, relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(F3, orient=VERTICAL)
        self.textarea = Text(F3,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        #Bill Menu Frame
        F4 = LabelFrame(self.root, text="Bill Menu", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color, bd=5,relief=GROOVE)
        F4.place(x=0, y=470, relwidth=1, height=235)
        totalprice_lbl = Label(F4, text="Total Groceries Bill(Rs.)", bg=bg_color, fg="white",
                       font=("times new roman", 16, "bold")).grid(row=1, column=0, padx=20, pady=10, sticky="w")
        totalprice_txt = Entry(F4, width=15, textvariable=self.totalprice, font="arial 15", bd=3, relief=SUNKEN).grid(row=1, column=1,padx=20, pady=10)

        totaltax_lbl = Label(F4, text="Groceries GST", bg=bg_color, fg="white", font=("times new roman", 16, "bold")).grid(row=1, column=2, padx=10, pady=10, sticky="w")
        totaltax_txt = Entry(F4, width=15, textvariable=self.totaltax, font="arial 15", bd=3, relief=SUNKEN).grid(row=1, column=3,padx=20, pady=10)
        btn_F = Frame(F4, bd=5, relief=GROOVE)
        btn_F.place(x=870, width=470, height=145)

        total_btn = Button(btn_F, command=self.total, text="Total", bg="lightgreen", fg="darkgreen", pady=20,font="arila 15 bold", width=6, bd=5, relief=GROOVE).grid(row=0, column=0, padx=7, pady=10)
        generate_btn = Button(btn_F, command=self.bill_area, text="Generate Bill", bg="cadetblue", fg="white", pady=20,font="arila 15 bold", width=11, bd=5, relief=GROOVE).grid(row=0, column=1, padx=5,pady=10)
        reset_btn = Button(btn_F, command=self.reset, text="Reset", bg="lightyellow", fg="black", pady=20,font="arila 15 bold", width=6, bd=5, relief=GROOVE).grid(row=0, column=2, padx=5, pady=10)
        exit_btn = Button(btn_F, command=self.exit, text="Exit", bg="orange", fg="white", pady=20, font="arila 15 bold",width=6, bd=5, relief=GROOVE).grid(row=0, column=3, padx=5, pady=10)

        co_frame = Frame(self.root, bg=bg_color)
        co_frame.place(x=1100, y=640, width=245, height=35)
        auth = Label(co_frame, text="Madhav Sharma", font=("Calibri 14"), fg="White", pady=40, bg=bg_color).pack()
        self.welcome_bill()

    def total(self):
        self.rice_price = self.rice.get() * 30
        self.food_oil_price = self.food_oil.get() * 30
        self.pulses_price = self.pulses.get() * 30
        self.wheat_price = self.wheat.get() * 30
        self.sugar_price = self.sugar.get() * 30
        self.tea_price = self.tea.get() * 30
        self.total_grocery = float(self.rice_price +self.food_oil_price +self.pulses_price +self.wheat_price +self.sugar_price +self.tea_price)
        self.totalprice.set(str(self.total_grocery))
        self.grocery_tax = round(self.total_grocery * 0.03, 2)
        self.totaltax.set(self.grocery_tax)
        self.Total = float(self.total_grocery +self.grocery_tax)

    def welcome_bill(self):
        self.textarea.delete('1.0', END)
        self.textarea.insert(END, "\tGenral Store\n")
        self.textarea.insert(END, f"\nInvoice Number : {self.cbill.get()}")
        self.textarea.insert(END, f"\nCustomer Name :{self.cname.get()} ")
        self.textarea.insert(END, f"\nMobile Number :{self.cphone.get()}")
        self.textarea.insert(END, f"\n-------------------------------------------")
        self.textarea.insert(END, f"\n  Product\t\t       Qty\t\t  Price")
        self.textarea.insert(END, f"\n-------------------------------------------")

    def bill_area(self):
        if self.cname.get() == "" or self.cphone.get() == "":  # Validation.
            messagebox.showerror("Error", "Customer Details must be filled!")
        elif self.totalprice.get() == "0.0" :
            messagebox.showerror("Error", "No Products Choosen!")
        else:
            self.welcome_bill()  
            if self.rice.get() != 0:
                self.textarea.insert(END, f"\n Rice\t\t\t {self.rice.get()}\t {self.rice_price}")
            if self.food_oil.get() != 0:
                self.textarea.insert(END, f"\n Food Oil\t\t\t {self.food_oil.get()}\t {self.food_oil_price}")
            if self.pulses.get() != 0:
                self.textarea.insert(END, f"\n Pulses\t\t\t {self.pulses.get()}\t {self.pulses_price}")
            if self.wheat.get() != 0:
                self.textarea.insert(END, f"\n Wheat Flour\t\t\t {self.wheat.get()}\t {self.wheat_price}")
            if self.sugar.get() != 0:
                self.textarea.insert(END, f"\n Sugar\t\t\t {self.sugar.get()}\t {self.sugar_price}")
            if self.tea.get() != 0:
                self.textarea.insert(END, f"\n Tea\t\t\t {self.tea.get()}\t {self.tea_price}")

            self.textarea.insert(END, f"\n-------------------------------------------")
            if self.totaltax.get() != "0.0":
                self.textarea.insert(END, f"\n Grocery Tax\t\t\t {self.grocery_tax}")

            self.textarea.insert(END, f"\n-------------------------------------------")

            self.textarea.insert(END, f"\n Total Bill :\t\t\t\t Rs.{self.Total}")
            self.textarea.insert(END, f"\n-------------------------------------------")

            self.textarea.config(state=DISABLED)   
            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you wish to save the Bill!")
        if op > 0:
            self.bill_data = self.textarea.get('1.0',END)  
            f1 = open("Bill_data/" + str(self.cbill.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill No. {self.cbill.get()} saved successfully!")
        else:
            return

    def find_bill(self):
        try:
            f1 = open("Bill_data/" + str(self.search_bill.get()) + ".txt", "r")
            data = f1.read()
            self.textarea.delete('1.0', END)
            self.textarea.insert(END, data)
            f1.close()
        except FileNotFoundError:
            messagebox.showerror("Error", "Invalid Bill Number!")
        except:
            print("oops")

    def reset(self):
        op = messagebox.askyesno("Reset", "Do you wish to clear data!")
        if op > 0:
            self.rice.set(0)
            self.food_oil.set(0)
            self.pulses.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            self.totalprice.set("")
            self.totaltax.set("")
            self.cname.set("")
            self.cphone.set("")
            self.cbill.set("")
            x = random.randint(1000, 9999)
            self.cbill.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()
        else:
            return
    def exit(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit!")
        if op > 0:
            self.root.destroy()
        else:
            return
root = Tk()
obj = Bill_App(root)
root.mainloop()