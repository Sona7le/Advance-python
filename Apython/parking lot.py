import time

class ParkingLot:
    def __init__(self, total_spots):
        self.total_spots = total_spots
        self.available_spots = total_spots
        self.parked_vehicles = {}   # vehicle_number : entry_time

    # Vehicle Entry
    def vehicle_entry(self, vehicle_number):
        if self.available_spots > 0:
            entry_time = time.time()
            self.parked_vehicles[vehicle_number] = entry_time
            self.available_spots -= 1
            print(f"Vehicle {vehicle_number} parked successfully.")
            print(f"Available spots: {self.available_spots}")
        else:
            print("Parking Full! No spots available.")

    # Vehicle Exit
    def vehicle_exit(self, vehicle_number):
        if vehicle_number in self.parked_vehicles:
            exit_time = time.time()
            entry_time = self.parked_vehicles.pop(vehicle_number)
            self.available_spots += 1

            # Calculate parking duration in hours
            duration = (exit_time - entry_time) / 3600
            fee = self.calculate_fee(duration)

            print(f"Vehicle {vehicle_number} exited.")
            print(f"Parking Duration: {round(duration, 2)} hours")
            print(f"Parking Fee: ₹{round(fee, 2)}")
            print(f"Available spots: {self.available_spots}")
        else:
            print("Vehicle not found in parking lot.")

    # Fee Calculation (₹20 per hour)
    def calculate_fee(self, hours):
        rate_per_hour = 20
        return hours * rate_per_hour


# Main Program
parking = ParkingLot(5)   # Total 5 parking spots

while True:
    print("\n1. Vehicle Entry")
    print("2. Vehicle Exit")
    print("3. Check Available Spots")
    print("4. Exit Program")

    choice = input("Enter your choice: ")

    if choice == '1':
        vehicle_no = input("Enter Vehicle Number: ")
        parking.vehicle_entry(vehicle_no)

    elif choice == '2':
        vehicle_no = input("Enter Vehicle Number: ")
        parking.vehicle_exit(vehicle_no)

    elif choice == '3':
        print(f"Available spots: {parking.available_spots}")

    elif choice == '4':
        print("Thank you! Exiting system.")
        break

    else:
        print("Invalid choice. Try again.")
