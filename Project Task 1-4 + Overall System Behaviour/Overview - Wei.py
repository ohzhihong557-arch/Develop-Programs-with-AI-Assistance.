BASE_CONSULTATION_FEE = 100
LAB_TEST_RATE = 10

def register_patient():
    """ Registers a new patient by validating name, age, and ID inputs. """
    # 1. Validate Patient Name (Non-blank string check)
    while True:
        name = input("Enter patient name: ").strip()
        if name:
            break
        print("Error: Name cannot be blank. Please re-input your name.")

    # 2. Validate Patient Age (Positive numeric check)
    while True:
        try:
            age = float(input("Enter patient age: "))
            if age > 0:
                if age.is_integer():
                    age = int(age)
                break
            print("Error: Age must be a positive number. Please re-input your age.")
        except ValueError:
            print("Error: Invalid input! Age must be a valid positive number.")

    # 3. Validate Patient ID (Non-blank string check)
    while True:
        patient_id = input("Enter patient ID: ").strip()
        if patient_id:
            break
        print("Error: Patient ID cannot be blank. Please re-enter an ID.")

    # 4. Display Patient Information
    print("\nPatient Information:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Patient ID: {patient_id}")
    print("\nPatient registered successfully.")

def book_appointment():
    # Calculate today's date and the maximum allowed date
    current_date = datetime.now().date()
    max_date = current_date + timedelta(days=7)

    # Step 1: Validate Department Input
    selected_department = ""

    while True:
        user_input = input("Select Department (GP / Specialist): ").strip()

        if user_input.lower() in ["gp", "specialist"]:
            selected_department = (
                "GP" if user_input.lower() == "gp" else "Specialist"
            )
            break
        else:
            print("Error: Invalid department. Please enter 'GP' or 'Specialist'.\n")

    # Step 2: Validate Appointment Date
    appointment_date = None

    while True:
        date_input = input(
            "Enter preferred appointment date (YYYY-MM-DD): "
        ).strip()

        try:
            parsed_date = datetime.strptime(
                date_input, "%Y-%m-%d"
            ).date()

            # Appointment must be today or within the next 7 days
            if current_date <= parsed_date <= max_date:
                appointment_date = parsed_date
                break
            else:
                print(
                    f"Error: Appointment date must be within 7 days "
                    f"of today ({current_date}). Please re-enter.\n"
                )

        except ValueError:
            print(
                "Error: Invalid date format. "
                "Please use YYYY-MM-DD (e.g., 2026-08-30).\n"
            )

    # Step 3: Confirmation Output
    print("\n" + "=" * 40)
    print("BOOKING CONFIRMED")
    print("=" * 40)
    print(f"Department: {selected_department}")
    print(
        f"Appointment Date: "
        f"{appointment_date.strftime('%A, %B %d, %Y')}"
    )
    print("=" * 40)

def calculate_bill():
    # Prompt and validate Patient_type
    patient_type = input("Choose patient type (Subsidised/Private): ")
    while patient_type != "Subsidised" and patient_type != "Private":
        print("Invalid options please select either (Subsidised/Private)")
        patient_type = input("Choose patient type (Subsidised/Private): ")

    # Prompt and validate Num_labtests
    while True:
        num_input = input("Enter number of lab tests completed: ")
        if num_input.isdigit():  
            num_labtests = int(num_input)
            break
        print("Invalid number please enter a whole number")

    # Calculate Subtotal using base fee and lab rate constants
    subtotal = BASE_CONSULTATION_FEE + (num_labtests * LAB_TEST_RATE)

    # Calculate final Total based on Patient_type discount
    if patient_type == "Subsidised":
        total = subtotal * 0.7
    else:
        total = subtotal

    # Display final patient bill
    print(f"Patient type : {patient_type}, Total amount to pay : ${total:.2f}")

def process_patient_triage() -> None:
    while True:
        raw_input = input("Enter condition severity (1-10): ").strip()
        if raw_input.isdigit():
            severity = int(raw_input)
            if 1 <= severity <= 10:
                break
        print("Error: Invalid input. Please enter a whole number from 1 to 10.\n")

    if severity <= 4:
        room = "Waiting Room"
    elif severity <= 7:
        room = "Room 1"
    else:
        room = "Room 2"

    print("\n=== TRIAGE SUMMARY ===")
    print(f"Severity Level : {severity}")
    print(f"Assigned Room  : {room}")

def main_menu():
    """ Displays the main menu and handles user navigation. """
    while True:
        print("\n" + "=" * 40)
        print("CareBridge Hospital Management System")
        print("=" * 40)
        print("1. Register Patient")
        print("2. Book Appointment")
        print("3. Calculate Bill")
        print("4. Assign Triage Room")
        print("5. Exit")
        print("=" * 40)
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            print("\n--- Register Patient ---")
            register_patient()
        elif choice == '2':
            print("\n--- Book Appointment ---")
            book_appointment()
        elif choice == '3':
            print("\n--- Calculate Bill ---")
            calculate_bill()
        elif choice == '4':
            print("\n--- Assign Triage Room ---")
            process_patient_triage()
        elif choice == '5':
            print("\nExiting CareBridge Hospital Management System. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 5.")

# Run the integrated program
if __name__ == "__main__":
    main_menu()


