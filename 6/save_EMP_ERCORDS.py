num_emps = int(input('How many employee records do you want to create? '))
with open('employee_records.txt', 'w') as emp_file:
    for count in range(1, num_emps + 1):
        print('Enter data for employee #', count, sep='')
        name = input('Name: ')
        id_number = input('ID Number: ')
        department = input('Department: ')
        emp_file.weite(name + '\n')
        emp_file.write(id_number + '\n')
        emp_file.write(department + '\n')
        print()  
print