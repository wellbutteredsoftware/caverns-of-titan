# Caverns of Titan Room Editor
# Version: 1.0
# Author: wellbutteredsoftware
# 
# CONTROLS:
# MouseLeft  -> Place Tile
# MouseRight -> Delete Tile
# Tab        -> Swap Type
# S          -> Save to .room


import pygame
import sys

TILE_SIZE = 32
GRID_WIDTH = 25   # 800 px
GRID_HEIGHT = 19  # 608 px
WINDOW_WIDTH = TILE_SIZE * GRID_WIDTH
WINDOW_HEIGHT = TILE_SIZE * GRID_HEIGHT
FPS = 60

TILE_TYPES = ["Solid", "Ice", "Platform"]
TILE_COLORS = {
    "Solid": (100, 100, 100),
    "Ice": (0, 180, 255),
    "Platform": (200, 200, 200)
}

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Rust Room Editor")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

# Tile storage: {(grid_x, grid_y): tile_type}
tiles = {}
current_tile = "Solid"

def draw_grid():
    for x in range(0, WINDOW_WIDTH, TILE_SIZE):
        pygame.draw.line(screen, (50, 50, 50), (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, TILE_SIZE):
        pygame.draw.line(screen, (50, 50, 50), (0, y), (WINDOW_WIDTH, y))

def draw_tiles():
    for (gx, gy), ttype in tiles.items():
        rect = pygame.Rect(gx * TILE_SIZE, gy * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(screen, TILE_COLORS[ttype], rect)

def save_to_file(filename):
    with open(filename, "w") as f:
        for (gx, gy), ttype in tiles.items():
            px = gx * TILE_SIZE
            py = gy * TILE_SIZE
            f.write(f"{px} {py} {TILE_SIZE} {TILE_SIZE} {ttype}\n")
    print(f"Saved {len(tiles)} tiles to {filename}")

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_TAB:
                idx = TILE_TYPES.index(current_tile)
                current_tile = TILE_TYPES[(idx + 1) % len(TILE_TYPES)]
                print(f"Switched to {current_tile}")
            elif event.key == pygame.K_s:
                save_to_file("room.room")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            gx = mx // TILE_SIZE
            gy = my // TILE_SIZE

            if event.button == 1:
                # Left click: place
                tiles[(gx, gy)] = current_tile
            elif event.button == 3:
                # Right click: remove
                if (gx, gy) in tiles:
                    del tiles[(gx, gy)]

    # Draw
    screen.fill((0, 0, 0))
    draw_tiles()
    draw_grid()

    # Show current tile type
    txt = font.render(f"Tile: {current_tile} (TAB to change, S to save)", True, (255, 255, 255))
    screen.blit(txt, (8, 8))

    pygame.display.flip()

pygame.quit()
sys.exit()
