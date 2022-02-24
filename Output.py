class Output:

    _outFile = ["a_out.txt", "b_out.txt", "c_out.txt", "d_out.txt", "e_out.txt", "f_out.txt"]
    _file = ""

    def __init__(self, fileNbr):
        self._file = "output/" + self._outFile[fileNbr]
        with open(self._file, "w+") as file:
            file.write('0\n')

    def setIntersection(self, intersection, streets, time):
        with open(self._file, "r") as file:
            content = file.readlines()

        with open(self._file, "w") as file:
            content[0] = str(int(content[0]) + 1) + '\n'
            content.append(str(intersection) + '\n')
            content.append(str(len(streets)) + '\n')
            for i in range(len(streets)):
                content.append(streets[i] + ' ' + str(time[i]) + '\n')
            file.writelines(content)