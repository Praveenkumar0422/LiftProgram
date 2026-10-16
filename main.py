from liftoperation import operate_down_lift, operate_up_lift
def main():
    current_floor = 0
    min_floor = -1
    max_floor = 10
    while True:
       
        try:
            destination_floor = int(input(f"Enter the destination floor ({min_floor} to {max_floor}): "))
        except ValueError:
                    print("Invalid input. Please enter a valid floor number.")
                    continue
        if destination_floor < min_floor or destination_floor > max_floor:
            print(f"Invalid floor. Please enter a floor between {min_floor} and {max_floor}.")
            continue
        if destination_floor == current_floor:
            print(f"You are already on floor {current_floor}.")
            continue
        if destination_floor > current_floor:   
            current_floor = operate_up_lift(current_floor, destination_floor)
        else:
            current_floor = operate_down_lift(current_floor, destination_floor)
        ignore = input("Do you want to continue using the lift? (yes/no): ")
        if ignore.lower() != "yes" and ignore.lower() != "y":
            print("Thank you for using the lift.")
            break

if __name__ == "__main__":
    main()