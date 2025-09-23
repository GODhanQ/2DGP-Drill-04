from pico2d import *
import pygame

open_canvas()

animation_count = 4
current_animation = 0
# 밑에서 부터 첫 번째
animation_frame_count = [5, 5, 6, 6]
animation_frame_wANDh = [
    # 주황 사무라이 종 배기
    [(300, 240), (300, 240), (300, 240), (300, 240), (300, 240) ],
    # 주황 사무라이 횡 배기
    [(150, 240), (160, 240), (170, 240), (300, 240), (250, 240) ],
    # 빨강 사무라이 뛰기
    [(300, 240), (300, 240), (300, 240), (300, 240), (300, 240), (300, 240) ],
    # 빨강 사무라이 걷기
    [(300, 240), (300, 240), (300, 240), (300, 240), (300, 240), (300, 240) ]
]
sprite_width = 1800
sprite_height = 1000

character = load_image("Samurai_Sprite_1800x1000.png")

frame = 0
while True:
    for i in range(0, animation_count):
        current_animation = i
        for loop in range(5):
            for j in range(animation_frame_count[i]):
                clear_canvas()

                width, height = animation_frame_wANDh[i][j]

                bottom = current_animation * (sprite_height // 4)
                left = j * sprite_width // 6

                # 줄어든 너비의 반 만큼 left를 이동
                MoveLeft_ReducedWidth = 300 - width
                left += MoveLeft_ReducedWidth // 2

                character.clip_draw(left, bottom, width, height, 400, 300)
                update_canvas()

                print(f"Frame : {j}, Animation : {i}, Width : {width}, Height : {height}")
                delay(0.1)
        delay(1.0)

close_canvas()