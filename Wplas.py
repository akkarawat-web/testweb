def example_w_plus_mode():
    with open('example.txt','w+') as file:
        file.write("This is a first line in the file\n")
        file.write("This is another line in the file\n")
        file.seek(0)  # Move the cursor to the beginning of the file
        contents = file.read()
        print("Contents of the file:")
        print(contents)
example_w_plus_mode()