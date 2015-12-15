import random

with open("Mikojale.csv") as f:
	Mikolaje = f.read().splitlines()

random.shuffle(Mikolaje)

n=len(Mikolaje)

for i in range(n):
	print Mikolaje[i]+"->"+Mikolaje[(i+1)%n]
for i in range(n):
	piesel=Mikolaje[i]+"->"+Mikolaje[(i+1)%n]



















