from datetime import datetime


def book_appointment():
    # Step 1: Department Selection and Validation
    while True:
        department = input("Select Department (GP / Specialist): ").strip()
        if department.upper() in ["GP", "SPECIALIST"]:
            department = (
                "GP" if department.upper() == "GP" else "Specialist"
            )
            break
        print("Error: Invalid department. Please enter 'GP' or 'Specialist'.\n")

    # Step 2: Date Input and Validation
    while True:
        current_date = datetime.now().date()
        date_str = input(
            "Enter preferred appointment date (YYYY-MM-DD): "
        ).strip()

        try:
            appointment_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Error: Invalid date format. Please use YYYY-MM-DD.\n")
            continue

        days_diff = (appointment_date - current_date).days

        # Reject past dates and dates beyond 7 days from today
        if days_diff <= 0:
            print("Error: Appointment date must be in the future.\n")
        elif days_diff > 7:
            print(
                f"Error: Appointment date must be within 7 days of today ({current_date}). Please re-enter.\n"
            )
        else:
            break

    # Step 3: Confirmation
    print("\n==============================")
    print("   BOOKING CONFIRMED")
    print("==============================")
    print(f"Department:       {department}")
    print(f"Appointment Date: {appointment_date.strftime('%A, %B %d, %Y')}")
    print("==============================")


if __name__ == "__main__":
    book_appointment()
