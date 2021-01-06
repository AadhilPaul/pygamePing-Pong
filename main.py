import pygame
import sys

# Intializing pygame
pygame.init()

# Screen
WIDTH, HEIGHT = 1000, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
CAPTION = "Ping Pong"
pygame.display.set_caption(CAPTION)


# colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

# GLOBAL VARIABLES
# gap
gap = 10
# define borders
right_border = ((gap, gap), (gap, HEIGHT - gap))
left_border =  ((WIDTH - gap, gap), (WIDTH - gap, HEIGHT - gap))
bottom_border = ((gap, HEIGHT - gap), (WIDTH - gap, HEIGHT - gap))
top_border = ((gap, gap), (WIDTH - gap, gap))
# player size
player_width = 30
player_height = 70
# player positions
player1_pos_x = right_border[0][0] + gap
player1_pos_y = right_border[0][1] + HEIGHT / 2
player2_pos_x = left_border[0][0] - player_width - gap
player2_pos_y =  left_border[0][1] + HEIGHT / 2
# player scores
player1_score = 0
player2_score = 0
# fonts 
SCORE_FONT = pygame.font.SysFont("comicsans", 45)
WIN_FONT = pygame.font.SysFont("comicsans", 60)
# ball
ball_width = 20
ball_height = 20
ball_vel = [5, 5]
ball_pos_x = (top_border[1][0] - top_border[0][0]) / 2 - ball_width
ball_pos_y = (HEIGHT - 20) / 2
ball_top = ball_pos_y
ball_bottom = ball_pos_y + ball_height
ball_right = ball_pos_x
ball_left = ball_pos_x + ball_width
# player velocity
player_velocity = 9



def draw_border(surface):
    # draw the border
    pygame.draw.line(surface, WHITE, right_border[0], right_border[1]) # right border
    pygame.draw.line(surface, WHITE, top_border[0], top_border[1]) # top border
    pygame.draw.line(surface, WHITE, left_border[0], left_border[1]) # left border
    pygame.draw.line(surface, WHITE, bottom_border[0], bottom_border[1]) # bottom border
    

def draw_players(surface, pos_x, pos_y):
    player1 = pygame.draw.rect(surface, WHITE, (pos_x, pos_y, player_width, player_height))
    player2 = pygame.draw.rect(surface, WHITE, (pos_x, pos_y, player_width, player_height))


def draw_middle(surface):
    start_middle_position = top_border[0][1] 
    middle_position = (top_border[1][0] - top_border[0][0]) / 2
    end_middle_position = bottom_border[0][1]
    black_spots_range = bottom_border[0][1] - top_border[0][1] + 5
    pygame.draw.line(surface, WHITE, (middle_position, start_middle_position), (middle_position, end_middle_position))
    for i in range(10, int(black_spots_range)):
        if i % 10 == 0:
            j = i
        pygame.draw.rect(surface, BLACK, (middle_position, j, 10, 5))

def draw_ball(surface, pos_x, pos_y, width, height):
    pygame.draw.rect(surface, GREEN, (pos_x, pos_y, width, height))

def display_scores(surface):
    # display scores
    score1_text = SCORE_FONT.render(f"Player 1: {str(player1_score)}", 1, WHITE)
    score2_text = SCORE_FONT.render(f"Player 2: {str(player2_score)}",  1, WHITE)
    surface.blit(score1_text, (right_border[0][0] + 50, right_border[0][1] + 20))
    surface.blit(score2_text, (left_border[0][0] - score1_text.get_width() - 50, left_border[0][1] + 20))

def tie(surface):
    tie_text = WIN_FONT.render(f"Tie.",  1, WHITE)
    surface.blit(tie_text, (WIDTH / 2 - (tie_text.get_width() / 2), (HEIGHT / 2 - (tie_text.get_height() / 2))))
    pygame.display.update()
    pygame.time.delay(2500)

