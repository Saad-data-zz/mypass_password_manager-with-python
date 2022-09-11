from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    #crearting one big list
    password_list = password_letters + password_symbols +password_numbers
    random.shuffle(password_list)

    #the join function in python used to concatainate string
    password = "".join(password_list)
    #now we're populate the password in the password field in the screen
    password_entry.insert(0,password)
    #using pyperclip will automatically copying the newly generated password into the clipboard
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    #getting hold of on our entry
    web = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    #if the user left any of the column of email or web empty then pop-up will be generated
    if len(web) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", messgae="Please make sure you haven't left any box empty.")
    else:
    #Using the message box to show the user pop=up that information is save
    #you can use the ask to ask anything from user
    #we also need to save the output of the messagebox
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \n"
                                              f" Email:{email}\nPassword:{password}\nIs it ok to save?")
        if is_ok:
            # opening te file in the append mood
            with open("data.txt", "a") as password_file:
                password_file.write(f"Web:{web} | ID:{email} | Password:{password}\n")
                web_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

#create the window with title
window = Tk()
window.minsize(width=200, height=200)
window.config(padx=50)
window.title("Password Manager")


#using canvas to load the image in the window
canvas = Canvas(width=200,height=200)
#we will use the PhotoImage lass of tkinter to load the image
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0,column=1)

#crating the labels
my_label = Label(text="@https://github.com/Saad-data", font=("arial",8, "normal"))
web_label = Label(text="Website:",  font=("arial",14, "bold"))
email_label = Label(text="Email/ Username:",  font=("arial",14, "bold"))
password_label = Label(text="Password:",  font=("arial",14, "bold"))
my_label.grid(column=1,row=0)
web_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

#entries
web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2)
#the focus will bring your cursal to the web_ertry
web_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
#it will populate the most commonly used email
email_entry.insert(0,"syedsaad047@gmail.com")
password_entry = Entry(width=21,)
password_entry.grid(column=1, row=3)

#buttons
generate_password_button = Button(text="Generated Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)















window.mainloop()