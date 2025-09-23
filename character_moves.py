from pico2d import *
import time

open_canvas()

# aniamtion_count = 4
grass = load_image("Lecture05_Animation\\grass.png")
character = load_image("Lecture05_Animation\\run_animation.png")

start = time.time()
frame = 0
for x in range(0, 800, 10):
    # duration = start - time.time()
    # if (duration >= 5.0):
    #     animation_mod = (animation_mod + 1) % aniamtion_count
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()