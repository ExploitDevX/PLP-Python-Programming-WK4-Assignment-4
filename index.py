def modify_file(input_file, output_file):
    with open(input_file, 'r') as f:
        content = f.read()
    
    modified = content.upper()
    
    with open(output_file, 'w') as f:
        f.write(modified)

modify_file('input.txt', 'output.txt')


def read_file():
    filename = input("Enter filename: ")
    try:
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission denied")
    except Exception as e:
        print(f"Error: {e}")

read_file()
