# BookVault - Console-Based Book Management System

## Introduction

BookVault is a simple, console-based application developed using Python and Object-Oriented Programming (OOP) principles. It provides basic functionalities for managing a collection of books, allowing users to add, view, search, and remove books directly from their terminal. This project serves as a practical example of applying OOP concepts to build a functional command-line interface (CLI) application.

## Features

* **Add Book:** Add new book entries with details like title, author, and ISBN.
* **View All Books:** Display a list of all books currently in the vault.
* **Search Book:** Search for books by title, author, or ISBN.
* **Update Book:** Modify the details of an existing book.
* **Delete Book:** Remove a book from the collection.
* **Persistent Storage (Assumed):** If you're saving data to a file (e.g., CSV, JSON, or a simple text file), mention this here. Otherwise, state that data is temporary for the session.
* **User-Friendly Console Interface:** Navigate and interact with the system through simple menu-driven commands.

## Technologies Used

* **Python 3:** The core programming language.
* **Object-Oriented Programming (OOP):** The project leverages classes and objects (e.g., `Book` class, `BookManager` class) to structure the code logically and promote reusability.

## Getting Started

### Prerequisites

* Python 3.x installed on your system.

### Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/shojibruhan/BookVault.git](https://github.com/shojibruhan/BookVault.git)
    cd BookVault
    ```

### Running the Program

Navigate into the cloned directory and run the main Python script:

```bash
python main.py
````

## How to Use

Once you run `python main.py`, the program will present you with a main menu in your console. You can interact with it by typing the number corresponding to your desired action and pressing Enter.

Example interaction:

```
Welcome to BookVault!
---------------------
1. Add a new book
2. View all books
3. Search for a book
4. Update a book
5. Delete a book
6. Exit
---------------------
Enter your choice:
```

Follow the on-screen prompts to perform operations.

## Project Structure (Assumed)

The project is typically structured with different responsibilities delegated to distinct files/classes:

```
BookVault/
├── main.py             # Entry point of the application, handles the main menu loop.
├── book.py             # Defines the 'Book' class (Book object structure).
├── book_manager.py     # Manages operations on books (add, delete, search, update).
├── data_handler.py     # (Optional) Handles reading/writing book data to a file.
├── .gitignore
└── README.md
```

*(Adjust the file names above to match your actual project structure if they differ, e.g., `book.py` might be part of `book_manager.py` if it's a single file.)*

## Contributing

Contributions are welcome\! If you have suggestions for improvements or new features, feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add new feature X'`).
5.  Push to the branch (`git push origin feature/your-feature`).
6.  Create a Pull Request.


