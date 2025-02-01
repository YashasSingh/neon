import random
import time
import board
import displayio
import framebufferio
import rgbmatrix

displayio.release_displays()

def apply_rps_rule(old, new):
    width = old.width
    height = old.height
    for y in range(height):
        yyy = y * width
        ym1 = ((y + height - 1) % height) * width
        yp1 = ((y + 1) % height) * width
        xm1 = width - 1
        for x in range(width):
            xp1 = (x + 1) % width
            current = old[x + yyy]
            counts = [0, 0, 0, 0]
            for dx in [xm1, x, xp1]:
                for dy in [ym1, yyy, yp1]:
                    if not (dx == x and dy == yyy):
                        val = old[dx + dy]
                        counts[val] += 1

            if current == 0:
                max_count = max(counts[1:])
                if max_count >= 4:
                    new[x+yyy] = random.choice([i for i, c in enumerate(counts) if c == max_count])
            else:
                enemy = 1 + (current % 3)
                if counts[enemy] >= 3:
                    new[x+yyy] = enemy
                else:
                    new[x+yyy] = current
            xm1 = x

def randomize_rps(output):
    for i in range(output.height * output.width):
        output[i] = random.choice([1, 2, 3])

matrix = rgbmatrix.RGBMatrix(
    width=64, height=32, bit_depth=2,
    rgb_pins=[board.D6, board.D5, board.D9, board.D11, board.D10, board.D12],
    addr_pins=[board.A5, board.A4, board.A3, board.A2],
    clock_pin=board.D13, latch_pin=board.D0, output_enable_pin=board.D1)
display = framebufferio.FramebufferDisplay(matrix, auto_refresh=False)

SCALE = 1
b1 = displayio.Bitmap(display.width//SCALE, display.height//SCALE, 4)
b2 = displayio.Bitmap(display.width//SCALE, display.height//SCALE, 4)
palette = displayio.Palette(4)
palette[0] = 0x000000
palette[1] = 0xFF0000
palette[2] = 0x00FF00
palette[3] = 0x0000FF

tg1 = displayio.TileGrid(b1, pixel_shader=palette)
tg2 = displayio.TileGrid(b2, pixel_shader=palette)

g1 = displayio.Group(scale=SCALE)
g1.append(tg1)
display.root_group = g1

g2 = displayio.Group(scale=SCALE)
g2.append(tg2)

randomize_rps(b1)
display.auto_refresh = True

while True:
    for _ in range(5):
        display.root_group = g1
        apply_rps_rule(b1, b2)
        display.root_group = g2
        apply_rps_rule(b2, b1)
    if random.random() < 0.02:
        palette[1] = random.randint(0, 0xffffff)
        palette[2] = random.randint(0, 0xffffff)
        palette[3] = random.randint(0, 0xffffff)
