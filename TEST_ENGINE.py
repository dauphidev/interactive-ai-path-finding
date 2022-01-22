import pygame, math, random

from TEST_UCS import *

def redraw_game_window():
    window.fill((195,181,181))
    paint_cells()
    draw_grid()
    pygame.display.update()

def draw_grid():
    for i in range(0,map_size[0]):
       for j in range(0,map_size[1]):
           draw_cell((i,j), (255,255,255), filled=False)

def draw_cell(raw_pos, color, filled=True):
    if filled:
        pygame.draw.rect(window, color, pygame.Rect((raw_pos[0]*CELL_SIZE,raw_pos[1]*CELL_SIZE), (CELL_SIZE, CELL_SIZE)))
    else:
        pygame.draw.rect(window, color, pygame.Rect((raw_pos[0]*CELL_SIZE,raw_pos[1]*CELL_SIZE), (CELL_SIZE, CELL_SIZE)), width = 1)

def translate (pos):
    i,j = pos
    new_pos = (i//CELL_SIZE, j//CELL_SIZE)
    print(new_pos)
    return new_pos
    
# ----------------------- "main" ----------------------- #
  
pygame.init()


SCREEN_WIDTH = 500
SCREEN_HEIGHT  = 500

window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

map_size = (25,25)

CELL_SIZE = SCREEN_WIDTH // map_size[0] # we assume that map_size width == height

obstacles = []
start = (3,12)
goal = (20,12)

prob = MapProblem(map_size[0],map_size[1],obstacles, goal)

solution = None

draw_mode = True
finished_searching = False

run = True

def paint_cells ():
    
    for i in range(0,map_size[0]):
        for j in range(0,map_size[1]):
            pos = (i,j)
            if not draw_mode:
                if (i,j) in prob.visited:
                    draw_cell(pos, (218,178,85))
                if finished_searching:
                    if (i,j) in solution.path:
                        draw_cell(pos, (196,71,46))
            if pos == goal:
                draw_cell(pos, (74,114,209))
            elif (i,j) == start:
                draw_cell(pos, (91,139,91))
            elif (i,j) in obstacles:
                    draw_cell(pos, (0,0,0))
            

while run:

    pygame.time.delay(20)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False
            
    mouse = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    
    left_click_pressed = mouse[0]
    right_click_pressed = mouse[2]
    middle_click_pressed = mouse[1]

    if draw_mode:
        if left_click_pressed:
            obstacles.append(translate(mouse_pos))
        elif right_click_pressed:
            prob.obstacles = obstacles
            prob.start(start)
            draw_mode = False
            
    elif finished_searching == False:
        s = prob.next_iteration()
        if s != Point((-1,-1)):
            solution = s
            print(s)
            finished_searching = True
            
            
    if middle_click_pressed:
        obstacles = []
        draw_mode = True

    
    redraw_game_window()


pygame.quit()

# TODO:
# if draw_mode ... handle_left_click(mouse_pos) -> implementar mudar start/goal de posicao, e limpar obstacles individuais
# if middle_click ... reset (isto ja esta bem)

# aumentar tamanho de janela, manter map size efetivo (mudar antigo SCREEN_WIDTH/HEIGHT para MAP_WIDTH/HEIGHT)
# adionar botoes de lado para mudar de algoritmo e dar reset (em vez de middle click)
# mostrar mensagem de lado quando nao existe solucao

# dar fix a diagonais bugadas
# Adicionar titulo a janela


                

