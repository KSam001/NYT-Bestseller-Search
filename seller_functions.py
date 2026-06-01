def yearRange(books:list[dict]):
   beginning_year = int(input("Enter beginning year: "))
   ending_year = int(input("Enter ending year: "))


   for book in books:
      year = book.get("date").split("/")[2]

      if int(year) >= beginning_year and int(year) <= ending_year:
         print(f'{book.get("title")}, by {book.get("author")} ({book.get("date")})')

def monthYear(books):
   input_month = int(input("Enter month of year in number: "))
   input_year = int(input("Enter year: "))


   for book in books:
      date_part = book.get("date").split("/")
      
      month = int(date_part[0])
      year = int(date_part[2])

      if month == input_month and year == input_year:
         print(f'{book.get("title")}, by {book.get("author")} ({book.get("date")})')   


def searchbyAuthor(books):
   search_input = input("Enter author name: ")
   author_input = search_input.lower()

   for book in books:
      author_name = book.get("author")

      if author_input in author_name.lower():
         print(f'{book.get("title")}, by {author_name} ({book.get("date")})')


def searchbyTitle(books):
   title_input = input("Enter title: ")
   search_title = title_input.lower()

   for book in books:
      book_title = book.get("title")
      if search_title in book_title.lower():
         print(f'{book_title}, by {book.get("author")} ({book.get("date")})')
   



   






      





