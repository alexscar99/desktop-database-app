from tkinter import Tk, Label, Entry, StringVar, Listbox, Scrollbar, Button, END, messagebox
import db_funcs


def get_selected_row(event):
    try:
        global selected_tuple
        index = lb1.curselection()[0]
        selected_tuple = lb1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass


def view():
    lb1.delete(0, END)
    for row in db_funcs.view_books():
        lb1.insert(END, row)


def search():
    lb1.delete(0, END)
    for row in db_funcs.search_book(title_text.get(), author_text.get(),
                                    year_text.get(), isbn_text.get()):
        lb1.insert(END, row)


def add():
    db_funcs.insert_book(title_text.get(), author_text.get(), year_text.get(),
                         isbn_text.get())
    lb1.delete(0, END)
    lb1.insert(END, (title_text.get(), author_text.get(), year_text.get(),
                     isbn_text.get()))


def delete():
    result = messagebox.askokcancel(
        "Delete", "Are you sure you want to delete this book?")
    if result == True:
        db_funcs.delete_book(selected_tuple[0])
        lb1.delete(0, END)
        for row in db_funcs.view_books():
            lb1.insert(END, row)


def update():
    db_funcs.update_book(selected_tuple[0], title_text.get(),
                         author_text.get(), year_text.get(), isbn_text.get())
    view()


window = Tk()

window.wm_title("Book Store")

# labels
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

# entries
title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

# listbox
lb1 = Listbox(window, height=6, width=35)
lb1.grid(row=2, column=0, rowspan=6, columnspan=2)

# scroll bar
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

# apply scroll bar to listbox
lb1.configure(yscrollcommand=sb1.set)
sb1.configure(command=lb1.yview)

# bind function to event type
lb1.bind('<<ListboxSelect>>', get_selected_row)

# buttons
b1 = Button(window, text="View All", width=12, command=view)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search Entry", width=12, command=search)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Entry", width=12, command=add)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update Selected", width=12, command=update)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete Selected", width=12, command=delete)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()