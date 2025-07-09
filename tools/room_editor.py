# Caverns of Titan Room Editor
# Version: 2.0
# Author: wellbutteredsoftware
# 
# CONTROLS:
# MouseLeft  -> Place Tile
# MouseRight -> Delete Tile
# Tab        -> Swap Type
# S          -> Save to .trm
#
# TODOS:
# * Add file reading
# * GUI improvements

import pygame
import sys
import toml

TILE_SIZE = 32
GRID_WIDTH = 25   # 800 px
GRID_HEIGHT = 19  # 608 px
WINDOW_WIDTH = TILE_SIZE * GRID_WIDTH
WINDOW_HEIGHT = TILE_SIZE * GRID_HEIGHT
FPS = 60

# Tile kinds and colors
TILE_TYPES = ["Solid", "Ice", "Platform"]
TILE_COLORS = {
    "Solid": (100, 100, 100),
    "Ice": (0, 180, 255),
    "Platform": (200, 200, 200)
}

BG_COLORS = [
    (0, 0, 0),
    (50, 50, 100),
    (0, 100, 0),
    (100, 0, 0)
]

# init the things
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("CoT Room Editor")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

# State
tiles = {}  # {(grid_x, grid_y): tile_type}
exits = []  # {"points_to": str, "pos": [x, y]}
current_tile = "Solid"
current_bg_color = BG_COLORS[0]
placing_exit = False
room_id = "UnnamedRoom"

# Drawing functions
def draw_grid():
    for x in range(0, WINDOW_WIDTH, TILE_SIZE):
        pygame.draw.line(screen, (50, 50, 50), (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, TILE_SIZE):
        pygame.draw.line(screen, (50, 50, 50), (0, y), (WINDOW_WIDTH, y))

def draw_tiles():
    for (gx, gy), ttype in tiles.items():
        rect = pygame.Rect(gx * TILE_SIZE, gy * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(screen, TILE_COLORS[ttype], rect)

def draw_exits():
    for exit in exits:
        x, y = exit["pos"]
        rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(screen, (255, 255, 0), rect)
        # Draw a border
        pygame.draw.rect(screen, (0,0,0), rect, 2)

def save_to_file(filename):
    room_data = {
        "id": room_id,
        "size": [WINDOW_WIDTH, WINDOW_HEIGHT],
        "bg_colour": list(current_bg_color),
        "exits": [],
        "tiles": []
    }

    for exit in exits:
        room_data["exits"].append({
            "points_to": exit["points_to"],
            "pos": exit["pos"]
        })

    for (gx, gy), ttype in tiles.items():
        room_data["tiles"].append({
            "pos": [gx * TILE_SIZE, gy * TILE_SIZE],
            "kind": ttype
        })

    with open(filename, "w") as f:
        toml.dump(room_data, f)

    print(f"Saved room to {filename}")

# Main loop
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
                if placing_exit:
                    pass
                else:
                    idx = TILE_TYPES.index(current_tile)
                    current_tile = TILE_TYPES[(idx + 1) % len(TILE_TYPES)]
                    print(f"Switched to {current_tile}")
            elif event.key == pygame.K_b:
                idx = BG_COLORS.index(current_bg_color)
                current_bg_color = BG_COLORS[(idx + 1) % len(BG_COLORS)]
                print(f"Changed background color to {current_bg_color}")
            elif event.key == pygame.K_e:
                placing_exit = not placing_exit
                mode = "Exit placement mode" if placing_exit else "Tile placement mode"
                print(f"Mode: {mode}")
            elif event.key == pygame.K_i:
                room_id = input("Enter room ID: ")
                print(f"Room ID set to {room_id}")
            elif event.key == pygame.K_s:
                save_to_file("room.trm")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            gx = mx // TILE_SIZE
            gy = my // TILE_SIZE
            px = gx * TILE_SIZE
            py = gy * TILE_SIZE

            # indent hell starts here
            if placing_exit:
                if event.button == 1:
                    target = input("Exit points to Room ID: ")
                    exits.append({
                        "points_to": target,
                        "pos": [px, py]
                    })
                    print(f"Added exit to '{target}' at {px},{py}")
                elif event.button == 3:
                    removed = False
                    for e in exits:
                        ex, ey = e["pos"]
                        if ex == px and ey == py:
                            exits.remove(e)
                            print(f"Removed exit at {px},{py}")
                            removed = True
                            break
                    if not removed:
                        print("No exit found here.")
            else:
                if event.button == 1:
                    tiles[(gx, gy)] = current_tile
                elif event.button == 3:
                    if (gx, gy) in tiles:
                        del tiles[(gx, gy)]

    screen.fill(current_bg_color)
    draw_tiles()
    draw_exits()
    draw_grid()

    # Info text
    mode_text = "EXIT MODE" if placing_exit else "TILE MODE"
    txt = font.render(
        f"{mode_text} | Tile: {current_tile} (TAB to change) | ID: {room_id} | B: BG | I: ID | E: Toggle Exit | S: Save",
        True, (255, 255, 255)
    )
    screen.blit(txt, (8, 8))

    pygame.display.flip()

pygame.quit()
sys.exit()

