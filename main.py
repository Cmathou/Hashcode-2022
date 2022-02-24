from Contributors import *
from Project import *
from ReadFiles import *
from Output import *

import time

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

def updateProj(lP, lCB, lCA, day, finP, finC, dic):
    ######Check project finish and release contributors
    t0 = time.time()
    for i, p in enumerate(lP) :

        t1 = time.time()
        if p.isFinished(day):
            ContribToSwitch = p.getContributors()
            for c in ContribToSwitch :
                c.released()
            # moveToAvail(lCB, lCA, ContribToSwitch)
            lP = lP[:i] + lP[i+1:]
            # t2 = time.time()
            # print("Finished: ",  t2-t1)
        ######Check if project are still doable and remove those without interest
        elif not p.isStarted() and not p.getScore(day):
            lP = lP[:i] + lP[i+1:]
            # t2 = time.time()
            # print("Score End :", t2-t1)
    
    t00 = time.time()
    # print("Int1:", t00 - t0)

    ######Check if new project can begin and attribute contributors
    for p in lP :
        if not p.isStarted():
            t1 = time.time()
            # listCont = p.searchContributors(lCA)
            listCont, dic = p.getCont(dic)
            t11 = time.time()
            # print("Search:", t11-t1)
            if len(listCont) != 0 :
                t2 = time.time()
                p.startProject(day, listCont)
                t22 = time.time()
                # print("Start: ", t22-t2)
                moveToBusy(lCA, lCB, listCont)
                t3 = time.time()
                # print("Move:", t3-t22)
                finP.append(p)
                finC.append(listCont)

    t000 = time.time()
    print("IntFin:", t000 - t00)

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
dic = makeDic(ContribAvail)

while len(listProj) != 0 :

    finProj, finCont, listProj = updateProj(listProj, ContribBusy, ContribAvail, currentDate, finProj, finCont, dic)

    t1 = time.time()
    val = getMiniDate(finProj, currentDate)
    t2 = time.time()
    print(t2-t1)
    currentDate += val

    print(val)

writeOutput("c_out.txt", finProj, finCont)



