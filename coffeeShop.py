
from tkinter import *
import customtkinter
from tkinter import messagebox
from datetime import date

window = customtkinter.CTk()
window.geometry("740x420")
window.config(bg="#25283b")
window.resizable(False, False)
window.title("S's Coffee Shop / Menu")

window2 = customtkinter.CTk()
window2.geometry("300x420")
window2.config(bg="#25283b")
window2.resizable(False, False)
window2.title("S's Coffee Shop / Bill")

prices = [12, 5, 8]
totalBill = 0

menuLabel = customtkinter.CTkLabel(
    window2, text="Thank You, Come Again.", text_color="#FFFFFF", bg_color="#25283b")
menuLabel.place(x=70, y=5)

image1 = PhotoImage(
    file=r"/Users/Sdeg/Documents/Etudes/Ivy_tech/SDEV_140/CoffeeShopProgram/coff.png")
image2 = PhotoImage(
    file=r"/Users/Sdeg/Documents/Etudes/Ivy_tech/SDEV_140/CoffeeShopProgram/coff.png")
image3 = PhotoImage(
    file=r"/Users/Sdeg/Documents/Etudes/Ivy_tech/SDEV_140/CoffeeShopProgram/coff.png")


def payBill():
    global totalBill
    if (userInput.get() == ""):
        messagebox.showerror(title="Error", message="Please insert your name!")
    else:
        totalBill = int(choice1comboBox.get()) * prices[0] + int(
            choice2comboBox.get()) * prices[1] + int(choice3comboBox.get()) * prices[2]
        if (totalBill == 0):
            messagebox.showwarning(
                title="Error", message="No drink was selected, select a drink!")
        else:
            name_label = customtkinter.CTkLabel(
                window2, text=f"Customer Name: {userInput.get()}", bg_color="#090b17", width=320, anchor=W)
            name_label.place(x=0, y=100)
            price_label = customtkinter.CTkLabel(
                window2, text=f"Total Price: $ {totalBill}", bg_color="#090b17", width=320, anchor=W)
            price_label.place(x=0, y=150)
            date_label = customtkinter.CTkLabel(
                window2, text=f"Bill Date: {date.today()}", bg_color="#090b17", width=320, anchor=W)
            date_label.place(x=0, y=200)


def restart():
    userInput.delete(0, END)
    choice1comboBox.set(0)
    choice2comboBox.set(0)
    choice3comboBox.set(0)


def saveBill():
    newFile = open(f"{userInput.get()} Bill", "w")
    newFile.write(f"Customer Name: {userInput.get()} \n")
    newFile.write(f"Total Price: $ {totalBill} \n")
    newFile.write(f"Bill Date: {date.today()}")
    messagebox.showinfo(title="Saved", message="Bill saved.")


image1Label = customtkinter.CTkLabel(window, image=image1, text="Cwindowucino\n Price: $ 12",  text_color="#FFFFFF",
                                     fg_color="#090b17", width=200, height=200, corner_radius=20, compound=TOP, anchor=N)
image1Label.place(x=30, y=70)
image2Label = customtkinter.CTkLabel(window, image=image2, text="Coffee\n Price: $ 5", text_color="#FFFFFF",
                                     fg_color="#090b17", width=200, height=200, corner_radius=20, compound=TOP, anchor=N)
image2Label.place(x=250, y=70)
image3Label = customtkinter.CTkLabel(window, image=image3, text="Espresso\n Price: $ 8", text_color="#FFFFFF",
                                     fg_color="#090b17", width=200, height=200, corner_radius=20, compound=TOP, anchor=N)
image3Label.place(x=470, y=70)

choice1comboBox = customtkinter.CTkComboBox(
    window, text_color="#000000", fg_color="#FFFFFF", values=("0", "1", "2"), state="readonly")
choice1comboBox.place(x=63, y=220)
choice1comboBox.set(0)

choice2comboBox = customtkinter.CTkComboBox(
    window, text_color="#000000", fg_color="#FFFFFF", values=("0", "1", "2"), state="readonly")
choice2comboBox.place(x=280, y=220)
choice2comboBox.set(0)

choice3comboBox = customtkinter.CTkComboBox(
    window, text_color="#000000", fg_color="#FFFFFF", values=("0", "1", "2"), state="readonly")
choice3comboBox.place(x=500, y=220)
choice3comboBox.set(0)

customerLabel = customtkinter.CTkLabel(
    window, text="Customer Name:", text_color="#FFFFFF", fg_color="#25283b")
customerLabel.place(x=40, y=300)

userInput = customtkinter.CTkEntry(
    window, text_color="#000000", fg_color="#FFFFFF", border_color="#FFFFFF", width=200)
userInput.place(x=200, y=300)

payBillButton = customtkinter.CTkButton(
    window, command=payBill, text="Pay Bill", fg_color="green", hover_color="turquoise", corner_radius=20)
payBillButton.place(x=100, y=350)

saveBillButton = customtkinter.CTkButton(
    window, command=saveBill, text="Save Bill", fg_color="green", hover_color="turquoise", corner_radius=20)
saveBillButton.place(x=250, y=350)

newBillButton = customtkinter.CTkButton(
    window, command=restart, text="New Bill", fg_color="green", hover_color="turquoise", corner_radius=20)
newBillButton.place(x=400, y=350)

exitButton = customtkinter.CTkButton(
    window, command=window.destroy, text="Exit", fg_color="blue", hover_color="turquoise", corner_radius=20)
exitButton.place(x=550, y=350)

exitButton2 = customtkinter.CTkButton(
    window2, command=window2.destroy, text="Exit", fg_color="blue", hover_color="turquoise", corner_radius=20)
exitButton2.place(x=80, y=350)


window.mainloop()
