landen = {'Belgie':'brussel',
		'duitsland' : 'Berlijn',
		'UK' : 'Londen'}
		
print("landen")
for land in landen.keys():
	print(land)

print("")
print("steden")
for stad in landen.values():
	print(stad)
	
for land, stad in landen.items():
	print("de hoofdstad van " + land + " is " + stad)
	

landen['taiwan'] = 'taipei'


for land, stad in landen.items():
	print("de hoofdstad van " + land + " is " + stad)
