import os
import time as t
import msvcrt as m

class gui:
    def __init__(self):
        __A = ['░'*120]*10
        __C = ['░'*120]*10
        __B = '░'*47
        __M = []
        __M.extend(__A)
        __M.append(__B+'╔════════════════════════╗'+__B)
        __M.append(__B+'║      Snakes v2.0       ║'+__B)
        __M.append(__B+'╠════════════════════════╣'+__B)
        __M.append(__B+'║    1. Play Game        ║'+__B)
        __M.append(__B+'║    2. Instructions     ║'+__B)
        __M.append(__B+'║    3. High Scores      ║'+__B)
        __M.append(__B+'║    4. Credits          ║'+__B)
        __M.append(__B+'║    5. Exit             ║'+__B)
        __M.append(__B+'╚════════════════════════╝'+__B)
        __M.extend(__C)
        self.__MSCREEN = __M
        __L = []
        __A = ['░'*120]*11
        __C = ['░'*120]*10
        __L.extend(__A)
        __L.append(__B+'╔════════════════════════╗'+__B)
        __L.append(__B+'║      Snakes v2.0       ║'+__B)
        __L.append(__B+'╠════════════════════════╣'+__B)
        __L.append(__B+'║  Choose a level :      ║'+__B)
        __L.append(__B+'║    1. Easy             ║'+__B)
        __L.append(__B+'║    2. Medium           ║'+__B)
        __L.append(__B+'║    3. Hard             ║'+__B)
        __L.append(__B+'╚════════════════════════╝'+__B)
        __L.extend(__C)
        self.__LSCREEN = __L
        __N = []
        __A = ['░'*120]*13
        __C = ['░'*120]*12
        __B = '░'*33
        __N.extend(__A)
        __N.append(__B+'╔════════════════════════════════════════════════════╗'+__B)
        __N.append(__B+'║ Enter Your Name :                                  ║'+__B)
        __N.append(__B+'╚════════════════════════════════════════════════════╝'+__B)
        __N.extend(__C)
        self.__NSCREEN = __N
        __I = []
        __A = ['░'*120]*2
        __C = ['░'*120]*2
        __B = '░'*28
        __I.extend(__A)
        __I.append(__B+'╔══════════════════════════════════════════════════════════════╗'+__B)
        __I.append(__B+'║                          Snakes v2.0                         ║'+__B)
        __I.append(__B+'╠══════════════════════════════════════════════════════════════╣'+__B)
        __I.append(__B+'║  Instructions :                                              ║'+__B)
        __I.append(__B+'║    The movement keys are w,a,s,d. any other key held will    ║'+__B)
        __I.append(__B+'║    make the snake sprint. Even the movement key will help    ║'+__B)
        __I.append(__B+'║    the snake sprint in the direction corresponding.          ║'+__B)
        __I.append(__B+'║    The Game Comprises of 3 levels :   Easy , Medium , Hard   ║'+__B)
        __I.append(__B+'║                                                              ║'+__B)
        __I.append(__B+'║    Easy Mode is a borderless map and speed of the snake is   ║'+__B)
        __I.append(__B+'║    limited to 100 ie, makes one move in 1/100 of a second.   ║'+__B)
        __I.append(__B+'║                                                              ║'+__B)
        __I.append(__B+'║    Medium Mode is a bordered  map and speed of the snake is  ║'+__B)
        __I.append(__B+'║    also limited to 100                                       ║'+__B)
        __I.append(__B+'║                                                              ║'+__B)
        __I.append(__B+'║    Hard Mode is a bordered  map and speed of the snake is    ║'+__B)
        __I.append(__B+'║    uncontrolled ie, increses without end                     ║'+__B)
        __I.append(__B+'║                                                              ║'+__B)
        __I.append(__B+'║    However in any mode the goal is to eat as many prey as    ║'+__B)
        __I.append(__B+'║    possible without hiting border (if not in easy mode) or   ║'+__B)
        __I.append(__B+'║    snake tail. Also the speed increases by eating prey       ║'+__B)
        __I.append(__B+'║    regarding with modes.                                     ║'+__B)
        __I.append(__B+'║                                                              ║'+__B)
        __I.append(__B+'║    Press any key to continue..........                       ║'+__B)
        __I.append(__B+'╚══════════════════════════════════════════════════════════════╝'+__B)
        __I.extend(__C)
        self.__ISCREEN = __I
        __CRED = []
        __A = ['░'*120]*11
        __C = ['░'*120]*11
        __B = '░'*18
        __CRED.extend(__A)
        __CRED.append(__B+' '*10+'░'*4+' '*10+'░'*6+' '*8+'░'*10+' '*4+'░'*8+' '*6+'░'*8+' '*2+'░'*6+' '*2+__B)
        __CRED.append(__B+'░'*7+' '*3+'░'*8+' '*2+'░'*9+' '*2+'░'*7+' '*2+'░'*6+' '*2+'░'*4+' '*2+'░'*6+' '*2+'░'*4+' '*2+'░'*6+' '*2+'░'*6+' '*2+__B)
        __CRED.append(__B+'░'*7+' '*3+'░'*8+' '*2+'░'*8+' '*2+'░'*15+' '*2+'░'*6+' '*2+'░'*5+' '*2+'░'*5+' '*2+'░'*5+' '*2+'░'*6+' '*2+__B)
        __CRED.append(__B+'░'*7+' '*3+'░'*8+' '*2+'░'*7+' '*2+'░'*15+' '*2+'░'*8+' '*2+'░'*4+' '*2+'░'*6+' '*2+'░'*4+' '*2+'░'*6+' '*2+__B)
        __CRED.append(__B+'░'*7+' '*3+'░'*8+' '*2+'░'*7+' '*2+'░'*5+' '*6+'░'*4+' '*2+'░'*8+' '*2+'░'*4+' '*2+'░'*6+' '*2+'░'*4+' '*2+'░'*6+' '*2+__B)
        __CRED.append(__B+'░'*7+' '*3+'░'*8+' '*2+'░'*7+' '*2+'░'*5+' '*2+'░'*2+' '*2+'░'*5+' '*2+'░'*6+' '*2+'░'*5+' '*2+'░'*5+' '*2+'░'*5+' '*2+'░'*6+' '*2+__B)
        __CRED.append(__B+' '*2+'░'*4+' '*3+'░'*9+' '*2+'░'*8+' '*3+'░'*3+' '*2+'░'*2+' '*2+'░'*6+' '*2+'░'*4+' '*2+'░'*6+' '*2+'░'*4+' '*2+'░'*6+' '*2+'░'*6+' '*2+__B)
        __CRED.append(__B+'░'+' '*7+'░'*6+' '*10+'░'*6+' '*5+'░'*3+' '*2+'░'*8+' '*4+'░'*8+' '*6+'░'*9+' '*8+'░'+__B)
        __CRED.extend(__C)
        self.__CSCREEN = __CRED
        __H = []
        __B = '░'*28
        __H.append(__B+'╔══════════════════════════════════════════════════════════════╗'+__B)
        __H.append(__B+'║                          Snakes v2.0                         ║'+__B)
        __H.append(__B+'║                          HIGH SCORES!                        ║'+__B)
        __H.append(__B+'╠══════════════════════════════════════════════════════════════╣'+__B)
        __H.append(__B+'║  HARD MODE :                                                 ║'+__B)
        __H.append(__B+'║  ╔═══════════════════════════════════╦══════════════════╗    ║'+__B)
        __H.append(__B+'║  ║               NAME                ║      SCORES      ║    ║'+__B)
        __H.append(__B+'║  ╠═══════════════════════════════════╬══════════════════╣    ║'+__B)
        __H.append(__B+'║  ║ ________________________________  ║ ________________ ║    ║'+__B)
        __H.append(__B+'║  ║ ________________________________  ║ ________________ ║    ║'+__B)
        __H.append(__B+'║  ║ ________________________________  ║ ________________ ║    ║'+__B)
        __H.append(__B+'║  ╚═══════════════════════════════════╩══════════════════╝    ║'+__B)
        __H.append(__B+'║  MEDIUM MODE :                                               ║'+__B)
        __H.append(__B+'║  ╔═══════════════════════════════════╦══════════════════╗    ║'+__B)
        __H.append(__B+'║  ║               NAME                ║      SCORES      ║    ║'+__B)
        __H.append(__B+'║  ╠═══════════════════════════════════╬══════════════════╣    ║'+__B)
        __H.append(__B+'║  ║ ________________________________  ║ ________________ ║    ║'+__B)
        __H.append(__B+'║  ║ ________________________________  ║ ________________ ║    ║'+__B)
        __H.append(__B+'║  ║ ________________________________  ║ ________________ ║    ║'+__B)
        __H.append(__B+'║  ╚═══════════════════════════════════╩══════════════════╝    ║'+__B)
        __H.append(__B+'║  EASY MODE :                                                 ║'+__B)
        __H.append(__B+'║  ╔═══════════════════════════════════╦══════════════════╗    ║'+__B)
        __H.append(__B+'║  ║               NAME                ║      SCORES      ║    ║'+__B)
        __H.append(__B+'║  ╠═══════════════════════════════════╬══════════════════╣    ║'+__B)
        __H.append(__B+'║  ║ ________________________________  ║ ________________ ║    ║'+__B)
        __H.append(__B+'║  ║ ________________________________  ║ ________________ ║    ║'+__B)
        __H.append(__B+'║  ║ ________________________________  ║ ________________ ║    ║'+__B)
        __H.append(__B+'║  ╚═══════════════════════════════════╩══════════════════╝    ║'+__B)
        __H.append(__B+'╚══════════════════════════════════════════════════════════════╝'+__B)
        self.__HSCREEN = __H
    def GET_M(self):
        return self.__MSCREEN

    def GET_L(self):
        return self.__LSCREEN

    def GET_N(self):
        return self.__NSCREEN
    
    def GET_I(self):
        return self.__ISCREEN

    def MAINS(self):
        if os.name == 'nt' :
            os.system('cls')
        else:
            os.system('clear')
        for I in self.__MSCREEN :
            print(I)
        while True:
            if m.kbhit():
                v =m.getch()
                if v in [b'1',b'2',b'3',b'4',b'5',b'6']:
                    break
        return v

    def INSTRUCTIONS(self):
        if os.name == 'nt' :
            os.system('cls')
        else:
            os.system('clear')
        for I in self.__ISCREEN :
            print(I)
        while not m.kbhit():
            pass
        t.sleep(0.25)
        a = m.getch()
        if a in [b'\x00',b'\xe0']:
            _ = m.getch()
        
    def CREDITS(self):
        T =[]
        for I in self.__CSCREEN:
            print(I)
        while not m.kbhit():
            n = t.perf_counter()
            T.append(n)
            if T[-1]-T[0]>0.08:
                if os.name == 'nt' :
                    os.system('cls')
                else:
                    os.system('clear')
                for I in range(len(self.__CSCREEN)) :
                    if I>=11 and I<=19:
                        self.__CSCREEN[I]= self.__CSCREEN[I][1:]+self.__CSCREEN[I][0]
                for I in self.__CSCREEN:
                    print(I)
                del T
                T = []
        _ = m.getch()
        t.sleep(0.25)

    def LEVELS(self):
        if os.name == 'nt' :
            os.system('cls')
        else:
            os.system('clear')
        for I in self.__LSCREEN :
            print(I)
        while True:
            if m.kbhit():
                v =m.getch()
                if v in [b'1',b'2',b'3']:
                    break
        return v

    def NAME(self):
        if os.name == 'nt' :
            os.system('cls')
        else:
            os.system('clear')
        NAME = ''
        for I in range(len(self.__NSCREEN)) :
            for J in range(len(self.__NSCREEN[I])):
                if I == 14 and J == 53 :
                    print('█',end='')
                else :
                    print(self.__NSCREEN[I][J],end='') 
            print('\n',end='')
        while True:
            if m.kbhit():
                K =m.getch()
                if K != b'\r':
                    if K == b'\x08' :
                        NAME = NAME[:-1]
                    elif K == b'\x1b' :
                        pass
                    elif K in [b'\xe0',b'\x00']:
                        if m.getch() in [b'H',b'M',b'K',b'P',b'S']:
                            pass
                    else:
                        if len(NAME)<31:
                            NAME += K.decode()
                    SCRN = self.__NSCREEN.copy()
                    TSCR = ''
                    L = []
                    for J in range(len(self.__NSCREEN[14])):
                        if J == 53 :
                            L.append(J)
                            for Z in range(len(NAME)):
                                TSCR += NAME[Z]
                                J += 1
                                L.append(J)
                            TSCR += '█'
                        elif J in L :
                            pass
                        else:
                            TSCR += self.__NSCREEN[14][J]
                
                    SCRN[14] = TSCR
                    if os.name == 'nt' :
                        os.system('cls')
                    else:
                        os.system('clear')
                    for I in SCRN :
                        print(I)
                else:
                    if len(NAME) == 0:
                        pass
                    else:
                        return NAME
    def HIGH(self,__NAMES,__MODES,__SCORES):
        if os.name == 'nt' :
            os.system('cls')
        else:
            os.system('clear')
        __H,__M,__E=3,3,3
        __POS_H,__POS_M,__POS_E=[],[],[]
        for I in range(len(__MODES)):
            if __MODES[I] == '1' and __E>0:
                __E -= 1
                __POS_E.append(I)
            elif __MODES[I] == '2' and __M>0:
                __M -= 1
                __POS_M.append(I)
            elif __MODES[I] == '3' and __H>0:
                __H -= 1
                __POS_H.append(I)
        __SCR = self.__HSCREEN.copy()
        for I in range(len(__POS_H)):
            __SCR[I+8]  = '░'*28+'║  ║ '+__NAMES[__POS_H[I]]+'  ║      '+__SCORES[__POS_H[I]]+'      ║    ║'+'░'*28
        for I in range(len(__POS_M)):
            __SCR[I+16]  = '░'*28+'║  ║ '+__NAMES[__POS_M[I]]+'  ║      '+__SCORES[__POS_M[I]]+'      ║    ║'+'░'*28
        for I in range(len(__POS_E)):
            __SCR[I+24]  = '░'*28+'║  ║ '+__NAMES[__POS_E[I]]+'  ║      '+__SCORES[__POS_E[I]]+'      ║    ║'+'░'*28
        for I in __SCR :
            print(I)
        t.sleep(1)
        while not m.kbhit():
            pass
        _ = m.getch()


if __name__ == "__main__":
    HIGH_SCORES = []
    try:
        with open('hsl.bin','rb') as FILE:
            RECORD = None
            while RECORD != b'':
                RECORD = FILE.read(40)
                HIGH_SCORES.append(RECORD[:-1].decode('utf-8'))
    except FileNotFoundError :
        with open('hsl.bin','wb') as FILE:
            print('Save File Was Not found....')
            t.sleep(1)
            pass
    HIGH_SCORES = HIGH_SCORES[:-1]
    NAMES = []
    SCORES = []
    MODES = []
    for I in HIGH_SCORES:
        NAMES.append(I[:32])
        SCORES.append(I[-7:-1])
        MODES.append(I[-1])
    
    G = gui()
    G.HIGH(NAMES,MODES,SCORES)
    # print(NAMES)
    # print(MODES)
    # print(SCORES)
                     
