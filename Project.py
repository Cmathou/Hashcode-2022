class Project:

    _name = ""
    _length = 0
    _score = 0
    _deadline = 0
    _roles = 0
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