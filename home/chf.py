import os

# Define your array of strings
items = [
    "starter_page",
    "contact_list",
    "profile",
    "timeline",
    "invoice",
    "faq",
    "pricing",
    "maintenance",
    "error_404",
    "error_404_alt",
    "error_500"
]








# Function to create HTML content
def create_html_content(item):
    return f""

# Get the current working directory
current_directory = os.getcwd()

# Iterate over each item and create an HTML file
for item in items:
    # Generate the HTML content
    html_content = create_html_content(item)
    
    # Create a safe filename
    filename = f"{item.replace(' ', '_')}.html"
    
    # Define the full path for the file
    file_path = os.path.join(current_directory, filename)
    
    # Write the HTML content to a file in the current directory
    with open(file_path, "w") as file:
        file.write(html_content)

print("HTML files created successfully in the current directory.")
