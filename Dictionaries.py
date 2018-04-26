student = {'name': 'John', 'age': 25, 'courses': ['Math', 'Compsci']}

#student['phone'] = '555-5555'
#student['name'] = 'Jane'
student.update({ 'name': 'Jane', 'age': 26, 'phone': '555-555'})
#age = student.pop('age')
#print(student)
#print(age)
#print(student['name'])
#print(student.get('phone', 'Not_found'))
#print(len(student))
#print(student.keys())
#print(student.values())
# print(student.items())

for key,value in student.items():
	print(key, value)
