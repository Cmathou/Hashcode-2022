from Contributors import *

class Project:

    _name = ""
    _length = 0
    _score = 0
    _deadline = 0
    _roles = []
    _skills = []

    def __init__(self, name, length, score, deadline, roles, skills):
        self._name = name
        self._length = length
        self._score = score
        self._deadline = deadline
        self._roles = roles
        self._skills = skills

    def get_name(self):
        return self._name

    def get_length(self):
        return self._length

    def get_score(self):
        return self._score

    def get_deadline(self):
        return self._deadline

    def get_roles(self):
        return self._roles

    def get_skills(self):
        return self._skills

    def search_contributors(self, contributors):
        selected = []
        for role in self._roles:
            for contributor in contributors:
                if (contributor.getLevel(role) >= self._skills[self._roles.index(role)] and contributor not in selected):
                    selected.append(contributor)
                    break
        return selected

# c = [Contributor("aaa", ["a"], [2]), Contributor("aba", ["b"], [2]), Contributor("aca", ["c"], [2]), Contributor("ada", ["d"], [2]), Contributor("aea", ["e"], [2])]
# p = Project("gh", 0, 0, 0, ["d", "c", "e"], [0, 1, 1])

# s = p.search_contributors(c)
# for e in s:
#     print(e.getName())