# CarFinder Program - AutoCountry

AllowedVehiclesList = [
    'Ford F-150',
    'Chevrolet Silverado',
    'Tesla CyberTruck',
    'Toyota Tundra',
    'Nissan Titan'
]

def show_banner():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.2")
    print("********************************")

def show_menu():
    print("Please Enter the following number below from the following menu:\n")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. Exit")

def print_allowed_vehicles():
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in AllowedVehiclesList:
        print(vehicle)

def search_vehicle():
    print("********************************")
    vehicle = input("Please Enter the full Vehicle name:\n").strip()
    if vehicle in AllowedVehiclesList:
        print(f"\n{vehicle} is an authorized vehicle")
    else:
        print(f"\n{vehicle} is not an authorized vehicle, if you received this in error please check the spelling and try again")

def main():
    while True:
        show_banner()
        show_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            print_allowed_vehicles()
        elif choice == '2':
            search_vehicle()
        elif choice == '3':
            print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
            input("\nPress Enter to close the program...")
            break
        else:
            print("\nInvalid option. Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    main()
