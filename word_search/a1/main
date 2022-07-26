import os
from tkinter import *
from tkinter import ttk, font, filedialog

from searcher import search_word

main_window = Tk()
folder_path = ""

# Creating a Font object of "TkDefaultFont"
main_window.defaultFont = font.nametofont("TkDefaultFont")

main_window.defaultFont.configure(family="Times New Roman",
                           size=20,
                           weight=font.BOLD)

main_window.title("BariumSearch")
# main_window.geometry("512x768")
main_window.resizable(0, 1)
my_tree = ttk.Treeview(main_window)


def open_folder_btn_click():
    global folder_path
    folder_path = filedialog.askdirectory()
    print(folder_path)
    # ask user for selection of folder from the system.
    folder_location_text['text'] = folder_path


def refresh_table():
    for data in my_tree.get_children():
        my_tree.delete(data)
    search_result = search_word(word_to_search=search_term_entry.get(), same_case=CheckVar2.get())
    for i,array in enumerate(search_result, start=1):
        my_tree.insert(parent='', index='end', iid=array, text="", values=((i,) + array), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
    my_tree.grid(row=3, column=0, columnspan=8, rowspan=11, padx=10, pady=20)
    my_tree.bind("<Double-1>", item_double_click)


def item_double_click(event):
    item = my_tree.selection()[0]
    values = my_tree.item(item, "values")
    os.startfile(values[1])


def search_btn_click():

    print("Search button clicked")
    print(search_term_entry.get())
    print("Search button clicked")

    refresh_table()


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
#
# file_type_label =  Label(grid_frame, text='File Type: ')
# file_type_label.grid(row=1, column=0)
#
# file_type_entry = Entry(grid_frame, text="*.txt")
# file_type_entry.grid(row=1, column=1, columnspan=6)

CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(grid_frame, text = "Sub folders", variable = CheckVar1,
                 onvalue = 1, offvalue = 0, height=5,
                 width = 20, command=open_folder_btn_click)
C1.grid(row=1, column=0)

C2 = Checkbutton(grid_frame, text = "Case sensitive", variable = CheckVar2,
                 onvalue = 1, offvalue = 0, height=5, width = 20,)
C2.grid(row=1, column=1)

search_term_text = Label(grid_frame, text="Search Term")
search_term_text.grid(row=2, column=0)


# search_term_entry = Entry(grid_frame)
search_term_entry = Entry(grid_frame, width=55, bd=5, font=('Arial', 15))
search_term_entry.grid(row=2, column=1, columnspan=6, padx=50, pady=5)

search_btn = Button(grid_frame, text='Search',
                   command=search_btn_click)

search_btn.grid(row=2, column=8)

my_tree['columns'] = ("S.No", "File-Path", "Search_Term", "Word_Count")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column(my_tree['columns'][0], anchor=W, width=100)
my_tree.column(my_tree['columns'][1], anchor=W, width=180)
my_tree.column(my_tree['columns'][2], anchor=W, width=150)
my_tree.column(my_tree['columns'][3], anchor=W, width=150)

my_tree.heading(my_tree['columns'][0], text=my_tree['columns'][0], anchor=W)
my_tree.heading(my_tree['columns'][1],text=my_tree['columns'][1], anchor=W)
my_tree.heading(my_tree['columns'][2],text=my_tree['columns'][2], anchor=W)
my_tree.heading(my_tree['columns'][3],text=my_tree['columns'][3], anchor=W)

refresh_table()

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold', 15))


# grid_frame.pack()
main_window.mainloop()
