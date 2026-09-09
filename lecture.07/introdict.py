phonebook = {"Anirach": "7777-1111", "Michael": "7777-2222", "John": "7777-3333"} 
print(phonebook)
print(phonebook["Anirach"])  # Output: 7777-1111
print(phonebook.get("Michael"))  # Output: 7777-2222
key = "plute"
if key in phonebook:
    print(phonebook[plute])
else:
    print(key + 'not in phonebook')  # Output: plute not in phonebook

phonebook["simpson"] = "8888-1111"  # Update Anirach's number
phonebook["pluto"] = "9999-1111"  # Update Anirach's number
phonebook["minchael"] = "8888-2222"  # Update Anirach's number
print(phonebook)  # Output: {'Anirach': '7777-1111', 'Michael': '7777-2222', 'John': '7777-3333', 'simpson': '8888-1111', 'pluto': '9999-1111', 'minchael': '8888-2222'}
del phonebook["simpson"]  # Delete John from the phonebook
print(phonebook)  # Output: {'Anirach': '7777-1111', 'Michael': '7777-2222', 'John': '7777-3333', 'pluto': '9999-1111', 'minchael': '8888-2222'}