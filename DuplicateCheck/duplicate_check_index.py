from duplicate_check import find_duplicate_lines

from os import listdir

directorys = listdir('pureData')
# print(directorys)

for i in directorys:
    find_duplicate_lines("pureData/"+i)
    print(i+'file is done!___________________')


