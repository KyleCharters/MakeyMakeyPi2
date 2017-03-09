from sys import exit
from os import listdir
from random import randint
from simpleaudio import WaveObject
from getch import getch

sounds = []
playing = None

def playSound(cat, num):
    print("Playing " + str(cat + 1) + "-" + str(num))

    global playing
    if playing != None:
        playing.stop()
    playing = sounds[cat][num].play()

def playRandom(cat):
    playSound(cat, randint(0, len(sounds[cat]) - 1))

for file in listdir("./Sounds"):
    fileName = str(file)
    if fileName.endswith(".wav"):
        info = [int(x) for x in fileName[:3].split("-", 1)]

        for x in range(info[0] - len(sounds)):
            sounds.append([])

        print("Loaded " + fileName)

        sounds[info[0] - 1].append(WaveObject.from_wave_file("./Sounds/" + fileName))

WaveObject.from_wave_file("Startup.wav").play()

print("Ready")

while True:
    key = getch()

    if key == 'w':
        playRandom(0)
    elif key == 'a':
        playRandom(1)
    elif key == 's':
        playRandom(2)
    elif key == 'd':
        playRandom(3)
    elif key == 'f':
        playRandom(4)
    elif key == 'g':
        playRandom(5)
    elif key == 'p':
        exit()
