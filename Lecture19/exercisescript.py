#!/usr/bin/python

import matplotlib.pyplot as plt
import os

ecoli = open("/localdisk/data/BPSM/Lecture19/ecoli.txt").read().replace('\n', '').upper()

window = 1000

at = []
for start in range(len(ecoli) - window):
    win = ecoli[start:start+window]
    at.append((win.count('A') + win.count('T')) / window)

plt.figure(figsize=(20,10))
plt.plot(at, label="AT contents of ecoli genome")
plt.ylabel('AT content (%)')
plt.xlabel('Position on genome')
plt.legend()
plt.savefig("e.coliATcontent.png",transparent=True)
plt.show()


