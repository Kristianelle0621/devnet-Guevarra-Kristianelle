print("Midterm Practical Exam — Pet Adoption Records Manager Student: Kristianelle")

pets = []
        
def display_menu():
    pass

def add_pet():
    pass 

def view_pets():
    pass

def count_available_adopted():
    pass

def find_pet():
    pass


def main():
    running = True
    while running:
        print("1. Add a Pet")
        print("2. View all Pet list")
        print("3. Count available vs adopted")
        print("4. Find a pet by name") 
        print("5. Exit")
        choice = input("Select (1/2/3/4/5): ")
       
        if choice == "1":
            print("1")
        elif choice == "2":
            print("2")
        elif choice == "3":
            print("3")
        elif choice == "4":
            print("4")
        elif choice == "5":
            running = False
        else:
            print("Invalid choice")   
main()