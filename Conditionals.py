language = 'java'
if language == 'python':
	print('Language is python')
elif language == 'java':
	print('Language is java')
else:
	print ('no match')

user = 'admin'
logged_in = False

if user == 'admin' and logged_in:
	print ('admin page')
else:
	print ('bad creds')

if not logged_in:
	print('please login')
else:
	print ('welcome')

a = [1,2,3]
b = [1,2,3]
print(id(a))
print(id(b))
print (a is b)

a = [1,2,3]
b = a
print(id(a))
print(id(b))
print (a is b)

condition = False
condition = None
condition = 0
condition = 10
condition = []
condition = ()
condition = {}

if condition:
	print('evaluated to True')
else:
	print('evaluated to False')




