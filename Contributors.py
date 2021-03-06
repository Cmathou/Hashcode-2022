import numpy as np

class Contributor:

    def __init__(self, name, skills, levels):
        self.skills = skills
        self.levels = levels
        self.name = name
        self.available = True
        self.hasBeenTried = False
    
    def getName(self):
        return self.name
    
    def getSkills(self):
        return self.skills

    def getLevel(self, skill):
        if skill in self.skills:
            a = np.argwhere([s == skill for s in self.skills])[0][0]
            return self.levels[a]
        return 0
    
    def increaseLevel(self, skill):
        if not skill in self.skills:
            self.skills.append(skill)
            self.levels.append(0)
        a = np.argwhere([s == skill for s in self.skills])[0][0]  
        self.levels[a] += 1
    
    def isAvailable(self):
        return self.available
    
    def attributeProject(self):
        self.available = False
    
    def released(self):
        self.available = True

    def getHasBeenTried(self):
        return self.hasBeenTried

    def tryContributor(self):
        self.hasBeenTried = True

    def clearHasBeenTried(self):
        self.hasBeenTried = False



# t = Contributor(["C++", "python"], [2,4])

# print(t.getLevel("C++"))
# print(t.getLevel("HTML"))
# t.increaseLevel("C++")

# print(t.getLevel("C++"))

# t.increaseLevel("HTML")

# print(t.getLevel("HTML"))





