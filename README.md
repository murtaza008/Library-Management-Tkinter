# Library-Management-Tkinter

A simple desktop Library Management System built with Python and Tkinter. This intuitive GUI application allows you to manage both physical books and eBooks by adding, lending, returning, removing, and searching by author.

---

## 🔍 Features

- ✅ Add physical books and eBooks (with download size)
- ✅ Lend and return books with availability checks
- ✅ Remove books by ISBN
- ✅ Search books by author
- ✅ View live inventory of available books
- ✅ Visual GUI for all interactions
- ✅ Custom exception handling for lending logic

---

## 🛠 Technologies Used

- **Python 3.x**
- **Tkinter** – For the desktop GUI
- **Custom OOP Classes & Exceptions** – Book, EBook, Library, BookNotAvailableError

---

## 📁 Project Structure

```
Library-Management-Tkinter/
├── book_library.py # Core classes and custom exceptions
├── gui_app.py # Tkinter GUI frontend
└── README.md # Project documentation
```

---

## ⚙️ Setup Instructions

## 🔒 Create Virtual Environment:

```bash
python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

This project uses only standard Python libraries (Tkinter), so no external packages are required.

---

## 🚀 Usage
To run the GUI application:

```bash
python gui_app.py
```
