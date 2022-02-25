from Contributors import *
from Project import *
from ReadFiles import *
from Output import *


from multiprocessing import Process
import progressbar
import sys
limitRecur = 10000
sys.setrecursionlimit(limitRecur+50) #increase stack size to allow more recursions, increasing could get better results 
                                     #default stack size is 1000

cpt=0


def init(nbFile):
    T = ReadFiles(nbFile)
    return T.allProjects, T.allContrib

def isPlacementPossible(grid, day, project_length, contributors_index):
    global cpt, last_day
    #print("today is "+str(day))
    #print("end day would be " +str(day+project_length))
    #print("last day is "+str(last_day))
    #print(cpt)
    cpt += 1
    if(cpt >= limitRecur): #stop before the recursion limit is reached and assume it can't be placed
        return -1
    if (day + project_length > last_day):
        return -1
    min_available = []
    for i in range(len(contributors_index)):
        if "" in grid[contributors_index[i]][day:]:
            min_available.append(grid[contributors_index[i]][day:].index(""))
        else:
            return -1
    
    max_day = max(min_available)+day
    #print("first free day for all is " + str(max_day))
    if(max_day == day): #if all contrib are free on day "day"
        for i in range(max_day, max_day + project_length):
            for j in range(len(contributors_index)):
                if grid[contributors_index[j]][i] != "":
                    #print("one isn't free long enough after day "+str(max_day))
                    return isPlacementPossible(grid, max_day + 1, project_length, contributors_index)
        #print(max_day)
        return max_day
    else: #check if all contribs are free on day "max_day"
        #print("one isn't free today day "+str(max_day))
        return isPlacementPossible(grid, max_day, project_length, contributors_index)

def setProject(grid, day, project_length, contributors_index, project_name):
    for i in range(day, day + project_length):
        #print(i, day + project_length)
        for j in range(len(contributors_index)):
            grid[contributors_index[j]][i] = project_name

inFile = ["a.txt", "b.txt", "c.txt", "d.txt", "e.txt", "f.txt"]
outFile = ["a_out.txt", "b_out.txt", "c_out.txt", "d_out.txt", "e_out.txt", "f_out.txt"]

def run(nbFile):
    global cpt, last_day
    project_list = []
    contributors_list = []
    
    projects, contributors = init(nbFile)
    last_day = 0
    for project in projects:
        if project.getDeadline() + project.getScore(0) > last_day:
            last_day = project.getDeadline() + project.getScore(0)
            #print(project.getName())
    
    #print(last_day)
    last_day_max = last_day
    
    grid = [["" for x in range(last_day)] for y in range(len(contributors))]
    for project in progressbar.progressbar(projects):                        #comment this line and uncomment the next 2 if you don't have progressbar
    #for project in projects:
    #    print("{:.2f}".format(100*projects.index(project)/len(projects)))
        contributors_selected = [1]
    
        while ((contributors_selected != []) and (project not in project_list)):
    
            contributors_selected = project.searchContributors(contributors)
    
            if contributors_selected != []:
                contributors_index = [contributors.index(x) for x in contributors_selected]
    
                for contrib in contributors_selected:
                    contrib.tryContributor()
    
                last_day = project.getDeadline() + project.getScore(0)  #update last_day for each project 
                                                                        # there are still some projects making 0 points with just "last_day = project.getDeadline()" 
                                                                        # so it looks like it's not perfect yet
                #print(last_day, project.getName())
    
                cpt=0
                dayToStart = isPlacementPossible(grid, 0, project.getLength(), contributors_index)
    
                if dayToStart >= 0:
                    setProject(grid, dayToStart, project.getLength(), contributors_index, project.getName()) #starts project on the right day
                    project_list.append(project)
                    contributors_list.append(contributors_selected)
                    #continue
    
        for contrib in contributors:
            contrib.clearHasBeenTried()
                    
                    
    #for contrib in grid:
    #    print(contrib[:100])
    
    writeOutput(outFile[nbFile], project_list, contributors_list)    
    print(inFile[nbFile]+" done")

#uncomment following to run sequentially
"""
print("running a")
run(0)
print("running b")
run(1)
print("running c")
run(2)
print("running d")
run(3)
print("running e")
run(4)
print("running f")
run(5)
"""

#comment following to run sequentially
if (__name__ == "__main__"):

    file0 = Process(target=run, args=(0,))
    file1 = Process(target=run, args=(1,))
    file2 = Process(target=run, args=(2,))
    file3 = Process(target=run, args=(3,))
    file4 = Process(target=run, args=(4,))
    file5 = Process(target=run, args=(5,))

    file0.start()
    file1.start()
    file2.start()
    file3.start()
    file4.start()
    file5.start()

    file0.join() #attend la fin de fileX pour la mesure avec time.time()
    file1.join()
    file2.join()
    file3.join()
    file4.join()
    file5.join()
