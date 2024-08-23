import pygame as pg
import random
import asyncio
import sys

# Initialize Pygame
pg.init()

# CONSTANTS
# Screen dimensions
BLOCK_SIZE = 30
GRID_WIDTH, GRID_HEIGHT = 10, 20
SW, SH = GRID_WIDTH * BLOCK_SIZE + 200, GRID_HEIGHT * BLOCK_SIZE  # Extra space for scoring

# Tetromino colors & shapes
COLORS = {
    'I': (0, 255, 255),
    'O': (255, 255, 0),
    'T': (128, 0, 128),
    'S': (0, 255, 0),
    'Z': (255, 0, 0),
    'J': (0, 0, 255),
    'L': (255, 165, 0)
}

SHAPES = {
    'I': [['0000',
           '1111',
           '0000',
           '0000'],
          ['0010',
           '0010',
           '0010',
           '0010']],
    'O': [['0110',
           '0110']],
    'T': [['010',
           '111',
           '000'],
          ['010',
           '011',
           '010'],
          ['000',
           '111',
           '010'],
          ['010',
           '110',
           '010']],
    'S': [['011',
           '110',
           '000'],
          ['010',
           '011',
           '001']],
    'Z': [['110',
           '011',
           '000'],
          ['001',
           '011',
           '010']],
    'J': [['100',
           '111',
           '000'],
          ['011',
           '010',
           '010'],
          ['000',
           '111',
           '001'],
          ['010',
           '010',
           '110']],
    'L': [['001',
           '111',
           '000'],
          ['010',
           '010',
           '011'],
          ['000',
           '111',
           '100'],
          ['110',
           '010',
           '010']]
}

try:
    FONT = pg.font.Font("font.ttf", BLOCK_SIZE)
except FileNotFoundError:
    print("Font file not found. Please check the path.")
    sys.exit()

playfield = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Set up display
screen = pg.display.set_mode((SW, SH))
pg.display.set_caption("Tetris")
clock = pg.time.Clock()

class tetris_blocks:
    # constructor
    def __init__(self, block_size, x, y, shape, color):
        self.block_size = block_size
        self.shape = random.choice(list(SHAPES.keys()))
        self.color = color
        self.x = (GRID_WIDTH // 2 - 1) * block_size
        self.y = 0
        self.rotation = 0

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(SHAPES[self.shape])

    def move_left(self):
        self.x -= self.block_size

    def move_right(self):
        self.x += self.block_size

    def move_down(self):
        self.y -= self.block_size

    def draw(self, screen):
        shape = SHAPES[self.shape][self.rotation]
        for i, row in enumerate(shape):
            for j, cell in enumerate(row):
                if cell == '1':
                    pg.draw.rect(screen, self.color, (self.x + j * self.block_size, self.y + i * self.block_size, self.block_size, self.block_size))

def draw_grid() -> None:
    for x in range(0, GRID_WIDTH * BLOCK_SIZE, BLOCK_SIZE):
        for y in range(0, GRID_HEIGHT * BLOCK_SIZE, BLOCK_SIZE):
            rect = pg.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pg.draw.rect(screen, (60, 60, 59), rect, 1)

def draw_info(score: int, level: int, lines: int) -> None:
    score_text = FONT.render(f"SCORE: {score}", True, (255, 255, 255))
    level_text = FONT.render(f"LEVEL: {level}", True, (255, 255, 255))
    lines_text = FONT.render(f"LINES: {lines}", True, (255, 255, 255))
    screen.blit(score_text, (GRID_WIDTH * BLOCK_SIZE + 20, 20))
    screen.blit(level_text, (GRID_WIDTH * BLOCK_SIZE + 20, 60))
    screen.blit(lines_text, (GRID_WIDTH * BLOCK_SIZE + 20, 100))

def line_cleared(lines_cleared: str,level: int) -> int :
    points_dictionary = {
        "single": 100,
        "double": 300,
        "triple": 500,
        "tetris": 800,
    }
    
    return points_dictionary[lines_cleared] * level

async def main() -> None:
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        screen.fill((0, 0, 0))  # Clear the screen
        draw_grid()  # Draw the grid
        draw_info(score=0, level=0, lines=0)  # Draw the scoring and level info at 0

        pg.display.update()
        await asyncio.sleep(0)

# Run the main function
asyncio.run(main())
