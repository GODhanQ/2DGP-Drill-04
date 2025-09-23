from pico2d import *

open_canvas()

animation_count = 4
current_animation = 0
animation_frame_count = [6, 6, 5, 5]
animation_frame_wANDh = [
    [(192, 150), (192, 150), (192, 150), (192, 150), (192, 150), (192, 150)],
    [(192, 150), (192, 150), (192, 150), (192, 150), (192, 150), (192, 150)],
    [(230, 150), (230, 150), (230, 150), (230, 150), (230, 150)],
    [(230, 150), (230, 150), (230, 150), (230, 150), (230, 150)]
]
sprite_width = 1536
sprite_height = 1024
character = load_image("Samurai_Sprite.png")

frame = 0
# 애니메이션의 첫 번째 프레임을 표시하기 위한 계산
# 첫 번째 애니메이션(current_animation = 0), 첫 번째 프레임(frame = 0)
left = 0
bottom = sprite_height - animation_frame_wANDh[0][0][1]
width = animation_frame_wANDh[0][0][0]
height = animation_frame_wANDh[0][0][1]

while True:
    clear_canvas()
    character.clip_draw(left, bottom, width, height, 400, 300)
    update_canvas()

close_canvas()