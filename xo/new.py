import pygame, sys

def winner(board, sign, win_length=3):
    size = len(board)

    for row in board:
        count = 0
        for cell in row:
            if cell == sign:
                count += 1
                if count == win_length:
                    return sign
            else:
                count = 0

    for col in range(size):
        count = 0
        for row in range(size):
            if board[row][col] == sign:
                count += 1
                if count == win_length:
                    return sign
            else:
                count = 0

    for x in range(size - win_length + 1):
        for y in range(size - win_length + 1):
            count = 0
            for i in range(win_length):
                if board[x + i][y + i] == sign:
                    count += 1
                    if count == win_length:
                        return sign
                else:
                    break

    for x in range(size - win_length + 1):
        for y in range(win_length - 1, size):
            count = 0
            for i in range(win_length):
                if board[x + i][y - i] == sign:
                    count += 1
                    if count == win_length:
                        return sign
                else:
                    break

    return 0


pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

def get_board_size():
    font = pygame.font.SysFont('Arial', 30)
    screen.fill(black)
    text = font.render('Enter the grid size (min 3 for 3x3):', True, white)
    text_rect = text.get_rect(center=(width // 2, height // 2 - 50))
    screen.blit(text, text_rect)
    
    pygame.display.update()

    input_active = True
    board_size = 3
    input_text = ""

    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  
                    if input_text.isdigit():
                        board_size = int(input_text)
                        if board_size < 3:
                            input_text = ""  
                            screen.fill(black)
                            text = font.render('Size must be between 3 and 9! Enter again:', True, white)
                            screen.blit(text, text_rect)
                            pygame.display.update()
                        elif board_size > 9:
                            input_text = ""  
                            screen.fill(black)
                            text = font.render('Size must be between 3 and 9 ! Enter again:', True, white)
                            screen.blit(text, text_rect)
                            pygame.display.update()
                    
                        else:
                            input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        screen.fill(black)
        screen.blit(text, text_rect)

        input_box = pygame.Rect(width // 2 - 50, height // 2 , 100, 32)
        pygame.draw.rect(screen, white, input_box, 2)
        input_surface = font.render(input_text, True, white)
        screen.blit(input_surface, (input_box.x + 40, input_box.y -2))

        pygame.display.update()
        pygame.time.wait(100)

    return board_size



size_block = 100
margin = 10
width = height = size_block * 5 + margin * 6

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("XO")

board_size = get_board_size()

width = height = size_block * board_size + margin * (board_size + 1)
screen = pygame.display.set_mode((width, height))

board = [[0] * board_size for _ in range(board_size)]
player = 1
hod = 0
Find_winner = False
stop = False
win_length = 3

while not Find_winner:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            Find_winner = True
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN and not stop:
            x, y = pygame.mouse.get_pos()
            col = x // (size_block + margin)
            row = y // (size_block + margin)
            if board[row][col] != 0:
                continue
            if player == 1:
                board[row][col] = 'x'
                player = 2
                hod += 1
            else:
                board[row][col] = 'o'
                player = 1
                hod += 1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                stop = False
                hod = 0
                player = 1
                board = [[0] * board_size for _ in range(board_size)]
                screen.fill(black)

    if not stop:
        for row in range(board_size):
            for col in range(board_size):
                if board[row][col] == 'x':
                    color = red
                elif board[row][col] == 'o':
                    color = blue
                else:
                    color = white
                x = col * size_block + (col + 1) * margin
                y = row * size_block + (row + 1) * margin
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == red:
                    pygame.draw.line(screen, black, (x, y), (x + size_block, y + size_block), 5)
                    pygame.draw.line(screen, black, (x + size_block, y), (x, y + size_block), 5)
                elif color == blue:
                    pygame.draw.circle(screen, white, (x + size_block // 2, y + size_block // 2), size_block // 2, 5)

    if player == 1:
        game_over = winner(board, 'o', win_length)
        if game_over == 0 and hod == board_size * board_size:
            game_over = 'x and o'

    else:
        game_over = winner(board, 'x', win_length)
        if game_over == 0 and hod == board_size * board_size:
            game_over = 'x and o'

    if game_over:
        screen.fill(black)
        font = pygame.font.SysFont('Arial', 30)
        text = font.render(f'Player {game_over} wins!', True, white)
        text_rect = text.get_rect()
        x = screen.get_width() // 2 - text_rect.width // 2
        y = screen.get_height() // 2 - text_rect.height // 2
        screen.blit(text, (x, y))
    pygame.display.update()

pygame.quit()
