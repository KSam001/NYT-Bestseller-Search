def yearRange(books:list[dict]):
   beginning_year = int(input("Enter beginning year: "))
   ending_year = int(input("Enter ending year: "))

   for book in books:
      year = book.get("date").split("/")[2]

      if int(year) >= beginning_year and int(year) <= ending_year:
         print(f'{book.get("title")}, by {book.get("author")} ({book.get("date")})')

      





