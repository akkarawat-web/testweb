import struct
num_records = int(input("how many records do you want to create? "))
with open("records.bin", "wb") as file:
    for _ in range(num_records):
        id_number = int(input("Enter ID number: "))
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        gpa = float(input("Enter GPA: "))
        data = struct.pack('i20sif', id_number, name.encode('utf-8'), age, gpa)
        file.write(data)
print(f"{num_records} records have been written to records.bin.")