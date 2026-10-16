def operate_up_lift(current_floor, destination_floor):
    print(f"Going up from floor {current_floor} to floor {destination_floor}.")
    for floor in range(current_floor + 1, destination_floor + 1):
        print(f"Passing floor {floor}.")
    print(f"Thank you for using the lift. You have arrived at floor {destination_floor}.")
    current_floor = destination_floor
    return current_floor

def operate_down_lift(current_floor, destination_floor):
    print(f"Going down from floor {current_floor} to floor {destination_floor}.")
    for floor in range(current_floor - 1, destination_floor - 1, -1):
        print(f"Passing floor {floor}.")
    print(f"Thank you for using the lift. You have arrived at floor {destination_floor}.")
    current_floor = destination_floor
    return current_floor 