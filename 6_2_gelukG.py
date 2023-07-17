geluksgetallen = {'oliver': 3,
				  'stijn' : 5,
				  'nina' : 9,
				  'lexi' : 6,
				  'carrie': 0}
print(geluksgetallen['oliver'])
for naam , getal in geluksgetallen.items():
	print(naam+ " geluksgetal = " + str(getal))
