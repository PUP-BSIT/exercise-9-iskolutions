UNSET_OPTION = -1
EXIT_OPTION = 6
def list_all_records():
    # TODO (Pearl): implement listing all records in this funciton.
    pass

def add_record():
    # TODO (Jakim): implement adding records in this function.
    pass

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