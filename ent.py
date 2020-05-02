# Importing necessary modules
import os
import random

# Debugging is still not implemented
# Yet Debugging is made possible manually
# global DEBUG_MODE


# Main Entity classes

class window:
    """
        Creates a Winodw to work in with border defined. Height = 28 and Width = 120
         
        \nMethods :\n
        \nGET ( ) --> SCREEN as List(Strings)
        Returns the screen as a nested list of strings
        Callable as RETVAL [I] [J] where I<25 and J <118
        \nUPDATE ( SNAKE , PREY , *ARGS ) --> None
        SNAKE = List of Tuples with 2 values
        PREY = A tuple with 2 Values
        Updates the SCREEN with positions of SNAKE and PREY
        The next variable i.e, ARGS[1] must be the SCORE
        The ARGS[2] is the DEBUG_MODE variable.
        If made True or 1 the next ARGS will be printed out too
        \nHIT_BOUND ( CORD ) --> True or False
        CORD = A Tuple with 2 values
        Checks whether the coordinate CORD is a BOUNDARY in
        SCREEN or not. 
    """
    def __init__(self):
        __L = 118
        __W = 25
        __M = ['║'+' '*__L+'║']*__W
        __SCR = ['╔'+'═'*__L+'╗']
        __SCR.extend(__M)
        __SCR.extend(['╚'+'═'*__L+'╝'])
        self.__SCREEN = __SCR.copy()
        self.__BOUND = []
        for I in range(len(self.__SCREEN)) :
            for J in range(len(self.__SCREEN[I])):
                if self.__SCREEN[I][J] != ' ' :
                    self.__BOUND.append((I,J))
        if os.name == 'nt' :
            os.system('mode con cols=120 lines=30')
            os.system('cls')
        else:
            os.system('clear')
            print('\n Sorry, This Script cannot control terminal size.\n Please rsize your terminal to Rows or Height = 30 and Cols or Width = 120.\n\n Then press enter to continue ....')
            _ = input()
    
    def GET(self):
        """
        GET ( ) --> SCREEN as List(Strings)
        \nReturns the screen as a nested list of strings
        \nCallable as RETVAL [I] [J] where I<25 and J <118
        """
        return self.__SCREEN
    
    def __DRAW(self,*ARGS):

        if os.name == 'nt' :
            os.system('cls')
        else:
            os.system('clear')
        if len(ARGS)>1:
            __SCORE = 'SCORE '+'0'*(6-len(str(ARGS[1])))+str(ARGS[1])
            print(' '*(118-len(__SCORE))+__SCORE)
        for __I in ARGS[0]:
            print(__I)
        if len(ARGS)>2 and ARGS[2] :
            for __K in ARGS[3:]:
                print(__K,end=' ')
            print('\n',end='')

    def UPDATE(self,__SNAKE,__PREY,*ARGS):
        """
        UPDATE ( SNAKE , PREY , *ARGS ) --> None
        \nSNAKE = List of Tuples with 2 values
        \nPREY = A tuple with 2 Values
        Updates the SCREEN with positions of SNAKE and PREY
        The next variable i.e, ARGS[1] must be the SCORE
        The ARGS[2] is the DEBUG_MODE variable.
        """
        __T_SCREEN = []
        for __I in range(len(self.__SCREEN)):
            __T_SCV = ''
            for __J in range(len(self.__SCREEN[__I])):
                if (__I,__J) in __SNAKE or (__I,__J) == __PREY :
                    if (__I,__J) in __SNAKE :
                        __T_SCV += '█'
                    else:
                        __T_SCV += '♦'
                else:
                    __T_SCV += self.__SCREEN[__I][__J]
            __T_SCREEN.append(__T_SCV)
        self.__DRAW(__T_SCREEN,*ARGS)

        
    def HIT_BOUND(self,__CORD):
        """
        HIT_BOUND ( CORD ) --> True or False
        \nCORD = A Tuple with 2 values
        Checks whether the coordinate CORD is a BOUNDARY in
        SCREEN or not.
        """
        if __CORD in self.__BOUND :
            return 1
        else:
            return 0

