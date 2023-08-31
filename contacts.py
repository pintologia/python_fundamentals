contacts = {
    'number': 4, 
    'students': [
        {'name': 'Sara Holderness', 'email': 'sara@gmail.com'},
        {'name': 'Silvina Holdeness', 'email': 'silvina@gmail.com'},
        {'name': 'Sara Sandra', 'email': 'sandra@gmail.com'},
    ] 
}

print('Students email:')

for key in contacts['students']:
    print(key['email'])
    
    
#Inside the loop, this line prints the value associated 
# with the 'email' key in the current dictionary,
# which represents the email address of a student.