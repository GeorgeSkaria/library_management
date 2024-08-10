# Library Management System

This is a simple Library Management System implemented in Python. It allows the user to register members, add and search for books, check out books, return books, and incur fines for late returns.

## Features

- **Member Registration:** Members can register and cancel their membership.
- **Book Management:** Books can be added to the library, searched, and checked out.
- **Book Checkout and Return:** Members can check out and return books. Fines are automatically calculated for late returns.
- **Fine Calculation:** A fine of Rs. 20 is incurred for each day after 15 days of borrowing a book.

## Installation

1. **Clone the repository** (if you have already pushed it to GitHub):

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
2. **Navigate to the project directory**:
   ```bash
   cd your-repo-name

## Usage
Choose an option from the menu:

Register Membership
Cancel Membership
Search and Retrieve Book
Checkout Book
Return Book
Quit
Follow the prompts to perform the desired action.

Fine Calculation: If a book is returned after 15 days from the checkout date, a fine of Rs. 20 per day will be calculated and displayed.

## Code Overview
Librarian Class: Manages library operations including book management, member registration, and fine calculation.
Book Class: Represents a book in the library, including its borrow status and borrower details.
Member Class: Represents a library member, including their checked-out books and reserved books.
