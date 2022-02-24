


"""
line 1 : n of projects

line 2 : name project
line 3 : contributor 1 / contributor 2 / contributor 3 ...

line 2 : name project
line 3 : contributor 1 / contributor 2 / contributor 3 ...

...

"""


def writeOutput(fileName, projects, contributors):
    with open(fileName, "w+") as file:
        file.write(str(len(projects))+"\n")

        for project in range(len(projects)):
            file.write(projects[project].getName()+"\n")
            for contrib in contributors[project]:
                file.write(contrib.getName()+" ")
            file.write("\n")
        file.write("\n")

