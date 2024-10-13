import pyautogui as pyag
from pyperclip import paste
# from time import sleep

pyag.PAUSE = 0.09
def dataCapturer(storyNumber,NumberOfTurns):
    dataFile = open('firstPhase/'+ 'story' + storyNumber+'data.txt','a+',encoding='utf-8')
    for i in range(NumberOfTurns):
        pyag.click(x=410, y=250)
        pyag.click(x=410, y=250)
        pyag.moveTo(410,400)
        # ______system ghaii dada
        # pyag.click(x=2500, y=600) 
        # pyag.click(x=2500, y=600)
        # pyag.moveTo(2600,800)
        # ______system shercat
        # pyag.click(x=-900, y=414)
        # pyag.click(x=-900, y=414)
        # pyag.moveTo(-900,600)
        pyag.hotkey('ctrl','a')
        pyag.hotkey('ctrl','c')
        dataFile.write(paste())
        # print(paste())
        # _______scroll windows 
        # pyag.scroll(-1000)
        # _______Scroll linux 
        pyag.scroll(-7)

    dataFile.close()