class snake:

    def __init__(self,SCREEN):
        self.__SCREEN = SCREEN
        __X = random.randint(4,len(self.__SCREEN)-5)
        __Y = random.randint(4,len(self.__SCREEN[0])-5)
        __D = random.randint(1,4)
        __SNAKE=[]
        __SNAKE.append((__X,__Y))
        if __D == 1:
            for _ in range(3):
                __Y-=1
                __SNAKE.append((__X,__Y))
        elif __D == 2:
            for _ in range(3):
                __Y+=1
                __SNAKE.append((__X,__Y))
        elif __D == 3:
            for _ in range(3):
                __X+=1
                __SNAKE.append((__X,__Y))
        else:
            for _ in range(3):
                __X-=1
                __SNAKE.append((__X,__Y))
        self.__SNAKE = __SNAKE

    def HEAD(self):
        return self.__SNAKE[-1]

    def GRASP(self,__DIR):
        if __DIR == b'w':
            return (self.__SNAKE[-1][0]-1,self.__SNAKE[-1][1])
        elif __DIR == b'a':
            return (self.__SNAKE[-1][0],self.__SNAKE[-1][1]-1)
        elif __DIR == b's':
            return (self.__SNAKE[-1][0]+1,self.__SNAKE[-1][1])
        elif __DIR == b'd':
            return (self.__SNAKE[-1][0],self.__SNAKE[-1][1]+1)
    
    def EAT(self,__DIR):
        self.__SNAKE.append(__DIR)
        return self.__SNAKE        

    def MOVE(self,__DIR):
        if __DIR == b'w':
            self.__SNAKE.append((self.__SNAKE[-1][0]-1,self.__SNAKE[-1][1]))
            del self.__SNAKE[0]
        elif __DIR == b'a':
            self.__SNAKE.append((self.__SNAKE[-1][0],self.__SNAKE[-1][1]-1))
            del self.__SNAKE[0]
        elif __DIR == b's':
            self.__SNAKE.append((self.__SNAKE[-1][0]+1,self.__SNAKE[-1][1]))
            del self.__SNAKE[0]
        elif __DIR == b'd':
            self.__SNAKE.append((self.__SNAKE[-1][0],self.__SNAKE[-1][1]+1))
            del self.__SNAKE[0]

    def JUMP(self,__DIR):
        if __DIR == b'w':
            self.__SNAKE.append((self.__SNAKE[-1][0]+24,self.__SNAKE[-1][1]))
            del self.__SNAKE[0]
        elif __DIR == b'a':
            self.__SNAKE.append((self.__SNAKE[-1][0],self.__SNAKE[-1][1]+117))
            del self.__SNAKE[0]
        elif __DIR == b's':
            self.__SNAKE.append((self.__SNAKE[-1][0]-24,self.__SNAKE[-1][1]))
            del self.__SNAKE[0]
        elif __DIR == b'd':
            self.__SNAKE.append((self.__SNAKE[-1][0],self.__SNAKE[-1][1]-117))
            del self.__SNAKE[0]

    def JUMP_GRASP(self,__DIR):
        if __DIR == b'w':
            return (self.__SNAKE[-1][0]+24,self.__SNAKE[-1][1])
        elif __DIR == b'a':
            return (self.__SNAKE[-1][0],self.__SNAKE[-1][1]+117)
        elif __DIR == b's':
            return (self.__SNAKE[-1][0]-24,self.__SNAKE[-1][1])
        elif __DIR == b'd':
            return (self.__SNAKE[-1][0],self.__SNAKE[-1][1]-117)

    def GET(self):
        return self.__SNAKE

class prey:
    def __init__(self,__SCREEN):
        self.__SCREEN = __SCREEN
        __X = random.randint(1,len(self.__SCREEN)-2)
        __Y = random.randint(1,len(self.__SCREEN[0])-2)
        while self.__SCREEN[__X] [__Y] != ' ':
            __X = random.randint(1,len(self.__SCREEN)-2)
            __Y = random.randint(1,len(self.__SCREEN[0])-2)
        self.__PREY = (__X,__Y)

    def RESPAWN(self):
        __X = random.randint(1,len(self.__SCREEN)-2)
        __Y = random.randint(1,len(self.__SCREEN[0])-2)
        while self.__SCREEN[__X] [__Y] != ' ':
            __X = random.randint(1,len(self.__SCREEN)-2)
            __Y = random.randint(1,len(self.__SCREEN[0])-2)
        self.__PREY = (__X,__Y)

    def GET(self):
        return self.__PREY

if __name__ == "__main__":
    w = window()
    SCR = w.GET()
    s = snake(SCR)
    p = prey(SCR)
    T_SET = []
    T_NAME = ['SNAKE_LENGTH','PREY_LENGTH']
    if len(s.GET()) != 4 :
        T_SET.append(False)
    else:
        T_SET.append(True)
    if len(p.GET()) != 2 :
        T_SET.append(False)
    else:
        T_SET.append(True)
    os.system('cls')
    for I,J in zip(T_NAME,T_SET):
        print(I,end='')
        print('.'*(18-len(I)),end='')
        if J :
            print('OK',end='\n')
        else:
            print('Error',end='\n')
    _ = input()