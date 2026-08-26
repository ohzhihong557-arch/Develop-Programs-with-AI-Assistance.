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

# Call the function so it runs when you execute the script
process_patient_triage()
