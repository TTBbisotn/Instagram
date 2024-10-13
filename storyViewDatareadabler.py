
def dataFixer(storyNumber):
    dataFile = open('firstPhase/'+ 'story' + storyNumber+'data.txt','r',encoding='utf-8')
    import re     
    data = re.findall('\'s profile picture\n.*\n(.*)',dataFile.read())
    exportData = open('duplicatedData/''Export'+storyNumber+'Storydata.txt','w')

    for i in data :
        exportData.write(i+';\n')

