from pico2d import *

open_canvas()

animation_count = 4
current_animation = 0
# 밑에서 부터 첫 번째
animation_frame_count = [5, 5, 6, 6]
animation_frame_wANDh = [
    [(300, 249), (300, 249), (300, 249), (300, 249), (300, 249), (300, 249)],
    [(), (), (), (), (), ()],
    [(), (), (), (), ()],
    [(), (), (), (), ()]
]
sprite_width = 1800
sprite_height = 1000
character = load_image("Samurai_Sprite_1800x1000.png")

frame = 0
while True:
    clear_canvas()

    # 현재 프레임의 너비와 높이 가져오기
    width, height = animation_frame_wANDh[0][frame]

    bottom = current_animation * (sprite_height // 4)
    left = frame * sprite_width // 6

    character.clip_draw(left, bottom, width, height, 400, 300)
    update_canvas()

    # 프레임 업데이트 및 딜레이
    print(frame)
    frame = (frame + 1) % animation_frame_count[0]
    delay(0.5)

close_canvas()