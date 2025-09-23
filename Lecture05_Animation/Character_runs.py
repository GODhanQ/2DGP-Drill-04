from pico2d import *
from typing import Final

open_canvas()

animation_count: Final = 4
animation_frame_count = [10, 12, 6, 9]  # 첫 번째 애니메이션 프레임 수를 10으로 조정
animation_frame_wANDh = [(24, 45), (24, 48), (24, 48), (24, 48), (24, 48),
                         (24, 48), (24, 48), (24, 48), (24, 48), (24, 48),
                         (24, 48)]  # 가로 너비를 기존 값에서 5 늘림
sprite_width = 399
sprite_height = 525
character = load_image("sonic-sprite.png")

clear_canvas()

frame = 0
bottom = sprite_height - (2 * animation_frame_wANDh[0][1]) + 10
left = frame * animation_frame_wANDh[0][0] + 5  # left 값을 5만큼 오른쪽으로 이동
character.clip_draw(left, bottom, animation_frame_wANDh[0][0],
                    animation_frame_wANDh[0][1], 400, 300)
update_canvas()

# while True:
#     clear_canvas()
#     # bottom 좌표를 약간 위로 조정
#     bottom = sprite_height - (2 * animation_frame_wANDh[0][1]) + 10
#     left = frame * animation_frame_wANDh[0][0] + 5  # left 값을 5만큼 오른쪽으로 이동
#     character.clip_draw(left, bottom, animation_frame_wANDh[0][0],
#                         animation_frame_wANDh[0][1], 410, 300)
#     update_canvas()
#     frame = (frame + 1) % animation_frame_count[0]
#     delay(0.5)

# close_canvas()
while True:
    pass