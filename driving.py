country = input ('Your nationality: ')
age = input('Your age: ')
age = int(age)
if country == 'Taiwan' or 'taiwan':
	if age >=18:
		print('You can apply driving license')
	else:
		print('You cannot apply')
elif country == 'USA':
	if age >=16:
		print('You can apply driving license')
	else:
		print('You cannot apply')
else:
	print('your nationality is not allowed to apply')