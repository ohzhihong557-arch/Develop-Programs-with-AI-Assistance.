def register_patient():
    """
    Registers a new patient by validating name, age, and ID inputs.
    """
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
                # Convert whole floats (e.g., 25.0) to integers for clean display
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


if __name__ == "__main__":
    register_patient()
