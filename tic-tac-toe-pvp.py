import pygame
import os
import random
pygame.font.init()

FPS = 60
WHITE = (255,255,255)
BLACK = (0,0,0)
WIDTH,HEIGHT = 800,500
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))

s1 = 0
s2 = 0
score_font = pygame.font.SysFont('Trebuchet MS',50)
winner_font = pygame.font.SysFont('Trebuchet MS',40)

xo_board_image = pygame.image.load(os.path.join('Assets', 'XO.png'))
xo_board = pygame.transform.scale(xo_board_image,(WIDTH,HEIGHT))

O_image = pygame.image.load(os.path.join('Assets', 'O.png'))
O = pygame.transform.scale(O_image,(100,100))
X_image = pygame.image.load(os.path.join('Assets', 'X.png'))
X = pygame.transform.scale(X_image,(100,100))

def winner(m):
    for row in range(3):
        if m[row][0] == m[row][1] == m[row][2] == 'X' or m[0][row] == m[1][row] == m[2][row] == 'X': return 'X'
        elif m[row][0] == m[row][1] == m[row][2] == 'O' or m[0][row] == m[1][row] == m[2][row] == 'O': return 'O'
    if m[0][0] == m[1][1] == m[2][2] == 'X' or m[0][-1] == m[1][-2] == m[2][-3] == 'X': return 'X'
    elif m[0][0] == m[1][1] == m[2][2] == 'O' or m[0][-1] == m[1][-2] == m[2][-3] == 'O': return 'O'
    else: return ''


def drawing_the_screen(draw_X,draw_O,s1,s2):

        SCREEN.fill(WHITE)
        SCREEN.blit(xo_board,(0,0))

        for i in draw_X:
            SCREEN.blit(X,i)

        for i in draw_O:
            SCREEN.blit(O,i)

        score_player_1_text = score_font.render(str(s1),1,BLACK)
        SCREEN.blit(score_player_1_text,(85,100))  

        score_player_2_text = score_font.render(str(s2),1,BLACK)
        SCREEN.blit(score_player_2_text,(685,100))                  
            
        #SCREEN.blit(X,(220,70))
        pygame.display.update()    

def player1_turn(run,draw_X,draw_O,d,m,s1,s2):
    hm = 0
    while hm == 0:
        unplayed = []
        for value in d.values():
            if value == 0: unplayed.append(value)

        if len(unplayed) == 0:
            hm += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_7 and d[(0,0)] == 0:
                    draw_X.append((220,70))
                    d[(0,0)] = 1
                    m[0][0] = 'X'
                    hm += 1
                    
                if event.key == pygame.K_KP_8 and d[(0,1)] == 0:
                    draw_X.append((353,70))
                    d[(0,1)] = 1
                    m[0][1] = 'X'
                    hm += 1

                if event.key == pygame.K_KP_9 and d[(0,2)] == 0:
                    draw_X.append((486,70))
                    d[(0,2)] = 1
                    m[0][2] = 'X'
                    hm += 1

                if event.key == pygame.K_KP_4 and d[(1,0)] == 0:
                    draw_X.append((220,203))
                    d[(1,0)] = 1
                    m[1][0] = 'X'
                    hm += 1
                    
                if event.key == pygame.K_KP_5 and d[(1,1)] == 0:
                    draw_X.append((353,203))
                    d[(1,1)] = 1
                    m[1][1] = 'X'
                    hm += 1

                if event.key == pygame.K_KP_6 and d[(1,2)] == 0:
                    draw_X.append((486,203))
                    d[(1,2)] = 1
                    m[1][2] = 'X'
                    hm += 1

                if event.key == pygame.K_KP_1 and d[(2,0)] == 0:
                    draw_X.append((220,337))
                    d[(2,0)] = 1
                    m[2][0] = 'X'
                    hm += 1
                    
                if event.key == pygame.K_KP_2 and d[(2,1)] == 0:
                    draw_X.append((353,337))
                    d[(2,1)] = 1
                    m[2][1] = 'X'
                    hm += 1

                if event.key == pygame.K_KP_3 and d[(2,2)] == 0:
                    draw_X.append((486,337))
                    d[(2,2)] = 1
                    m[2][2] = 'X'
                    hm += 1    
        drawing_the_screen(draw_X,draw_O,s1,s2) 

