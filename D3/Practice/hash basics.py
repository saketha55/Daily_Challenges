#hashing basics
#initialisation

new_tble=dict(Dave = '001' , Ava= '002' , Joe= '003')
print(new_tble)

emp_details = {'Employee': {'Dave': {'ID': '001',
                                     'Salary': 2000,
                                     'Designation':'Python Developer'},
                            'Ava': {'ID':'002',
                                    'Salary': 2300,
                                    'Designation': 'Java Developer'},
                            'Joe': {'ID': '003',
                                    'Salary': 1843,
                                    'Designation': 'Hadoop Developer'}}}

#
#normal way using index
print(emp_details['Employee'])

print(emp_details['Employee']['Dave'])

print(emp_details['Employee']['Dave']['Salary'])

#using get() function
print(emp_details.get('Employee'))
      
print(emp_details.get('Employee').get('Ava'))

print(emp_details.get('Employee').get('Ava').get('Salary'))

#using 
