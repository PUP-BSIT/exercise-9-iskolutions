UNSET_OPTION = -1
EXIT_OPTION = 6

movie_records = [] 

def list_all_records():
    print("\n---MOVIE RECORDS---")

    if not movie_records:
        print("No records found.")
        return
    
    for record in movie_records:
        print(f"Title: {record['title']}")
        print(f"Year: {record['year']}")
        print(f"Genre: {record['genre']}")
        print(f"Rating: {record['rating']}")
        print(f"Director: {record['direct']}")
        print("--------------------")
        
    print("End of records.")

def add_record():
    movie_title = input("\nEnter movie title: ").strip()

    year_input = (input("Enter year released: ")).strip()
    if not year_input.isdigit():
        print("Invalid input")
        return
    release_year = int(year_input)

    genre = input("Enter movie genre: ").strip()
    if genre == "":
        print ("Invalid input")
        return
    
    rating = float(input("Enter movie rating: "))

    director = input("Enter movie director: ").strip()
    if director == "":
        print("Invalid input")

    movie_record = {
        "title": movie_title,
        "year": release_year,
        "genre": genre,
        "rating": rating,
        "direct": director,
    }

    movie_records.append(movie_record)
    print("\nMovie record added succesfully.\n")

def update_record():
    # TODO (Miko): implement updating record in this function.
    pass

def delete_record():
    # TODO (Hanz): implement deleting records in this function.
    pass

def search_record():
    # TODO (Kyle): implement record searching in this function.
    pass

def display_get_choice():
    print("---DATA RECORD MAIN MENU(MOVIES)---")
    print("1. List All")
    print("2. Add")
    print("3. Update")
    print("4. Delete")
    print("5. Search")
    print("6. Exit")

    return int(input("Enter your choice: "))

def process_choice(choice):
    match choice:
        case 1:
            list_all_records()
        case 2:
            add_record()
        case 3:
            update_record()
        case 4:
            delete_record()
        case 5:
            search_record()
        case 6:
            pass
        case _:
            print("Invalid choice. Please try again.")

def main():
    # TODO (everyone): Call your functions here
    choice = UNSET_OPTION
    while choice != EXIT_OPTION:
        choice = display_get_choice()
        process_choice(choice)
        
main()