# Game Mechanics Module

#Importing Necessary modules
import os
import ent as e
import time as t
import msvcrt as m
import random as r

# Funtions
def VALID(VAL):
    if VAL in [b'w',b'a',b's',b'd']:
        return 1
    else :
        return 0
 
def POLAR(VAL):
    if VAL==b'w':
        return b's'
    elif VAL==b'a':
        return b'd'
    elif VAL==b's':
        return b'w'
    elif VAL==b'd':
        return b'a'

def RANDOM_DIR():
    V = r.randint(1,4)
    if V == 1 :
        return b'w'
    elif V == 2 :
        return b'd'
    elif V == 3 :
        return b'a'
    else :
        return b's'

def ACTION(MODE,WINDOW,SNAKE,PREY,KEY,SCORE,SPEED):
    NEXT_P = SNAKE.GRASP(KEY)
    PREY_P = PREY.GET()
    SNAKES = SNAKE.GET()
    if NEXT_P == PREY_P :
        SNAKE.EAT(PREY_P)
        PREY.RESPAWN()
        SCORE += 1
        if MODE == 2:
            SPEED += 1
        else:
            if SPEED<101:
                SPEED += 1
        return 1,SCORE,SPEED
    elif WINDOW.HIT_BOUND(NEXT_P):
        if MODE == 0:
            NEXT_P = SNAKE.JUMP_GRASP(KEY)
            if NEXT_P == PREY_P :
                SNAKE.EAT(PREY_P)
                PREY.RESPAWN()
                SCORE += 1
                if SPEED<101:
                    SPEED += 1
                return 1,SCORE,SPEED
            elif NEXT_P == SNAKES[-2] :
                KEY = POLAR(KEY)
                return ACTION(MODE,WINDOW,SNAKE,PREY,KEY,SCORE,SPEED)
            elif NEXT_P in SNAKES[:-3] :
                return 0,SCORE,SPEED
            else:
                SNAKE.JUMP(KEY)
                return 1,SCORE,SPEED
        else:
            return 0,SCORE,SPEED
    elif NEXT_P == SNAKES[-2] :
        KEY = POLAR(KEY)
        return ACTION(MODE,WINDOW,SNAKE,PREY,KEY,SCORE,SPEED)
    elif NEXT_P in SNAKES[:-3] :
        return 0,SCORE,SPEED
    else:
        SNAKE.MOVE(KEY)
        return 1,SCORE,SPEED

