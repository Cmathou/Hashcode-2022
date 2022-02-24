from Contributors import *
from Project import *
from ReadFiles import *
from Output import *


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
    for i, p in enumerate(lP) : 
        if not p.isStarted() and not p.getScore(day):
            lP = lP[:i] + lP[i+1:]


    ######Check if new project can begin and attribute contributors
    for p in lP :
        if not p.isStarted():
            listCont = p.searchContributors(lCA)
            if len(listCont) != 0 :
                p.startProject(listCont, day)
                moveToBusy(lCA, lCB, listCont)
                finP.append(p)
                finC.append(listCont)


    return finP, finC

def moveToBusy(CA, CB, listCont):
    print(CA, CB)
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




ContribBusy = []
finProj = []
finCont = []
currentDate = 0
nbFile = 0

listProj, ContribAvail = init(nbFile)

print(listProj, ContribAvail)

while len(listProj) != 0 :

    finProj, finCont = updateProj(listProj, ContribBusy, ContribAvail, currentDate, finProj, finCont)

    currentDate +=1

print(finProj, finCont)

