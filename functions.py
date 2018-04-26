def hello_func():
	pass

print(hello_func)
print(hello_func())

def hello_func():
	print('hello function')

hello_func()
hello_func()
hello_func()
hello_func()

#Keep your code dry (don't repeat yourself in code)

def hello_func():
	return 'hello function'

print(hello_func().upper())

print (len('Test'))

def hello_func(greeting):
	return '{} Function.'.format(greeting)

print(hello_func('Hi'))