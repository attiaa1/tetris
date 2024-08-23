import pygame as pg
import asyncio
import sys

# Initialize Pygame
pg.init()

# Screen dimensions
BLOCK_SIZE = 30
GRID_WIDTH, GRID_HEIGHT = 10, 20
SW, SH = GRID_WIDTH * BLOCK_SIZE + 200, GRID_HEIGHT * BLOCK_SIZE  # Extra space for scoring

# Load font
try:
    FONT = pg.font.Font("font.ttf", BLOCK_SIZE)
except FileNotFoundError:
    print("Font file not found. Please check the path.")
    sys.exit()

# Set up display
screen = pg.display.set_mode((SW, SH))
pg.display.set_caption("Tetris")
clock = pg.time.Clock()

class TetrisBlock:
    def __init__(self) -> None:
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.x_dir = 0
        self.y_dir = -1

def draw_grid() -> None:
    for x in range(0, GRID_WIDTH * BLOCK_SIZE, BLOCK_SIZE):
        for y in range(0, GRID_HEIGHT * BLOCK_SIZE, BLOCK_SIZE):
            rect = pg.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pg.draw.rect(screen, (60, 60, 59), rect, 1)

def draw_info(score: int, level: int) -> None:
    score_text = FONT.render(f"Score: {score}", True, (255, 255, 255))
    level_text = FONT.render(f"Level: {level}", True, (255, 255, 255))
    screen.blit(score_text, (GRID_WIDTH * BLOCK_SIZE + 20, 20))
    screen.blit(level_text, (GRID_WIDTH * BLOCK_SIZE + 20, 60))

async def main() -> None:
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        screen.fill((0, 0, 0))  # Clear the screen
        draw_grid()  # Draw the grid
        draw_info(score=0, level=0)  # Draw the scoring and level info

        pg.display.update()
        await asyncio.sleep(0)

# Run the main function
asyncio.run(main())

