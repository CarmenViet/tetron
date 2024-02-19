import pygame
from modules.images import *
from pprint import pprint
import random

def spawn_o(board):
    if board[0][4] == False and board[0][5] == False and board[1][4] == False and board[1][5] == False:
        board[0][4] = "current"
        board[0][5] = "current"
        board[1][4] = "current"
        board[1][5] = "current"

def spawn_i(board):
    if board[0][3] == False and board[0][4] == False and board[0][5] == False and board[0][6] == False:    
        board[0][3] = "current"
        board[0][4] = "current"
        board[0][5] = "current"
        board[0][6] = "current"

def spawn_l(board):
    if board[1][3] == False and board[1][4] == False and board[1][5] == False and board[0][5] == False:
        board[1][3] = "current"
        board[1][4] = "current"
        board[1][5] = "current"
        board[0][5] = "current"

def spawn_j(board):
    if board[1][3] == False and board[1][4] == False and board[1][5] == False and board[0][3] == False:
        board[1][3] = "current"
        board[1][4] = "current"
        board[1][5] = "current"
        board[0][3] = "current"

def spawn_z(board):
    if board[0][4] == False and board[1][3] == False and board[1][4] == False and board[2][3] == False:
        board[0][4] = "current"
        board[1][3] = "current"
        board[1][4] = "current"
        board[2][3] = "current"

def spawn_s(board):
    if board[0][3] == False and board[1][3] == False and board[1][4] == False and board[2][4] == False:
        board[0][3] = "current"
        board[1][3] = "current"
        board[1][4] = "current"
        board[2][4] = "current"

def show_game(screen, clock):
    row_amount = 20
    column_amount = 10
    board = []
    block_width = 30
    start = False
    start_time = 0
    active_piece_exists = False
    
    for rows in range(row_amount):
        row = []
        for columns in range(column_amount):
           row.append(False)
        board.append(row)
    
    while True:
        pygame.draw.rect(screen, (218, 134, 148), (0, 0, 1280, 720))
        pygame.draw.rect(screen, (163, 157, 174), (40, 250, 200, 200))
        screen.blit(bunny, (50, 260))
        pygame.draw.rect(screen, (163, 157, 174), (390, 40, 600, 620))
        pygame.draw.rect(screen, (204, 199, 213), (400, 50, 600, 620))
        for row_index in range(len(board)):
            for column_index in range(len(board[row_index])):
                pygame.draw.rect(screen, (7 * row_index + 7 * column_index, 0, 3 * row_index + 3 * column_index), (column_index * block_width + 540, row_index * block_width + 60, block_width, block_width))
        if start == False:
            screen.blit(play, (450, 150))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    sop = pygame.mouse.get_pos()
                    print(sop)
                    if 950 > sop[0] and sop[0] > 450 and 550 > sop[1] and sop[1] > 150:
                        start = True
        if start == True:
            current_time = pygame.time.get_ticks()
            if active_piece_exists == False:
                rand = random.randint(1, 6)
                if rand == 1:
                    spawn_o(board)
                elif rand == 2:
                    spawn_i(board)
                elif rand == 3:
                    spawn_l(board)
                elif rand == 4:
                    spawn_j(board)
                elif rand == 5:
                    spawn_z(board)
                elif rand == 6:
                    spawn_s(board)
                active_piece_exists = True
            # Every second, perform lowering logic 
            if current_time >= start_time + 200:
                start_time = current_time

                # Makes a list of blocks in current piece 
                current_piece_blocks = []
                for row_index in range(row_amount-1, -1, -1):
                    for column_index in range(column_amount-1, -1, -1):
                        if board[row_index][column_index] == "current":
                            current_piece_blocks.append({"row_index": row_index, "column_index": column_index})

                # Checks if current piece should lower
                should_lower = True
                for block in current_piece_blocks:
                    if block["row_index"] == row_amount - 1 or board[block["row_index"]+1][block["column_index"]] == True:
                        should_lower = False

                # Makes current piece True if it shouldn't lower
                if should_lower == False:
                    for block in current_piece_blocks:
                        board[block["row_index"]][block["column_index"]] = True
                    active_piece_exists = False
                    for row_index in range(len(board)):
                        if False not in board[row_index]:
                            del board[row_index]
                            board.insert(0, [False]*column_amount) 

                # Lowers
                elif should_lower == True:
                    for block in current_piece_blocks:
                        board[block["row_index"]+1][block["column_index"]] = "current"
                        board[block["row_index"]][block["column_index"]] = False

            # Draws in the block if its not False
            for row_index in range(row_amount):
                for column_index in range(column_amount):
                    if board[row_index][column_index] != False:
                        pygame.draw.rect(screen, (203, 150, 255), (column_index*block_width+540, row_index*block_width+60, block_width, block_width))    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # Moves block left and right
            if event.type == pygame.KEYDOWN and start == True:
                current_piece_blocks = []
                for row_index in range(row_amount-1, -1, -1):
                    for column_index in range(column_amount-1, -1, -1):
                        if board[row_index][column_index] == "current":
                            current_piece_blocks.append({"row_index": row_index, "column_index": column_index})

                if event.key == pygame.K_RIGHT:
                    can_move_right = True
                    for block in current_piece_blocks:
                        if block["column_index"] == column_amount - 1 or board[block["row_index"]][block["column_index"]+1] == True:
                            can_move_right = False
                    if can_move_right == True:
                        for block in current_piece_blocks:
                            board[block["row_index"]][block["column_index"]+1] = "current"
                            board[block["row_index"]][block["column_index"]] = False

                if event.key == pygame.K_LEFT:
                    can_move_left = True
                    for block in reversed(current_piece_blocks):
                        if block["column_index"] == 0 or board[block["row_index"]][block["column_index"]-1] == True:
                            can_move_left = False
                    if can_move_left == True:
                        for block in reversed(current_piece_blocks):
                            board[block["row_index"]][block["column_index"]-1] = "current"
                            board[block["row_index"]][block["column_index"]] = False
        if True in board[0]:
            pygame.quit()

        pygame.display.update()
        clock.tick(60)
