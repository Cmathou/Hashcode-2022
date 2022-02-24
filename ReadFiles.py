from Contributors import *
from Project import *


inFile = ["a.txt", "b.txt", "c.txt", "d.txt", "e.txt", "f.txt"]
outFile = ["a_out.txt", "b_out.txt", "c_out.txt", "d_out.txt", "e_out.txt", "f_out.txt"]


"""
line 1 :                      C n of contributors / P n of projects

lines 2:                      NAME1 name / Sn1 n of skills              //
lines 3 - 3+Sn1 :             S1 skill / Li1 skill level                //  C fois
line 3+Sn1+1 :                NAME name / Sn n of skills                //
lines 3+Sn1+2 - 3+Sn1+2+Sn2 : S2 skill / Li2 skill level                //

line N :                      Pn project name / Di days to complete / Si score / Bi best before / Ri n of roles
lines N+1 - N+Ri+1 :          Xk skill name / Lk level required 
"""



class ReadFiles:


	def __init__(self, fileNbr):
		data = open(inFile[fileNbr], "r")
		lines = data.readlines()
		data.close()
		currLine = 0

		self.allContrib = []
		self.allProjects = []

		[C, P] = [int(i) for i in lines[currLine].split()]

		for contributor in range(C):
			currLine+=1
			[name, Sn] = [i for i in lines[currLine].split()]
			Sn = int(Sn)
			skills = []
			level = []
			for skill in range(Sn):
				currLine+=1
				[skillName, skillLevel] = [i for i in lines[currLine].split()]
				skills.append(skillName)
				level.append(int(skillLevel))

			contrib = Contributor(name, skills, level)
			self.allContrib.append(contrib)

		for project in range(P):
			currLine+=1
			[Pn, D, S, B, R] = [i for i in lines[currLine].split()]
			D=int(D)
			S=int(S)
			B=int(B)
			R=int(R)
			skills = []
			level = []
			for skill in range(R):
				currLine+=1
				[skillName, skillLevel] = [i for i in lines[currLine].split()]
				skills.append(skillName)
				level.append(int(skillLevel))

			project = Project(Pn, D, S, B, skills, level)
			self.allProjects.append(project)




"""
T = ReadFiles(0)
for contrib in T.allContrib:
	print(contrib.getName())
	print(contrib.getSkills())

for proj in T.allProjects:
	print(proj.getName())
	print(type(proj.getLength()))
	print(proj.getScore())
	print(proj.getDeadline())
	print(proj.getRoles())
	print(proj.getSkills())
"""