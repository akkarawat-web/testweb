def example_a_plus_mode():
    with open('example.txt','a+') as file:
       file.seek(0)  # Move the cursor to the beginning of the file
       contents = file.read() 
       print("Contents contained of the file:")
       print(contents)
       file.write("This is a new line added to the file\n")
       file.seek(0)  # Move the cursor to the beginning of the file again
       updated_contents = file.read()
       print("\nUpdated contents of the file:")
       print(updated_contents)