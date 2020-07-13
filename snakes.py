# Importing all modules
import os
import sys
import scr
import mec
import time
import msvcrt as m

# Global Varibales (can be point of attack)
BLANK = False
HIGH_SCORES = []

#Starting up the High Scores record
try:
    with open('hsl.bin','rb') as FILE:
        RECORD = None
        while RECORD != b'':
            RECORD = FILE.read(40)
            HIGH_SCORES.append(RECORD[:-1])
except FileNotFoundError :
    with open('hsl.bin','wb') as FILE:
        pass
    BLANK = True

# Loading records to memory
HIGH_SCORES = HIGH_SCORES[:-1]
NAMES = []
SCORES = []
MODES = []
for I in HIGH_SCORES:
    NAMES.append(I[:32])
    SCORES.append(I[-7:-1])
    MODES.append(I[-1:])
if HIGH_SCORES == []:
    BLANK = True

# Starting the main execution flow
G = scr.gui()
try:
    sel = None
    while sel != b'5':
        sel = G.MAINS()
        if sel == b'1':
            G.INSTRUCTIONS()
            NAME = G.NAME()
            LEVEL = G.LEVELS()
            SCORE = mec.GAME(int(LEVEL.decode())-1)
            if os.name == 'nt' :
                os.system('cls')
            else:
                os.system('clear')
            print('\n'*12)
            print(' '*55,'GAME OVER!')
            T_L = len(NAME)+len(str(SCORE))+14
            T_L /= 2
            T_L = 60-T_L
            print(' '*int(T_L),'{} Your Score : {}'.format(NAME,SCORE))
            if BLANK:
                NAME = bytes(NAME,'utf-8')+b'\x00'*(32-len(NAME))
                NAME += b'\x00'*(32-len(NAME))
                SCORE = '0'*(6-len(str(SCORE)))+str(SCORE)
                SCORE = bytes(SCORE,'utf-8')
                NAMES.append(NAME)
                SCORES.append(SCORE)
                MODES.append(LEVEL)
                BLANK = False
            else:
                RAN = False
                for I in range(len(SCORES)):
                    if int(SCORES[I])<=int(SCORE) :
                        NAME = bytes(NAME,'utf-8')+b'\x00'*(32-len(NAME))
                        NAME += b'\x00'*(32-len(NAME))
                        SCORE = '0'*(6-len(str(SCORE)))+str(SCORE)
                        SCORE = bytes(SCORE,'utf-8')
                        NAMES.insert(I,NAME)
                        SCORES.insert(I,SCORE)
                        MODES.insert(I,LEVEL)
                        RAN = True
                        break
                if not RAN :
                    NAME = bytes(NAME,'utf-8')+b'\x00'*(32-len(NAME))
                    NAME += b'\x00'*(32-len(NAME))
                    SCORE = '0'*(6-len(str(SCORE)))+str(SCORE)
                    SCORE = bytes(SCORE,'utf-8')
                    NAMES.append(NAME)
                    SCORES.append(SCORE)
                    MODES.append(LEVEL)
            with open('hsl.bin','wb') as f:                
                for I in range(len(NAMES)):
                    LINE = NAMES[I]+SCORES[I]+MODES[I]
                    f.write(LINE)
                    f.write(b'\r')
                    f.flush()
            time.sleep(2)
            while not m.kbhit() :
                pass
            os.system('cls')
        elif sel == b'2':
            G.INSTRUCTIONS()
        elif sel == b'3':
            SNAMES=[I.decode() for I in NAMES]
            SMODES=[I.decode('utf-8') for I in MODES]
            SSCORES=[I.decode() for I in SCORES]
            G.HIGH(SNAMES,SMODES,SSCORES)
        elif sel == b'4':
            G.CREDITS()
    os.system('cls')
except:
    #debugging part not removed
    typ,ob,tb=sys.exc_info()
    lineno = tb.tb_lineno
    fil = tb.tb_frame.f_code.co_filename