def player2_turn(run,draw_X,draw_O,d,m,s1,s2):
    hm = 0
    while hm == 0:
        unplayed = []
        for value in d.values():
            if value == 0: unplayed.append(value)

        if len(unplayed) == 0:
            hm += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_7 and d[(0,0)] == 0:
                    draw_O.append((220,70))
                    d[(0,0)] = 1
                    m[0][0] = '0'
                    hm += 1
                    
                if event.key == pygame.K_KP_8 and d[(0,1)] == 0:
                    draw_O.append((353,70))
                    d[(0,1)] = 1
                    m[0][1] = 'O'
                    hm += 1

                if event.key == pygame.K_KP_9 and d[(0,2)] == 0:
                    draw_O.append((486,70))
                    d[(0,2)] = 1
                    m[0][2] = 'O'
                    hm += 1

                if event.key == pygame.K_KP_4 and d[(1,0)] == 0:
                    draw_O.append((220,203))
                    d[(1,0)] = 1
                    m[1][0] = 'O'
                    hm += 1
                    
                if event.key == pygame.K_KP_5 and d[(1,1)] == 0:
                    draw_O.append((353,203))
                    d[(1,1)] = 1
                    m[1][1] = 'O'
                    hm += 1

                if event.key == pygame.K_KP_6 and d[(1,2)] == 0:
                    draw_O.append((486,203))
                    d[(1,2)] = 1
                    m[1][2] = 'O'
                    hm += 1

                if event.key == pygame.K_KP_1 and d[(2,0)] == 0:
                    draw_O.append((220,337))
                    d[(2,0)] = 1
                    m[2][0] = 'O'
                    hm += 1
                    
                if event.key == pygame.K_KP_2 and d[(2,1)] == 0:
                    draw_O.append((353,337))
                    d[(2,1)] = 1
                    m[2][1] = 'O'
                    hm += 1

                if event.key == pygame.K_KP_3 and d[(2,2)] == 0:
                    draw_O.append((486,337))
                    d[(2,2)] = 1
                    m[2][2] = 'O'
                    hm += 1    
        drawing_the_screen(draw_X,draw_O,s1,s2)                   
                   
   

def print_winner(m):
    if winner(m) == 'X':
        winner_text = winner_font.render('!!X Wins!!',1,BLACK)
        SCREEN.blit(winner_text,(15,350))
        pygame.display.update()
        pygame.time.delay(2000)

    if winner(m) == 'O':
        winner_text = winner_font.render('!!O Wins!!',1,BLACK)
        SCREEN.blit(winner_text,(615,350))
        pygame.display.update()
        pygame.time.delay(2000)        

def main(s1,s2):

    m = [['-','-','-'], ['-','-','-'], ['-','-','-']]
    d = {(0,0): 0, (0,1): 0, (0,2): 0, (1,0): 0, (1,1): 0, (1,2): 0, (2,0): 0, (2,1): 0, (2,2): 0}

    draw_X = []
    draw_O = []
    run = True

    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        player1_turn(run,draw_X,draw_O,d,m,s1,s2)
        if winner(m) == 'X':
            s1 += 1
            print_winner(m) 
            break   

        player2_turn(run,draw_X,draw_O,d,m,s1,s2)
        if winner(m) == 'O':
            s2 += 1
            drawing_the_screen(draw_X,draw_O,s1,s2)
            print_winner(m)
            break  

        for i in d.values():
            if i == 0: break
        else:
            s1 += 1
            s2 += 1
            break           
            
        drawing_the_screen(draw_X,draw_O,s1,s2)

    main(s1,s2)    

main(s1,s2)
