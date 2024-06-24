def create_html_file():
    # Prompt the user for input
    name = input("Enter your name: ")
    description = input("Describe yourself: ")
    
    # Define the HTML content
    html_content = f"""<html>
<body>
<h1>{name}</h1>
<hr />
{description}
<hr />
</body>
</html>"""
    
    # Define the file name
    filename = "index.html"
    
    # Open a file in write mode
    with open(filename, 'w') as file:
        file.write(html_content)
    
    print(f"HTML file created successfully: {filename}")

if __name__ == "__main__":
    create_html_file()

input('hit enter to close')
