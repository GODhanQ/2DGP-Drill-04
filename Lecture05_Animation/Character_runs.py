from pico2d import *
from typing import Final

open_canvas()

animation_count: Final = 4
animation_frame_count = [10, 12, 6, 9]
animation_frame_wANDh = [(27, 45), (27, 48), (27, 48), (27, 48), (32, 48),
                         (32, 48), (32, 48), (32, 48), (32, 48), (32, 48),
                         (32, 48)]  # 가로 너비를 기존 값에서 3 더 늘림
sprite_width = 399
sprite_height = 525
character = load_image("sonic-sprite.png")

frame = 0
while True:
    clear_canvas()

    bottom = sprite_height - (2 * animation_frame_wANDh[0][1]) + 10
    left = frame * animation_frame_wANDh[0][0] + 3

    # 5번째 프레임부터 left 값을 추가로 +5
    if frame >= 5:
        left += 5

    character.clip_draw(left, bottom, animation_frame_wANDh[0][0],
                        animation_frame_wANDh[0][1], 410, 300)
    update_canvas()
    frame = (frame + 1) % animation_frame_count[0]
    delay(0.5)
    print(frame)

close_canvas()