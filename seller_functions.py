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

   match_found = False
   # why do you need the match_found flag? What's its role?
   for book in books:
      date_part = book.get("date").split("/")
      
      month = int(date_part[0])
      year = int(date_part[2])

      if month == input_month and year == input_year:
         print(f'{book.get("title")}, by {book.get("author")} ({book.get("date")})')
         match_found = True

# Overall, the implementation is on point.



   






      





