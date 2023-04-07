from tkinter import *
from tkinter import messagebox
import random
from PIL import ImageTk, Image
from tkinter import simpledialog
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# empty string
password = ''

# password creating function
def pass_function(pass_code, range_code):
    global password # using global variable for password
    password_list = [random.choice(pass_code) for i in range(int(range_code))]
    for i in password_list:
        password += i
    
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = entry_1.get() # website entry
    email = entry_2.get() # email entry
    password = entry_3.get() # password entry
    
    data_dict = {
        website: {
            'email':email,
            'pass':password   
        }
          
    }
    
    if len(entry_3.get()) == 0:
        messagebox.askokcancel(title="NULL VALUES-ERROR", message=f"No values were inputed, please try again.")
    else:
        # opening json file with R
        try: # trying to see if works
            with open('data.json', 'r') as datafile:
                # to read json file
                data = json.load(datafile) 
        except FileNotFoundError: # if file not found
            with open('data.json', 'w') as datafile:
                json.dump(data_dict, datafile, indent=4)
        else:
            data.update(data_dict)
            with open ("data.json", "w") as datafile:
                json.dump(data, datafile, indent=4)
        finally:    
            entry_1.delete(0, END) #website entry
            entry_3.delete(0, END) #password entry
 # ---------------------------- GENERATE PASSWORD ------------------------------- #           
def generate():
    global password
    if len(entry_3.get()) == 0:
        #input dialoge
        USER_INP_LETTERS = simpledialog.askstring(title="Password", prompt="How mnay letters would you like in your password?")              
        USER_INP_NUMBERS = simpledialog.askstring(title="Password", prompt="How many numbers would you like in your password?")               
        USER_INP_SYMBOLS = simpledialog.askstring(title="Password", prompt="How mnay symbols would you like in your password?")
        pass_function(letters, USER_INP_LETTERS)
        pass_function(numbers, USER_INP_NUMBERS)
        pass_function(symbols, USER_INP_SYMBOLS)
        # shuffling password
        x = list(password)
        random.shuffle(x)
        password = ''.join(x)
        entry_3.insert(0, password)
    
    else:
        entry_3.delete(0, END)
        USER_INP_LETTERS = simpledialog.askstring(title="Password", prompt="How mnay letters would you like in your password?")              
        USER_INP_NUMBERS = simpledialog.askstring(title="Password", prompt="How many numbers would you like in your password?")               
        USER_INP_SYMBOLS = simpledialog.askstring(title="Password", prompt="How mnay symbols would you like in your password?")
        pass_function(letters, USER_INP_LETTERS)
        pass_function(numbers, USER_INP_NUMBERS)
        pass_function(symbols, USER_INP_SYMBOLS)
        # shuffling password
        x = list(password)
        random.shuffle(x)
        password = ''.join(x)
        entry_3.insert(0, password)
# ---------------------------- FIND PASSWORD ------------------------------- #       
def find_password():
    website = entry_1.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
        
    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Brandon's Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = ImageTk.PhotoImage(Image.open("/Volumes/GoogleDrive/My Drive/Self projects (learning)/password-manager-start/minions_PNG15.png")) 
# MyPassImg = PhotoImage(file="")
canvas.create_image(125, 125, image=img)
canvas.grid(column=1,row=0)

# website label
website_label = Label(text="             Website:")
website_label.grid(column=0,row=1)

# email/user label
email_user_label = Label(text="Email/Username:")
email_user_label.grid(column=0,row=2)

# password label
password_label = Label(text="             Password:")
password_label.grid(column=0,row=3)

#Entries
entry_1 = Entry(width=38) #website entry
entry_1.focus()
entry_2 = Entry(width=38) #email entry
entry_3 = Entry(width=22) #password entry

entry_1.grid(column=1,row=1, columnspan=2)
entry_2.grid(column=1,row=2, columnspan=2)
entry_2.insert(0,"brandenosmith01@gmail.com")
entry_3.grid(column=1,row=3)

#Buttons
generate_password = Button(text="Generate Password",  width=13, command=generate)
generate_password.grid(column=2,row=3)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)

add = Button(text="Add", width=36, command=save)
add.grid(column=1, row=4, columnspan=2)


window.mainloop()




