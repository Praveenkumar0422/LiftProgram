def read_binary_file():
    try:
        with open('Ajithimages.jpg', 'rb') as file:
                binary_data = file.read()
        with open('Ajithimagescopy.jpg', 'wb') as file:
                file.write(binary_data)
                print("Binary file copied successfully.")

    except Exception as e:
            print(f"An error occurred: {e}")

read_binary_file()

