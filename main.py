from Contributors import *
from Project import *
from ReadFiles import *
from Output import *


def init(lP, CA):
    pass

def updateProj(lP, lCB, lCA, day):
    ######Check project finish and release contributors
    for p in lP :
        if p.isFinished(day):
            ContribToSwitch = p.getContributors()
            moveToAvail(lCB, lCA, ContribToSwitch)



    ######Check if project are still doable and remove those without interest
    for i, p in enumerate(lP) : 
        if not p.isStarted() and not p.getScore(day):
            lP = lP[:i] + lP[i+1:]


    ######Check if new project can begin and attribute contributors
    for p in lP :
        if not p.isStarted():
            listCont = p.chercheContributors(lCA)
            if len(listCont) != 0 :
                p.Start(listCont, day)
                moveToBusy(lCA, lCB, listCont)


    pass

def moveToBusy(CA, CB, listCont):
    for toMove in listCont:
        if toMove in CA:
            CB.append(CA.pop(toMove))
    pass

def moveToAvail(CA, CB, listCont):
    for toMove in listCont:
        if toMove in CB:
            CA.append(CB.pop(toMove))
    pass




listProj = []
ContribBusy = []
ContribAvail = []

currentDate = 0

init(listProj, ContribBusy)


while len(listProj) != 0 :

    updateProj(listProj, ContribBusy, ContribAvail, currentDate)


    currentDate +=1



