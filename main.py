from Contributors import *
from Project import *
from ReadFiles import *
from Output import *


def makeDic(contributors):
    dic = {}
    for contrib in contributors:
        for skill in contrib.getSkills():
            if skill in dic.keys():
                dic[skill].append(contrib)
            else:
                dic[skill] = [contrib]
    return dic


def init(nbFile):
    T = ReadFiles(nbFile)
    return T.allProjects, T.allContrib

def updateProj(lP, lCB, lCA, day, finP, finC):
    ######Check project finish and release contributors
    for i, p in enumerate(lP) :
        if p.isFinished(day):
            ContribToSwitch = p.getContributors()
            moveToAvail(lCB, lCA, ContribToSwitch)
            lP = lP[:i] + lP[i+1:]


    ######Check if project are still doable and remove those without interest
        elif not p.isStarted() and not p.getScore(day):
            lP = lP[:i] + lP[i+1:]


    ######Check if new project can begin and attribute contributors
    for p in lP :
        if not p.isStarted():
            listCont = p.searchContributors(lCA)
            if len(listCont) != 0 :
                p.startProject(day, listCont)
                moveToBusy(lCA, lCB, listCont)
                finP.append(p)
                finC.append(listCont)


    return finP, finC, lP

def moveToBusy(CA, CB, listCont):
    for toMove in listCont:
        if toMove in CA:
            CB.append(toMove)
            CA.remove(toMove)
    pass

def moveToAvail(CA, CB, listCont):
    for toMove in listCont:
        if toMove in CB:
            CA.append(toMove)
            CB.remove(toMove)
    pass

def getMiniDate(P, d):
    mini = 1e10
    for k in P : 
        m = k.timeToFinish(d)
        if m > 0 : 
            mini = np.min([mini, m])

    return mini

ContribBusy = []
finProj = []
finCont = []
currentDate = 0
nbFile = 2

listProj, ContribAvail = init(nbFile)

#print(makeDic(ContribAvail))

while len(listProj) != 0 :

    finProj, finCont, listProj = updateProj(listProj, ContribBusy, ContribAvail, currentDate, finProj, finCont)

    val = getMiniDate(finProj, currentDate)

    currentDate += val

    print(val)

writeOutput("c_out.txt", finProj, finCont)



