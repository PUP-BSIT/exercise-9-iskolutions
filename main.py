import os

UNSET_OPTION = -1
EXIT_OPTION = 6

def list_all_records(movie_records):
    os.system("cls")
    print("\n---MOVIE RECORDS---")

    if movie_records == []:
        print("No records found.")
        return
    
    count = 1
    for records in movie_records:
        print(f"\nMovie #{count}:")
        count += 1
        for key, value in records.items():
            print(f"{key}:   \t{value}")
        
    print("\nEnd of records.")

def add_record(movie_records):
    os.system("cls")
    input_list = ["title", "genre", "year", "rating", "director"]
    movie_record = {}

    print("\n---ADD MOVIE RECORD---")

    for record in input_list:
        movie_record[record] = input(f"Enter {record}: ")

    if is_valid_record(movie_record):
        movie_record["year"] = int(movie_record["year"])
        movie_record["rating"] = float(movie_record["rating"])    
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

def update_record(movie_records):
    os.system("cls")
    list_all_records(movie_records)
    
    record_num = int(input("Enter a record to update: "))
    record = movie_records[record_num - 1] # for zero indexing
    
    for field in record:
        record[field] = input(f"Enter {field}: ")
    
    if is_valid_record(record):
        record["year"] = int(record["year"])
        record["rating"] = float(record["rating"]) 
        movie_records[record_num - 1] = record # Change old record to new one
        print("\nRecord updated successfully")
        return
    
    print("\nUpdating record failed.")
    
def delete_record(movie_records):
    os.system("cls")
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

def get_search_field():
    os.system("cls")
    search_fields = {
        "1": "title",
        "2": "genre",
        "3": "year",
        "4": "rating",
        "5": "director"
    }

    field_choice = UNSET_OPTION

    while field_choice not in search_fields:
        for key, value in search_fields.items():
            print(f"{key}. {value}")

        field_choice = input("Enter the number you want to search: ")

        if field_choice not in search_fields:
            print("\nInvalid choice")
    
    return field_choice, search_fields

def search_record(movie_records):
    os.system("cls")
    print("\n---SEARCH MOVIE RECORD---")

    field_choice, search_fields = get_search_field()
    
    search_field = search_fields[field_choice]
    search_value = input(f"Enter the {search_field}: ").lower()

    print("\nMovies Found")
    is_found = False
    
    for record in movie_records:
        if search_value == str(record[search_field]).lower():
            print("\n---Movie Found---")
            for key, value in record.items():
                print(f"{key}: {value}")
            
            is_found = True
    
    if not is_found:
        print(f"\nNo movies found with the {search_field}: {search_value}")

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
            update_record(movie_records)
        case 4:
            delete_record(movie_records)
        case 5:
            search_record(movie_records)
        case 6:
            os.system("cls")
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