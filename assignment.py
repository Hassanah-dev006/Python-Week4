def read_and_modify_file():
    """
    Reads a file and writes a modified version to a new file.
    Handles errors if the file does not exist or can't be read.
    """
    try:
        # Ask the user for the filename
        input_filename = input("Enter the name of the file to read: ")

        # Try to open and read the file
        with open(input_filename, 'r') as file:
            content = file.read()

        # Modify the content (example: convert text to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new file
        output_filename = "modified_" + input_filename
        with open(output_filename, 'w') as file:
            file.write(modified_content)

        print(f"The modified content has been written to {output_filename}.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' could not be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    read_and_modify_file()
