# CarFinder Program - AutoCountry

FILENAME = "authorized_vehicles.txt"

def read_vehicles():
    try:
        with open(FILENAME, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def write_vehicles(vehicle_list):
    with open(FILENAME, 'w') as file:
        for vehicle in vehicle_list:
            file.write(vehicle + '\n')

def print_banner():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.5")
    print("********************************")

def show_menu():
    print("Please Enter the following number below from the following menu:\n")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")

def print_vehicles():
    vehicles = read_vehicles()
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in vehicles:
        print(vehicle)

def search_vehicles():
    print("********************************")
    search_vehicle = input("Please Enter the full Vehicle name:\n").strip()
    vehicles = read_vehicles()

    if search_vehicle in vehicles:
        print(f"\n{search_vehicle} is an authorized vehicle")
    else:
        print(f"\n{search_vehicle} is not an authorized vehicle, if you received this in error please check the spelling and try again")

def add_vehicle():
    print("********************************")
    new_vehicle = input("Please Enter the full Vehicle name you would like to add:\n").strip()
    vehicles = read_vehicles()

    vehicles.append(new_vehicle)
    write_vehicles(vehicles)
    print(f'\nYou have added "{new_vehicle}" as an authorized vehicle')

def delete_vehicle():
    print("********************************")
    vehicle_to_remove = input("Please Enter the full Vehicle name you would like to REMOVE:\n").strip()
    vehicles = read_vehicles()

    if vehicle_to_remove in vehicles:
        confirm = input(f'Are you sure you want to remove "{vehicle_to_remove}" from the Authorized Vehicles List?\n').strip().lower()
        if confirm == 'yes':
            vehicles.remove(vehicle_to_remove)
            write_vehicles(vehicles)
            print(f'\nYou have REMOVED "{vehicle_to_remove}" as an authorized vehicle')
        else:
            print("")
    else:
        print(f'\n"{vehicle_to_remove}" is not currently in the Authorized Vehicles List.')

def main():
    while True:
        print_banner()
        show_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            print_vehicles()
        elif choice == '2':
            search_vehicles()
        elif choice == '3':
            add_vehicle()
        elif choice == '4':
            delete_vehicle()
        elif choice == '5':
            print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
            input("\nPress Enter to close the program...")
            break
        else:
            print("\nInvalid option. Please enter a number from 1 to 5.\n")

if __name__ == "__main__":
    main()
