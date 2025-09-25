from pico2d import *

open_canvas(800, 600)
image = load_image('sonic-sprite.png')

sprite = (
    ((0, 0, 100, 100), (100, 0, 100, 100), (200, 0, 100, 100), (300, 0, 100, 100)),
    ((0, 100, 100, 100), (100, 100, 100, 100), (200, 100, 100, 100), (300, 100, 100, 100)),
    ((0, 200, 100, 100), (100, 200, 100, 100), (200, 200, 100, 100), (300, 200, 100, 100)),
    ((0, 300, 100, 100), (100, 300, 100, 100), (200, 300, 100, 100), (300, 300, 100, 100))
)
def play_animation(action):
    for frame in action:
        clear_canvas()
        image.clip_draw(frame[0], frame[1], frame[2], frame[3], 400, 300)
        update_canvas()
        delay(0.1)

while True:
    for action in sprite:
        for i in range(5):
            play_animation(action)
        delay(1.0)
    pass

