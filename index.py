from storyViewDatareadabler import dataFixer
from math import ceil
from StoryViewData import dataCapturer
import pyautogui as pyag

from duplicate_file_remover import remove_duplicate_lines

storyNumber = str(input("Enter Story Number :   "))
a  = int(input('input viewer count :   '))
NumberOfTurns = int(ceil(a / 16.5))

dataCapturer(storyNumber,NumberOfTurns)
dataFixer(storyNumber)

indata = 'duplicatedData/''Export'+storyNumber+'Storydata.txt'
outdata = f"pureData/pure{storyNumber}Storydata.txt"
remove_duplicate_lines(indata,outdata)



# pyag.click(x=-900, y=414)
# pyag.moveTo(-900,600)


# close bottun location
# pyag.click(x=-800, y=414)

# test the fufcking app before using 
# pyag.click(x=2500, y=600)
# pyag.moveTo(2600,800)