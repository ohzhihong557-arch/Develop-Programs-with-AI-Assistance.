def calculate_bill():
    # Prompt and validate Patient_type
    patient_type = input("Choose patient type (Subsidised/Private): ")
    while patient_type != "Subsidised" and patient_type != "Private":
        print("Invalid options please select either (Subsidised/Private)")
        patient_type = input("Choose patient type (Subsidised/Private): ")

    # Prompt and validate Num_labtests
    while True:
        num_input = input("Enter number of lab tests completed: ")
        if num_input.isdigit():  # Ensures input is a non-negative whole number
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
    print(f"Patient type : {patient_type}, Total amount to pay : ${total}")


# Run function standalone
if __name__ == "__main__":
    calculate_bill()
