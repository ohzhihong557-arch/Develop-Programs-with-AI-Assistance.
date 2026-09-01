from datetime import datetime


def book_appointment():
    while True:
        # Step 1: Department Selection and Validation
        while True:
            department = input(
                "Select Department (GP / Specialist): "
            ).strip()

            if department.upper() in ["GP", "SPECIALIST"]:
                department = (
                    "GP" if department.upper() == "GP" else "Specialist"
                )
                break

            print(
                "Error: Invalid department. "
                "Please enter 'GP' or 'Specialist'.\n"
            )

        # Step 2: Date Input and Validation
        while True:
            current_date = datetime.now().date()

            date_str = input(
                "Enter preferred appointment date (YYYY-MM-DD): "
            ).strip()

            try:
                appointment_date = datetime.strptime(
                    date_str, "%Y-%m-%d"
                ).date()
            except ValueError:
                print(
                    "Error: Date is not correctly entered. "
                    "Please use YYYY-MM-DD format.\n"
                )
                continue

            days_diff = (appointment_date - current_date).days

            # Appointment must be within the next 7 days
            if days_diff <= 0:
                print(
                    "Error: Appointment date must be in the future.\n"
                )
            elif days_diff > 7:
                print(
                    f"Error: Appointment date must be within 7 days "
                    f"of today ({current_date}). Please re-enter.\n"
                )
            else:
                break

        # Step 3: Appointment Confirmation
        print("\n==============================")
        print("     APPOINTMENT DETAILS")
        print("==============================")
        print(f"Department:       {department}")
        print(
            f"Appointment Date: "
            f"{appointment_date.strftime('%A, %B %d, %Y')}"
        )
        print("==============================")

        while True:
            confirmation = input(
                "Confirm appointment? (Yes/No): "
            ).strip().lower()

            if confirmation == "yes":
                print("\n==============================")
                print("     APPOINTMENT BOOKED")
                print("==============================")
                print(f"Department:       {department}")
                print(
                    f"Appointment Date: "
                    f"{appointment_date.strftime('%A, %B %d, %Y')}"
                )
                print("Thank you for your service!")
                print("==============================")
                return

            elif confirmation == "no":
                print(
                    "\nAppointment cancelled. "
                    "Restarting booking process...\n"
                )
                break

            else:
                print(
                    "Error: Please enter Yes or No.\n"
                )


if __name__ == "__main__":
    book_appointment()