# def ACTION(MODE,WINDOW,SNAKE,PREY,KEY,SCORE,SPEED):
#     if MODE == 0:
#         NEXT_P = SNAKE.GRASP(KEY)
#         PREY_P = PREY.GET()
#         SNAKES = SNAKE.GET()
#         if NEXT_P == PREY_P :
#             SNAKE.EAT(PREY_P)
#             PREY.RESPAWN()
#             SCORE += 1
#             if SPEED<101:
#                 SPEED += 1        
#             return 1,SCORE,SPEED
#         elif WINDOW.HIT_BOUND(NEXT_P):
#             KEY = SNAKE.JUMP(KEY)
#             return ACTION(MODE,WINDOW,SNAKE,PREY,KEY,SCORE,SPEED)
#         elif NEXT_P == SNAKES[-2] :
#             KEY = POLAR(KEY)
#             return ACTION(MODE,WINDOW,SNAKE,PREY,KEY,SCORE,SPEED)
#         elif NEXT_P in SNAKES[:-3] :
#             return 0,SCORE,SPEED
#         else:
#             SNAKE.MOVE(KEY)
#             return 1,SCORE,SPEED
#     elif MODE == 1:
#         NEXT_P = SNAKE.GRASP(KEY)
#         PREY_P = PREY.GET()
#         SNAKES = SNAKE.GET()
#         if NEXT_P == PREY_P :
#             SNAKE.EAT(PREY_P)
#             PREY.RESPAWN()
#             SCORE += 1
#             if SPEED<101:
#                 SPEED += 1        
#             return 1,SCORE,SPEED
#         elif WINDOW.HIT_BOUND(NEXT_P):
#             return 0,SCORE,SPEED
#         elif NEXT_P == SNAKES[-2] :
#             KEY = POLAR(KEY)
#             return ACTION(MODE,WINDOW,SNAKE,PREY,KEY,SCORE,SPEED)
#         elif NEXT_P in SNAKES[:-3] :
#             return 0,SCORE,SPEED
#         else:
#             SNAKE.MOVE(KEY)
#             return 1,SCORE,SPEED
#     else:
#         NEXT_P = SNAKE.GRASP(KEY)
#         PREY_P = PREY.GET()
#         SNAKES = SNAKE.GET()
#         if NEXT_P == PREY_P :
#             SNAKE.EAT(PREY_P)
#             PREY.RESPAWN()
#             SCORE += 1
#             SPEED += 1        
#             return 1,SCORE,SPEED
#         elif WINDOW.HIT_BOUND(NEXT_P):
#             return 0,SCORE,SPEED
#         elif NEXT_P == SNAKES[-2] :
#             KEY = POLAR(KEY)
#             return ACTION(MODE,WINDOW,SNAKE,PREY,KEY,SCORE,SPEED)
#         elif NEXT_P in SNAKES[:-3] :
#             return 0,SCORE,SPEED
#         else:
#             SNAKE.MOVE(KEY)
#             return 1,SCORE,SPEED
def GAME(MODE):
    W = e.window()
    SCR =W.GET()
    S = e.snake(SCR)
    P = e.prey(SCR)
    W.UPDATE(S.GET(),P.GET(),0)
    SCORE = 0
    SPEED = 10
    A = []
    K = None
    N = 1
    DEBUG = 0
    while N :
        if m.kbhit() :
            K = m.getch()
            if VALID(K):
                OLD_K = K
            else:
                if K == b'/':
                    if DEBUG == 0 :
                        DEBUG = 1
                    else:
                        DEBUG = 0
                    K = OLD_K
                elif DEBUG == 1 and K == b'p':
                    while not m.kbhit() and m.getch() != b'p':
                        pass
                    K = OLD_K
                else:
                    K = OLD_K
            N,SCORE,SPEED = ACTION(MODE,W,S,P,K,SCORE,SPEED)
            DEBUG_STRING = 'POS : '+'0'*(2-len(str(S.HEAD()[0])))+str(S.HEAD()[0])+','+'0'*(3-len(str(S.HEAD()[1])))+str(S.HEAD()[1])+' LOOK : '+'0'*(2-len(str(S.GRASP(K)[0])))+str(S.GRASP(K)[0])+','+'0'*(3-len(str(S.GRASP(K)[1])))+str(S.GRASP(K)[1])+' PREY : '+'0'*(2-len(str(str(P.GET()[0]))))+str(P.GET()[0])+','+'0'*(3-len(str(str(P.GET()[1]))))+str(P.GET()[1])+' MOVE : '+K.decode('utf-8')
            W.UPDATE(S.GET(),P.GET(),SCORE,DEBUG,DEBUG_STRING)
        else:
            N = t.perf_counter()
            A.append(N)
            if K == None :
                K = RANDOM_DIR()
                OLD_K = K
            if K == b'w' or K == b's' :
                F = 5
            else :
                F = 1
            if A[-1]-A[0]>(F/SPEED):
                N,SCORE,SPEED = ACTION(MODE,W,S,P,K,SCORE,SPEED)
                DEBUG_STRING = 'POS : '+'0'*(2-len(str(S.HEAD()[0])))+str(S.HEAD()[0])+','+'0'*(3-len(str(S.HEAD()[1])))+str(S.HEAD()[1])+' LOOK : '+'0'*(2-len(str(S.GRASP(K)[0])))+str(S.GRASP(K)[0])+','+'0'*(3-len(str(S.GRASP(K)[1])))+str(S.GRASP(K)[1])+' PREY : '+'0'*(2-len(str(str(P.GET()[0]))))+str(P.GET()[0])+','+'0'*(3-len(str(str(P.GET()[1]))))+str(P.GET()[1])+' MOVE : '+K.decode('utf-8')
                W.UPDATE(S.GET(),P.GET(),SCORE,DEBUG,DEBUG_STRING)
                del A
                A = []
    return SCORE

if __name__ == "__main__":
    NAME = 'DEBUG'
    SCORE = GAME(0)
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
    t.sleep(2)