def how_many _days(chiffre)
	if chiffre in "1,3,5,7,9,11":
		print(chiffre,31)
	elif chiffre in "2":
		print(chiffre,28)
	else:
		print(chiffre,30)

