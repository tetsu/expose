import os
import shutil
import math

lists = os.listdir('girl_output')
lists.sort()

for list in lists:
    i = lists.index(list)

    if i+ 1 < len(lists):
        first = lists[i].split('.')[0]
        second = lists[i+1].split('.')[0]

        if first == second:
            # shutil.copyfile("./girl_output/" + lists[i] + "/hd_overlay.png", "./compile/{:0=3}.png".format(math.floor(i/2)))
            shutil.copyfile("./girl_output/" + lists[i] + "/hd_overlay.png", "./compile/" + first)