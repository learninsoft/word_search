from tkinter import *
from tkinter import ttk, font

main_window = Tk()

# Creating a Font object of "TkDefaultFont"
main_window.defaultFont = font.nametofont("TkDefaultFont")

main_window.defaultFont.configure(family="Times New Roman",
                           size=20,
                           weight=font.BOLD)

main_window.title("BariumSearch")
# main_window.geometry("512x768")
main_window.resizable(0, 1)
my_tree = ttk.Treeview(main_window)


def open_folder_btn_click(*args):
    print(args)
    # ask user for selection of folder from the system.
    folder_location_text['text'] = "Hello, button is clicked"
    folder_location_text['text'] += str(CheckVar1.get())
    folder_location_text['text'] += str(CheckVar2.get())


def read():
    return [(i,i*2,i*3,i*4) for i in range(1000)]


def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)

    for array in read():
        my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
    my_tree.grid(row=3, column=0, columnspan=5, rowspan=11, padx=10, pady=20)


def search_btn_click():

    print("Search button clicked")
    refreshTable()


# grid_frame = Frame(main_window)
grid_frame = main_window

location_label = Label(grid_frame, text='Location: ')
location_label.grid(row=0, column=0)

folder_location_text = Label(grid_frame, text=' ' * 10)
folder_location_text.grid(row=0, column=1, columnspan=6)

my_button = Button(grid_frame, text='Open Folder',
                   command=open_folder_btn_click)
# command=open_folder_btn_click, fg="blue", bg="#000000")

my_button.grid(row=0, column=8)

# ######################## row 2 ########################

file_type_label =  Label(grid_frame, text='File Type: ')
file_type_label.grid(row=1, column=0)

file_type_entry = Entry(grid_frame, text="*.txt")
file_type_entry.grid(row=1, column=1, columnspan=6)

CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(grid_frame, text = "Sub folders", variable = CheckVar1,
                 onvalue = 1, offvalue = 0, height=5,
                 width = 20, command=open_folder_btn_click)
C1.grid(row=1, column=8)

C2 = Checkbutton(grid_frame, text = "Case sensitive", variable = CheckVar2,
                 onvalue = 1, offvalue = 0, height=5,
                 width = 20, command=open_folder_btn_click)
C2.grid(row=1, column=9)

search_term_text = Label(grid_frame, text="Search Term")
search_term_text.grid(row=2, column=0)

# search_term_entry = Entry(grid_frame)
search_term_entry = Entry(grid_frame, width=55, bd=5, font=('Arial', 15))
search_term_entry.grid(row=2, column=1, columnspan=6, padx=50, pady=5)

search_btn = Button(grid_frame, text='Search',
                   command=search_btn_click)

search_btn.grid(row=2, column=8)

#
# v=Scrollbar(main_window, orient='vertical')
# v.pack(side=RIGHT, fill='y')
#
# # Add a text widget
# # text=Text(grid_frame, font=("Georgia, 24"))
# text=Text(grid_frame, font=("Georgia, 24"), yscrollcommand=v.set)
#
# # Add some text in the text widget
# for i in range(100):
#    text.insert(END, f"{i}Welcome to Tutorials point...\n\n")
#
# # Attach the scrollbar with the text widget
# v.config(command=text.yview)
# text.grid(row=3)
# # text.grid_columnconfigure(0, weight=6)

my_tree['columns'] = ("number", "number*2", "number*3", "number*4")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column(my_tree['columns'][0], anchor=W, width=170)
my_tree.column(my_tree['columns'][1], anchor=W, width=150)
my_tree.column(my_tree['columns'][2], anchor=W, width=150)
my_tree.column(my_tree['columns'][3], anchor=W, width=165)

my_tree.heading(my_tree['columns'][0], text=my_tree['columns'][0], anchor=W)
my_tree.heading(my_tree['columns'][1],text=my_tree['columns'][1], anchor=W)
my_tree.heading(my_tree['columns'][2],text=my_tree['columns'][2], anchor=W)
my_tree.heading(my_tree['columns'][3],text=my_tree['columns'][3], anchor=W)

refreshTable()

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold', 15))


# grid_frame.pack()
main_window.mainloop()