def display_winner(surface, player, player_score):
    global top_border, player1_score, player2_score

    win_text = WIN_FONT.render(f"{str(player)} Won!!",  1, WHITE)
    score_win_text = SCORE_FONT.render(f"Score: {str(player_score)}", 1, WHITE)
    surface.blit(win_text, (WIDTH / 2 - (win_text.get_width() / 2), (HEIGHT / 2 - (win_text.get_height() / 2))))
    surface.blit(score_win_text, (WIDTH / 2 - (win_text.get_width() / 3) + 25, (HEIGHT / 2 - (score_win_text.get_height() / 2) + win_text.get_height() + 10)))
    pygame.display.update()
    pygame.time.delay(2500)

# Redraw game window fuunction
def DrawGameWindow(surface):

    # fill screen with black
    surface.fill(BLACK)
    # draw players
    draw_players(surface, player1_pos_x, player1_pos_y)
    draw_players(surface, player2_pos_x, player2_pos_y)
    # draw middle
    draw_middle(surface)
    # draw border
    draw_border(surface)
    # draw ball
    draw_ball(surface, ball_pos_x, ball_pos_y, ball_width, ball_height)
    # display scores
    display_scores(surface)
    # update the screen
    pygame.display.update()


# Main Loop
def main(surface):
    global player1_pos_y, player2_pos_y, ball_pos_x, ball_pos_y, ball_width, ball_vel, player1_score, player2_score, score1_text, score2_text

    run = True
    clock = pygame.time.Clock()
    FPS = 60
    
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                surface.fill(BLACK)
                if player1_score > player2_score:
                    display_winner(surface, "Player 1", player1_score)
                elif player1_score == player2_score:
                    tie(surface)
                else:
                    display_winner(surface, "Player 2", player2_score)
                run = False
                sys.exit()

        # define keys
        keys = pygame.key.get_pressed()

        # if user press down
        if keys[pygame.K_DOWN] and player2_pos_y < bottom_border[0][1] - player_height - gap:
            player2_pos_y += player_velocity

        if keys[pygame.K_UP] and player2_pos_y > top_border[0][1] + gap:
            player2_pos_y -= player_velocity

        # if user press w
        if keys[pygame.K_w] and player1_pos_y > top_border[0][1] + gap:
            player1_pos_y -= player_velocity

        # if user press s
        if keys[pygame.K_s] and player1_pos_y < bottom_border[0][1] - player_height - gap:
            player1_pos_y += player_velocity

        # ball controls
        ball_pos_x += ball_vel[0]
        ball_pos_y += ball_vel[1]


        # if ball hit right border
        if ball_pos_x + ball_width >= left_border[0][0] - gap:
            ball_pos_x = (top_border[1][0] - top_border[0][0]) / 2 - ball_width
            ball_pos_y = (HEIGHT - 20) / 2
            player2_pos_y = (HEIGHT - 20) / 2
            player1_pos_y = (HEIGHT - 20) / 2
            pygame.time.delay(500)
            player1_score += 1
            print(f"Player 1 has scored \n player 1 score: {player1_score}")


        # if ball left border
        if ball_pos_x <= right_border[0][0] + gap:
            ball_pos_x = (top_border[1][0] - top_border[0][0]) / 2 - ball_width
            ball_pos_y = (HEIGHT - 20) / 2
            player2_pos_y = (HEIGHT - 20) / 2
            player1_pos_y = (HEIGHT - 20) / 2
            pygame.time.delay(500)
            player2_score += 1
            print(f"Player 2 has scored \n player 2 score: {player2_score}")

        # if ball hit bottom border
        if ball_pos_y + ball_height >= bottom_border[0][1] - gap:
            ball_vel[1] *= -1
        
        # if ball hit top border
        if ball_pos_y <= top_border[0][1] + gap:
            ball_vel[1] *= -1

        # if ball hit player2
        if ball_pos_y >= player2_pos_y and ball_pos_y < player2_pos_y + player_height and ball_pos_x + ball_width >= player2_pos_x:
            ball_vel[0] *= -1

        # if ball hit player1
        elif ball_pos_y >= player1_pos_y and ball_pos_y < player1_pos_y + player_height and ball_pos_x <= player1_pos_x + player_width:
            ball_vel[0] *= -1


        DrawGameWindow(surface)
        
        
main(WIN)
pygame.quit()

