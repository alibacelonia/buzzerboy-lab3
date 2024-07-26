import os

# Input words
converted_words = ["google-maps.png", "vector-maps.png"]

# Get a list of files in the current directory
files = [f for f in os.listdir('.') if os.path.isfile(f) and f != '.DS_Store']
files = sorted(files)


# Check if the number of words and files match
if len(converted_words) != len(files):
    print("The number of words and files do not match.")
else:
    # Rename files
    for old_name, new_name in zip(files, converted_words):
        os.rename(old_name, new_name)
        print(f"Renamed '{old_name}' to '{new_name}'")
