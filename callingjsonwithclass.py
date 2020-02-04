import json

def getFileContent(pathAndFileName):
    with open(pathAndFileName, 'r') as theFile:
        data = theFile.read().split('\n')
        return data

listOfLines = getFileContent('./greekcharacters.json')

for line in listOfLines:
    print('----')
    print(line)