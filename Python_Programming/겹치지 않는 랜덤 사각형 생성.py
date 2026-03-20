import turtle as t
import random as rd
import PySimpleGUI as sG

# 겹침 여부를 판단하는 함수
def overlap_check(square1, square2):
    x1, y1, width1, height1 = square1
    x2, y2, width2, height2 = square2

    if x2<=-300 or x2+width2>=300 or y2>=300 or y2-height2<=-300 :
        return True  # 테두리와 겹침
    elif x1 <= x2 <= x1+width1 and (y1>=y2>=y1-height1 or y2>=y1 and y1>=y2-height2) :
        return True  # 겹침
    elif x1 <= x2+width2 <= x1+width1 and (y1>=y2>=y1-height1 or y2>=y1 and y1>=y2-height2):
        return True  # 겹침
    elif x2<=x1 and x1+width1<=x2+width2 and y1>=y2-height2 :
        return True  # 겹침
    else :
        return False # 안겹침

# 레이아웃 만들기
layout = [
    [sG.Text('사각형 몇개를 그릴까요? ')],
    [sG.Text('개수 : '), sG.InputText(key='_INPUT_')],
    [sG.Button('그리기'), sG.Button('지우기'), sG.Button('끝내기(Exit)')]
]

# 원도우 창 만들기
window = sG.Window('사각형 그리기', layout, grab_anywhere=True)

# 이벤트 루프
while True:
    event, values = window.Read()  # Read the event that happened and the values dictionary
    print(event, values)
    if event in (None, '끝내기(Exit)'):  # If user closed window with X or clicked "끝내기(Exit)" button, then exit
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
    count = 0
    t.setup(660, 660)
    t.speed(4)
    t.shape("turtle")

    # 범위 그리기
    t.penup()
    t.goto(-300, 300)
    t.pendown()
    for _ in range(4):
        t.fd(600)
        t.right(90)

    # 사각형 그리는 함수
    def draw_square(x, y, width, height):
        t.penup()
        t.goto(x, y)
        t.pendown()
        for _ in range(2):
            t.fd(width)
            t.right(90)
            t.fd(height)
            t.right(90)

    # 사각형들을 안겹치게 그리는 함수
    def draw_squares():
        squares=[]

        while True:
            width = rd.randint(10, 100)  # 가로 길이를 10에서 100 사이로 설정
            height = rd.randint(10, 100)  # 세로 길이를 10에서 100 사이로 설정
            x = rd.randint(-300, 300) # x를 -3003에서 300 사이로 설정
            y = rd.randint(-300, 300) # y를 -300에서 300 사이로 설정

            new_sqaure = (x, y, width, height) #새 사각형의 값 튜플로 저장

            # 다른 사각형들과 겹치는지 확인
            overlap = False
            for sqaure in squares:
                if overlap_check(sqaure, new_sqaure):
                    overlap = True
                    break

            # 사각형이 안겹치면 그리기
            if overlap==False:
                draw_square(x, y, width, height)
                squares.append(new_sqaure)
                global count
                count += 1

            # 사각형의 개수가 되면 끝내기
            if count == n:
                break

    # 사각형들 그리기
    draw_squares()

window.close()

