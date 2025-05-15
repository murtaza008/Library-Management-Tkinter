# gui_app_tkinter.py
# Murtaza Mazhar 
# F2022065163
import tkinter as tk
from tkinter import messagebox, simpledialog
from book_library import Book, EBook, Library, BookNotAvailableError

library = Library()
root = tk.Tk()
root.title("Library Management System (Tkinter)")
root.geometry("600x600")

def toggle_size_entry():
    if ebook_var.get():
        size_entry.config(state="normal")
    else:
        size_entry.delete(0, tk.END)
        size_entry.config(state="disabled")

def add_book():
    title = title_entry.get()
    author = author_entry.get()
    isbn = isbn_entry.get()
    is_ebook = ebook_var.get()
    size = size_entry.get()

    if not title or not author or not isbn:
        messagebox.showerror("Error", "Title, Author, and ISBN are required.")
        return

    if is_ebook:
        try:
            size = float(size)
            book = EBook(title, author, isbn, size)
        except ValueError:
            messagebox.showerror("Error", "Download size must be a number.")
            return
    else:
        book = Book(title, author, isbn)

    library.add_book(book)
    messagebox.showinfo("Success", f"Book '{title}' added.")
    update_book_list()

def lend_book():
    isbn = simpledialog.askstring("Lend Book", "Enter ISBN:")
    if isbn:
        try:
            library.lend_book(isbn)
            messagebox.showinfo("Success", "Book lent.")
        except BookNotAvailableError as e:
            messagebox.showerror("Error", str(e))
    update_book_list()

def return_book():
    isbn = simpledialog.askstring("Return Book", "Enter ISBN:")
    if isbn:
        try:
            library.return_book(isbn)
            messagebox.showinfo("Success", "Book returned.")
        except BookNotAvailableError as e:
            messagebox.showerror("Error", str(e))
    update_book_list()

def remove_book():
    isbn = simpledialog.askstring("Remove Book", "Enter ISBN:")
    if isbn:
        library.remove_book(isbn)
        messagebox.showinfo("Removed", "Book removed.")
    update_book_list()

def view_books_by_author():
    author = simpledialog.askstring("Author", "Enter author's name:")
    if author:
        books = list(library.books_by_author(author))
        listbox.delete(0, tk.END)
        if books:
            listbox.insert(tk.END, f"Books by {author}:")
            for book in books:
                listbox.insert(tk.END, str(book))
        else:
            listbox.insert(tk.END, "No books found.")

def update_book_list():
    listbox.delete(0, tk.END)
    listbox.insert(tk.END, "Available Books:")
    for book in library:
        listbox.insert(tk.END, str(book))

tk.Label(root, text="Title:").pack()
title_entry = tk.Entry(root)
title_entry.pack()

tk.Label(root, text="Author:").pack()
author_entry = tk.Entry(root)
author_entry.pack()

tk.Label(root, text="ISBN:").pack()
isbn_entry = tk.Entry(root)
isbn_entry.pack()

ebook_var = tk.BooleanVar()
tk.Checkbutton(root, text="eBook?", variable=ebook_var, command=toggle_size_entry).pack()

tk.Label(root, text="Download Size (MB):").pack()
size_entry = tk.Entry(root)
size_entry.pack()
size_entry.config(state="disabled")

tk.Button(root, text="Add Book", command=add_book).pack(pady=5)
tk.Button(root, text="Lend Book", command=lend_book).pack(pady=5)
tk.Button(root, text="Return Book", command=return_book).pack(pady=5)
tk.Button(root, text="Remove Book", command=remove_book).pack(pady=5)
tk.Button(root, text="Books by Author", command=view_books_by_author).pack(pady=5)

tk.Label(root, text="Library Inventory:").pack()
listbox = tk.Listbox(root, width=70)
listbox.pack(pady=10)

update_book_list()
root.mainloop()
