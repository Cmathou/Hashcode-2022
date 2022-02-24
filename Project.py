from Contributors import *

class Project:

    _name = ""
    _length = 0
    _score = 0
    _deadline = 0
    _roles = []
    _skills = []

    _day = -1
    _contributors = []

    def __init__(self, name, length, score, deadline, roles, skills):
        self._name = name
        self._length = length
        self._score = score
        self._deadline = deadline
        self._roles = roles
        self._skills = skills

    def getName(self):
        return self._name

    def getLength(self):
        return self._length

    def getScore(self, actual_day):
        if (actual_day <= self._deadline):
            return self._score
        elif (actual_day >= self._deadline + self._score):
            return 0
        else:
            return self._score - (actual_day - self._deadline)
            

    def getDeadline(self):
        return self._deadline

    def getRoles(self):
        return self._roles

    def getSkills(self):
        return self._skills

    def startProject(self, day, contributors):
        self._day = day
        self._contributors = contributors

    def getContributors(self):
        return self._contributors

    def isStarted(self):
        return True if (self._day != -1) else False

    def isFinished(self, actual_day):
        return True if (self._day + self._length <= actual_day and self._day != -1) else False

    def searchContributors(self, contributors):
        selected = []
        for role in self._roles:
            for contributor in contributors:
                if (contributor.getLevel(role) >= self._skills[self._roles.index(role)] and contributor not in selected):
                    selected.append(contributor)
                    break
        if len(selected) == len(self._roles):
            return selected
        else:
            return []

    def timeToFinish(self, actual_day):
        return self._length-(actual_day-self._day)

# c = [Contributor("aaa", ["a"], [2]), Contributor("aba", ["b"], [2]), Contributor("aca", ["c"], [2]), Contributor("ada", ["d"], [2]), Contributor("aea", ["e"], [2])]
# p = Project("gh", 0, 0, 0, ["d", "c", "e"], [0, 1, 1])

# s = p.search_contributors(c)
# for e in s:
#     print(e.getName())