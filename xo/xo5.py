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


size_block = 100
margin = 10
width = height = size_block * 5 + margin * 6

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("XO")

board = [[0]*5 for _ in range(5)]
player = 1 
hod = 0
Find_winner = False
stop = False

while not Find_winner :
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
                board = [[0]*5 for _ in range(5)]
                screen.fill(black)

            

    if not stop:
        for row in range(5):
            for col in range(5):
                if board[row][col] == 'x':
                    color = red
                elif board[row][col] == 'o':
                    color = blue
                else:
                    color = white
                x = col *size_block + (col + 1) * margin
                y = row *size_block + (row + 1) * margin
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == red:
                    pygame.draw.line(screen, black, (x, y ), (x + size_block, y + size_block ), 5)
                    pygame.draw.line(screen, black, (x + size_block, y), (x, y + size_block  ), 5)
                elif color == blue:
                    pygame.draw.circle(screen, white, (x + size_block // 2, y + size_block // 2), size_block // 2, 5)
    if player == 1:
        game_over = winner(board, 'o')
        if game_over == 0 and hod == 25:
            game_over = 'x and o'
            
    else:
        game_over = winner(board, 'x')
        if game_over == 0 and hod == 25:
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