from datetime import datetime, timedelta

def book_appointment():
    # Calculate today's date and the minimum allowed date boundary (current date + 7 days)
    current_date = datetime.now().date()
    min_date = current_date + timedelta(days=7)
    
    # Step 1: Validate Department Input
    selected_department = ""
    while True:
        user_input = input("Select Department (GP / Specialist): ").strip()
        
        # Case-insensitive validation for flexibility
        if user_input.lower() in ["gp", "specialist"]:
            # Format nicely as 'GP' or 'Specialist'
            selected_department = "GP" if user_input.lower() == "gp" else "Specialist"
            break
        else:
            print("Error: Invalid department. Please enter 'GP' or 'Specialist'.\n")
            
    # Step 2: Validate Appointment Date
    appointment_date = None
    while True:
        date_input = input("Enter preferred appointment date (YYYY-MM-DD): ").strip()
        
        try:
            # Parse input string to a date object
            parsed_date = datetime.strptime(date_input, "%Y-%m-%d").date()
            
            # Condition check: Must be strictly MORE than 7 days from today
            if parsed_date > min_date:
                appointment_date = parsed_date
                break
            else:
                print(f"Error: Date must be more than 7 days from today (after {min_date.strftime('%Y-%m-%d')}).\n")
                
        except ValueError:
            print("Error: Invalid date format. Please use the format YYYY-MM-DD (e.g., 2026-09-15).\n")

    # Step 3: Confirmation Output
    print("\n" + "=" * 40)
    print("BOOKING CONFIRMED")
    print("=" * 40)
    print(f"Department:       {selected_department}")
    print(f"Appointment Date: {appointment_date.strftime('%A, %B %d, %Y')}")
    print("=" * 40)

# Run the function
if __name__ == "__main__":
    book_appointment()

