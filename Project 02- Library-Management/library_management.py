
books = []


# Add Book
def add_book():
    book_id = int(input("Enter Book ID: "))
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "status": "Available"
    }

    books.append(book)
    print("Book added successfully!")


# Search Book
def search_book():
    book_id = int(input("Enter Book ID to search: "))

    for book in books:
        if book["id"] == book_id:
            print("\nBook Found!")
            print("Book ID:", book["id"])
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Status:", book["status"])
            return

    print("Book not found.")


# Issue Book
def issue_book():
    book_id = int(input("Enter Book ID to issue: "))

    for book in books:
        if book["id"] == book_id:

            if book["status"] == "Available":
                book["status"] = "Issued"
                print("Book issued successfully!")
            else:
                print("Book is already issued.")

            return

    print("Book not found.")


# Return Book
def return_book():
    book_id = int(input("Enter Book ID to return: "))

    for book in books:
        if book["id"] == book_id:

            if book["status"] == "Issued":
                book["status"] = "Available"
                print("Book returned successfully!")
            else:
                print("Book was not issued.")

            return

    print("Book not found.")


# Display Available Books
def display_available_books():
    found = False

    print("\n--- Available Books ---")

    for book in books:
        if book["status"] == "Available":
            print("Book ID:", book["id"])
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("----------------------")
            found = True

    if found == False:
        print("No books are currently available.")


# Save Records
def save_records():
    file = open("library.txt", "w")

    for book in books:
        file.write(
            str(book["id"]) + "," +
            book["title"] + "," +
            book["author"] + "," +
            book["status"] + "\n"
        )

    file.close()
    print("Library records saved successfully!")


# Main Program
while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Available Books")
    print("6. Save Records")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_book()

    elif choice == 2:
        search_book()

    elif choice == 3:
        issue_book()

    elif choice == 4:
        return_book()

    elif choice == 5:
        display_available_books()

    elif choice == 6:
        save_records()

    elif choice == 7:
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
