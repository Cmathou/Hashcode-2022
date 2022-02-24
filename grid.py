from Contributors import *
from Project import *
from ReadFiles import *
from Output import *


def init(nbFile):
    T = ReadFiles(nbFile)
    return T.allProjects, T.allContrib

def isPlacementPossible(grid, day, project_length, contributors_index):
    for i in range(day, day + project_length):
        for j in range(len(contributors_index)):
            if grid[contributors_index[j]][i] != "":
                return False
    return True

def setProject(grid, day, project_length, contributors_index, project_name):
    for i in range(day, day + project_length):
        for j in range(len(contributors_index)):
            grid[contributors_index[j]][i] = project_name

nbFile = 2
last_day = 100
project_list = []
contributors_list = []

projects, contributors = init(nbFile)
grid = [["" for x in range(last_day)] for y in range(len(contributors))]
for project in projects:
    done = False
    contributors_selected = project.searchContributors(contributors)
    if (contributors_selected != []):
        for day in range(last_day - project.getLength()):
            if done:
                continue
            contributors_index = [contributors.index(x) for x in contributors_selected]
            if isPlacementPossible(grid, day, project.getLength(), contributors_index):
                setProject(grid, day, project.getLength(), contributors_index, project.getName())
                project_list.append(project)
                contributors_list.append(contributors_selected)
                done = True
                
                



writeOutput("c_out.txt", project_list, contributors_list)