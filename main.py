UNSET_OPTION = -1
EXIT_OPTION = 6

def list_all_records(movie_records):
    print("\n---MOVIE RECORDS---")

    if movie_records == []:
        print("No records found.")
        return
    
    for records in movie_records:
        for key, value in records.items():
            print(f"{key}: {value}")
        
    print("End of records.")

def add_record(movie_records):
    input_list = ["title", "genre", "year", "rating", "director"]
    movie_record = {}

    print("\n---ADD MOVIE RECORD---")

    for record in input_list:
        movie_record[record] = input(f"Enter {record}: ")

    if is_valid_record(movie_record):
        movie_record["year"] = int(movie_record["year"])
        movie_record["rating"] = int(movie_record["rating"])    
        movie_records.append(movie_record)
        print("\nMovie record added successfully.")
    

def is_valid_record(movie_record):
    if not movie_record["year"].isdigit():
        print("Year must be numeric! Aborting process.")
        return False

    try:
        movie_record["rating"] = float(movie_record["rating"])
    except ValueError:
        print("Ratings must be numeric! Aborting process.")
        return False
    
    return True

def update_record():
    # TODO (Miko): implement updating record in this function.
    pass

def delete_record(movie_records):
    
    print("\n---DELETE MOVIE RECORD---")

    if not movie_records:
        print("No records to delete.")
        return

    title_to_delete = input("Enter the title of the movie to delete: ")

    for record in movie_records:
        if record["title"].lower() == title_to_delete.lower():
            movie_records.remove(record)
            print(f"Movie '{title_to_delete}' has been deleted.")
            return

    print(f"No movie found with the title '{title_to_delete}'.")

def search_record():
    # TODO (Kyle): implement record searching in this function.
    pass

def display_get_choice():
    print("\n---DATA RECORD MAIN MENU(MOVIES)---")
    print("1. List All")
    print("2. Add")
    print("3. Update")
    print("4. Delete")
    print("5. Search")
    print("6. Exit")

    return int(input("Enter your choice: "))

def process_choice(choice, movie_records):
    match choice:
        case 1:
            list_all_records(movie_records)
        case 2:
            add_record(movie_records)
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
    movie_records = []
    choice = UNSET_OPTION
    while choice != EXIT_OPTION:
        choice = display_get_choice()
        process_choice(choice, movie_records)
        
main()