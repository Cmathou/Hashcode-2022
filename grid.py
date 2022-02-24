from Contributors import *
from Project import *
from ReadFiles import *
from Output import *


def init(nbFile):
    T = ReadFiles(nbFile)
    return T.allProjects, T.allContrib

def isPlacementPossible(grid, day, project_length, contributors_index):
    if (day + project_length > last_day):
        return -1
    min_available = []
    for i in range(len(contributors_index)):
        if "" in grid[contributors_index[i]][day:]:
            min_available.append(grid[contributors_index[i]][day:].index(""))
        else:
            return -1
    
    max_day = max(min_available)
    for i in range(max_day, max_day + project_length):
        for j in range(len(contributors_index)):
            if grid[contributors_index[j]][i] != "":
                return isPlacementPossible(grid, max_day + 1, project_length, contributors_index)
            else:
                return max_day

def setProject(grid, day, project_length, contributors_index, project_name):
    for i in range(day, day + project_length):
        for j in range(len(contributors_index)):
            grid[contributors_index[j]][i] = project_name

nbFile = 2
project_list = []
contributors_list = []

projects, contributors = init(nbFile)
last_day = 0
for project in projects:
    if project.getDeadline() + project.getScore(0) > last_day:
        last_day = project.getDeadline() + project.getScore(0)

grid = [["" for x in range(last_day)] for y in range(len(contributors))]
for project in projects:
    print("{:.2f}".format(100*projects.index(project)/len(projects)))
    contributors_selected = project.searchContributors(contributors)
    if (contributors_selected != []):
        contributors_index = [contributors.index(x) for x in contributors_selected]
        if isPlacementPossible(grid, 0, project.getLength(), contributors_index) >= 0:
            setProject(grid, 0, project.getLength(), contributors_index, project.getName())
            project_list.append(project)
            contributors_list.append(contributors_selected)
            continue
                
                



writeOutput("c_out.txt", project_list, contributors_list)