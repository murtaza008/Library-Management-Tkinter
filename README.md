# Library-Management-Tkinter

A simple desktop Library Management System built with Python and Tkinter. Manage physical books and eBooks by adding, lending, returning, removing, and searching by author through an intuitive GUI.

## Features

- Add physical books and eBooks (with download size)
- Lend and return books with availability checks
- Remove books by ISBN
- Search books by author
- View live inventory of available books

## Technologies

- Python 3.x
- Tkinter for GUI
- Custom exception handling for lending logic

## Project Structure

Library-Management-Tkinter/
├── book_library.py # Core classes and exceptions
├── gui_app.py # Tkinter GUI frontend
└── README.md # Project documentation

## Setup

It is recommended to create a Python virtual environment before running the app:

```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

This project uses only Python’s standard libraries (Tkinter), so no additional packages are needed.

## Usage

Run the GUI application:

```bash
python gui_app.py
```

## Future Enhancements

- Persistent data storage (file or database)
- User authentication and lending history
- Advanced search and filtering
- Support for multiple copies per book
