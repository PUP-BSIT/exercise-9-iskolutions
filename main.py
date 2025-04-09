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
    input_list = ["title", "genre", "year", "rating", "direct"]
    movie_record = {}

    print("\n---ADD MOVIE RECORD---")

    for record in input_list:
        user_input = input(f"Enter {record}: ")

        if record == "year":
            if not user_input.isdigit():
                print(f"{user_input} must be an integer")
                return
                
            movie_record[record] = int(user_input)

        elif record == "rating":
            try:
                movie_record[record] = float(user_input)
            except ValueError:
                print(f"{user_input} must be a float number")
                return
            
        else: 
            movie_record[record] = user_input

    movie_records.append(movie_record)
    print("\nMovie record added successfully.")

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