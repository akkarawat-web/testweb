phonebook = {'Anirach': '7777-1111', 'Michael': '7777-2222', 'Donald': '7777-3333'}
phonebook['bart'] = [1, 2, 3]
elements = len(phonebook)
print('There are', elements, ', names in phonebook')
for key in phonebook:
    print(key, 'phones number is', phonebook[key])
phonebook['bart'][1]=9
print(phonebook)