import seller_functions
with open("files/bestsellers.txt", "r") as best_seller:
    file = best_seller.readlines()

#title, author, publisher, date, category   

books = []

for i in file:
    str_list = i.split("\t")
    title = str_list[0]
    author = str_list[1]
    publisher = str_list[2]
    date = str_list[3]
    category = str_list[4]

    book = {"title": title, 
            "author": author,
            "publisher": publisher,
            "date": date,
            "category": category.replace("\n", "")}
    books.append(book)

tries = 3
valid_inputs = ["1","2","3","4","Q"]

while tries >= 1:
    user_input = input("""
What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit
>
    """
    )

    if user_input not in valid_inputs:
        print(f"Valid inputs are {valid_inputs}")
        tries -= 1
    else:
        if user_input == "1":
            seller_functions.yearRange(books)

if tries <= 1:
    print("Number of tries exhausted")










