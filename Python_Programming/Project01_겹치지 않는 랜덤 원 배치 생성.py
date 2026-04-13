import turtle as t
import random as rd
import PySimpleGUI as sG
import math as m

#  레이아웃 만들기
layout = [
            [sG.Text('원 몇개를 그릴까요? ')],
            [sG.Text('개수 : '), sG.InputText(key = '_INPUT_')],
            [sG.Button('그리기'), sG.Button('지우기'), sG.Button('끝내기(Exit)')]
         ]

# 원도우 창 만들기
window = sG.Window('원 그리기', layout, grab_anywhere=True)

# 이벤트 루프
while True:
    event, values = window.Read() # Read the event that happened and the values dictionary
    print(event, values)
    if event in (None, '끝내기(Exit)'): # If user closeddow with X or if user clicked "끝내기(Exit)" button then exit
        break
    elif event in (None, '그리기'):
        print(values)
        print(values['_INPUT_'])
        window.Element('_INPUT_').Update('')
    elif event in (None, '지우기'):
        t.clear()
        continue

    # 초기 설정
    n = int(values['_INPUT_'])
    count=0
    t.setup(660,660)
    t.speed(4)
    t.shape("turtle")

    # 범위 그리기
    t.penup()
    t.goto(-300,300)
    t.pendown()
    for _ in range(4):
        t.fd(600)
        t.right(90)

    # 원 그리는 함수
    def draw_circle(x, y, radius):
        t.penup()
        t.goto(x, y - radius)
        t.pendown()
        t.circle(radius)

    # 원들을 안겹치게 그리는 함수
    def draw_circles():
        circles = []  # 원들의 정보를 저장할 리스트

        while True:
            radius = rd.randint(10, 50)  # 반지름 범위를 10에서 50 사이의 랜덤값으로 지정
            x = rd.randint(-250, 250) # x좌표의 범위를 -250에서 250 사이의 랜덤값으로 지정
            y = rd.randint(-250, 250) # y좌표의 범위를 -250에서 250 사이의 랜덤값으로 지정
            
            # 원들이 안겹치도록 확인
            overlap = False
            for circle in circles:
                distance = m.sqrt((x - circle[0]) ** 2 + (y - circle[1]) ** 2)
                if distance < radius + circle[2]:
                    overlap = True
                    break

            #원이 안겹치면 그리기
            if overlap==False :
                draw_circle(x, y, radius)
                circles.append((x, y, radius))
                global count
                count+=1
                
            # 원의 개수가 되면 끝내기
            if count==n:
                break

    # 원들 그리기
    draw_circles()

window.close()

