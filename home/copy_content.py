import os

def copy_content_to_files(directory):
    # List all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    if not files:
        print("No files found in the directory.")
        return
    
    # Sort files to ensure consistent behavior for the 'first' file
    files.sort()
    
    # Get the path of the first file
    first_file_path = os.path.join(directory, files[0])
    
    try:
        # Read the content of the first file
        with open(first_file_path, 'r', encoding='utf-8') as first_file:
            content = first_file.read()
    except UnicodeDecodeError:
        print(f"Could not decode {files[0]} with UTF-8. Skipping content copy.")
        return
    except Exception as e:
        print(f"Error reading {files[0]}: {e}")
        return
    
    # Copy content to other files
    for file_name in files[1:]:
        file_path = os.path.join(directory, file_name)
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
        except Exception as e:
            print(f"Error writing to {file_name}: {e}")
    
    print(f"Content of {files[0]} has been copied to {', '.join(files[1:])}")

if __name__ == "__main__":
    # Get the current directory
    current_directory = os.getcwd()
    copy_content_to_files(current_directory)
