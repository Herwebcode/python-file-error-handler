def modify_content(text):
    """Modify the content by converting it to uppercase."""
    return text.upper()


def handle_file_operations():
    try:
        filename = input("Enter the name of the file to read: ")

        # Attempt to open and read the input file
        with open(filename, 'r') as file:
            content = file.read()

        # Modify the content
        modified_content = modify_content(content)

        # Define the output filename
        output_filename = "modified_" + filename

        # Write the modified content to a new file
        with open(output_filename, 'w') as file:
            file.write(modified_content)

        print(f"Success! Modified content saved to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

    except IOError:
        print("Error: An I/O error occurred while handling the file.")


# Run the main function
handle_file_operations()
