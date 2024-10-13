
importFiles = open('import.txt','r')

exportFiles = open('export.txt','w')
for i in importFiles:
    exportFiles.write((i.replace('\n',';'))+'\n')
    # i.replace('\n',';')
importFiles.close()
exportFiles.close()