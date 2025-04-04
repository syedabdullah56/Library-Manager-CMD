from collections import Counter, defaultdict


library = [
    {"title": "Think And Grow Rich", "author": "Napolean Hill", "year": 1937, "genre": "Self Growth", "read": True}
]



def add_books():
    print("=======Add a Book😎=======")
    title = input("Enter the title: ")
    author = input("Enter the author name: ")
    try:
        year = int(input("Enter the year of publication: "))    
    except ValueError:
        print("Settling Year To 0!")
        year = 0

    genre = input("Enter the genre of the book: ")
    
    read = False 
    try:
        ch = int(input("Have you read it?\n Enter the option:\n1.Read \n2.Not Read\n"))
        if ch == 1:
            read = True
        elif ch == 2:
            read = False
        else:
            print("Invalid Choice! Setting read status to 'Not Read'.")
    except ValueError:
        print("Invalid Input! Setting read status to 'Not Read'.")

    # Setting new book
    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }

    # Adding the book to the library
    library.append(new_book)
    print(f"{title} added successfully to Library!😊")
    

def remove_books():
    print("======Remove Book😎========")
    if len(library) == 0:
        print("Library is empty! No books to remove.")
        return
    
    title_to_remove = input("Enter the title of the book to remove🤔: ").strip().lower()
    found = False
    
    for book in library:
        if book["title"].lower() == title_to_remove:
            library.remove(book)
            print(f"'{book['title']}' has been successfully removed from the library!😊")
            found = True
            break
    
    if not found:
        print("Book not found! Please try again.")


def search_books():
    print("======Search Books📚========")
    if len(library) == 0:
        print("Library is empty! No books to search.")
        return
    
    
    print("Search By:\n1. Title\n2. Author\n3. Year\n4. Genre")

    try:
        search_option=int(input("Enter Your Choice:"))
    
    except ValueError:
        print("Invalid Input! Please enter a valid number.")
        return
    search_query = input("Enter your search query: ").strip().lower()
    found_books = []

    for book in library:
        if (search_option==1 and search_query in book["title"].lower()) or \
        (search_option == 2 and search_query in book["author"].lower()) or \
        (search_option == 3 and search_query == str(book["year"])) or \
        (search_option == 4 and search_query in book["genre"].lower()):
            found_books.append(book)
    
    if found_books:
        print(f"\n📚 Found {len(found_books)} book(s):")
        for book in found_books:
            print(f"📖 Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Read: {'Yes' if book['read'] else 'No'}")
    else:
        print("No books found matching your query.")

        



def show_stats():
    print("\n======📊 Library Statistics📊======\n")
    
    if not library:
        print("Library is empty! Add some books first.")
        return

    # 1. Total number of books
    total_books = len(library)
    print(f"📚 Total number of books: {total_books}")

     # 2. Books read and not read
    read_books = sum(1 for book in library if book['read'])
    unread_books = total_books - read_books
    print(f"📖 Books read: {read_books}")
    print(f"📖 Books not read: {unread_books}")

    # 4. Genres available
    genres = [book['genre'] for book in library if book['genre']]
    genre_count = Counter(genres)
    
    if genre_count:
        print("\n📑 Genres available:")
        for genre, count in genre_count.items():
            print(f"  {genre}: {count} book(s)")

    print("\n======📊 End of Statistics📊======\n")

def show_all_books():
    print(library)


while True:
    try:
        choice = int(input("\nEnter the option Number:\n1.Add book \n2.Remove Book \n3.Search Book \n4.Show Statistics \n5.Show All Books \n6.Quit\n"))
        
        if choice == 1:
            add_books()
        elif choice == 2:
            remove_books()
        elif choice == 3:
            search_books()
        elif choice == 4:
            show_stats()
        elif choice == 5:
            show_all_books()
        elif choice == 6:
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid Choice! Please Enter a number between 1 and 5.")
            
    except ValueError:
        print("Invalid Input! Please enter a valid number.")
