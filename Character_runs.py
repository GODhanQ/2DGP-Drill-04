from pico2d import *
from typing import Final
open_canvas()

animation_count: Final = 4
animation_frame_count = [11, 12, 6, 9]
character = load_image("Lecture05_Animation\\sonic-sprite.png")

frame = 0
while True:
    clear_canvas()
    character.clip_draw(frame * 72, 97 * 3, 72, 97, 400, 300)
    update_canvas()
    frame = (frame + 1) % animation_frame_count[0]
    delay(0.05)


close_canvas()