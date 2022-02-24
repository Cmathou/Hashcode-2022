


inFile = ["a.txt", "b.txt", "c.txt", "d.txt", "e.txt", "f.txt"]
outFile = ["a_out.txt", "b_out.txt", "c_out.txt", "d_out.txt", "e_out.txt", "f_out.txt"]

"""
line 1 : D duration / I intersections / S streets / V cars / F bonus temps
lines 2-S+1 : B - E (intersections debut fin) / street name / L time
lines S+2-S+V+1 = P nb streets / P * name of street
"""
begin=0
end=0
duration=0
streetsUsed=0
identity=0
name="test"

class ReadFiles:
	duration = 0
	intersectionsNumber = 0
	streetsNumber = 0
	carNumber = 0
	bonus = 0

	streets = {} #{name:[begin, end, duration]}
	cars = {} #{identity:[streetsUsed]}
	streetOut = []

	def __init__(self, fileNbr):
		data = open("problem/" + inFile[fileNbr], "r")
		lines = data.readlines()
		data.close()

		[self.duration, self.intersectionsNumber, self.streetsNumber, self.carNumber, self.bonus] = [int(i) for i in lines[0].split()]
		for i in range(self.intersectionsNumber):
			self.streetOut.append([])

		for i in lines[1:self.streetsNumber+1]:
			[begin, end, name, time] = [j for j in i.split()]

			self.streets[name] = [int(begin), int(end), int(time), 0]
			self.streetOut[int(end)].append(name)

		currentId = 0

		for i in lines[self.streetsNumber+1:]:
			number=int(i.split()[0])

			self.cars[currentId]=i.split()[1:]
			currentId+=1

	def getStreets(self, intersection):
		return self.streetOut[intersection]