import turtle as t
import PySimpleGUI as sG
import math as m

# 레이아웃 만들기
layout = [
            [sG.Text('무슨 원소를 그릴까요? ')],
            [sG.Button('H'),sG.Button('  '),sG.Button('  '),sG.Button('  '),sG.Button('  '),sG.Button('  '),sG.Button('  '),sG.Button('He')],
            [sG.Button('Li'),sG.Button('Be'),sG.Button('B'),sG.Button('C'),sG.Button('N'),sG.Button('O'),sG.Button('F'),sG.Button('Ne'),],
            [sG.Button('Na'),sG.Button('Mg'),sG.Button('Al'),sG.Button('Si'),sG.Button('P'),sG.Button('S'),sG.Button('Cl'),sG.Button('Ar'),],
            [sG.Button('K'),sG.Button('Ca')],
         ]

# 원도우 창 만들기
window = sG.Window('원소 그리기', layout, grab_anywhere=True)

def cycle(cy1,cy2,cy3,cy4):
    nl=t.Turtle()
    nl.turtlesize(2)
    nl.shape('circle')
    nl.color('red')
    nl.goto(0,0)
    for i in range(1,cy1+cy2+cy3+cy4+1):
        globals()["et{}".format(i)]=t.Turtle()
        globals()["et{}".format(i)].color('blue')
        globals()["et{}".format(i)].shape('circle')
        globals()["et{}".format(i)].turtlesize(1)
        globals()["et{}".format(i)].speed(0)
        globals()["et{}".format(i)].penup()        

i=0


def cycle1(r):
    global x1
    global y1
    x1=m.cos(i)*r
    y1=m.sin(i)*r

def cycle2(r):
    global x2
    global y2
    x2=m.cos(i-80)*r
    y2=m.sin(i-80)*r

def cycle3(r):
    global x3
    global y3
    x3=m.cos(i-175)*r
    y3=m.sin(i-175)*r

def cycle4(r):
    global x4
    global y4
    x4=m.cos(i-230)*r
    y4=m.sin(i-230)*r

def pd(i):
    for i in range(1,i+1):
        globals()["et{}".format(i)].pendown()
    
# 이벤트 루프
while True:
    event, values = window.Read() # Read the event that happened and the values dictionary
    print(event, values)
    if event in (None, 'H'):
        cycle(1,0,0,0)
        while True:
            cycle1(50)
            et1.goto(x1,y1)
            pd(1)
            i=i+0.01
    elif event in (None,"He"):
        cycle(2,0,0,0)
        while True:
            cycle1(50)
            et1.goto(x1,y1)
            et2.goto(-x1,-y1)
            pd(2)
            i=i+0.01
    elif event in (None,"Li"):
        cycle(2,1,0,0)
        while True:
            cycle1(50)
            et1.goto(x1,y1)
            et2.goto(-x1,-y1)
            cycle1(100)
            et3.goto(x1,y1)
            pd(3)
            i=i+0.01
    elif event in (None,"Be"):
        cycle(2,2,0,0)
        while True:
            cycle1(50)
            et1.goto(x1,y1)
            et2.goto(-x1,-y1)
            cycle1(100)
            et3.goto(x1,y1)
            et4.goto(-x1,-y1)
            pd(4)
            i=i+0.01
    elif event in (None,"B"):
        cycle(2,3,0,0)
        while True:
            cycle1(50)
            et1.goto(x1,y1)
            et2.goto(-x1,-y1)
            cycle1(100)
            et3.goto(x1,y1)
            et4.goto(-x1,-y1)
            cycle2(100)
            et5.goto(x2,y2)
            pd(5)
            i=i+0.01
    elif event in (None,"C"):
        cycle(2,4,0,0)
        while True:
            cycle1(50)
            et1.goto(x1,y1)
            et2.goto(-x1,-y1)
            cycle1(100)
            et3.goto(x1,y1)
            et4.goto(-x1,-y1)
            cycle2(100)
            et5.goto(x2,y2)
            et6.goto(-x2,-y2)
            pd(6)
            i=i+0.01
    elif event in (None,"N"):
        cycle(2,5,0,0)
        while True:
            cycle1(50)
            et1.goto(x1,y1)
            et2.goto(-x1,-y1)
            cycle1(100)
            et3.goto(x1,y1)
            et4.goto(-x1,-y1)
            cycle2(100)
            et5.goto(x2,y2)
            et6.goto(-x2,-y2)
            cycle3(100)
            et7.goto(x3,y3)
            pd(7)
            i=i+0.01
    elif event in (None,"O"):
        cycle(2,6,0,0)
        while True:
            cycle1(50)
            et1.goto(x1,y1)
            et2.goto(-x1,-y1)
            cycle1(100)
            et3.goto(x1,y1)
            et4.goto(-x1,-y1)
            cycle2(100)
            et5.goto(x2,y2)
            et6.goto(-x2,-y2)
            cycle3(100)
            et7.goto(x3,y3)
            et8.goto(-x3,-y3)
            pd(8)
            i=i+0.01
    elif event in (None,"F"):
        cycle(2,7,0,0)
        while True:
            cycle1(50)
            et1.goto(x1,y1)
            et2.goto(-x1,-y1)
            cycle1(100)
            et3.goto(x1,y1)
            et4.goto(-x1,-y1)
            cycle2(100)
            et5.goto(x2,y2)
            et6.goto(-x2,-y2)
            cycle3(100)
            et7.goto(x3,y3)
            et8.goto(-x3,-y3)
            cycle4(100)
            et9.goto(x4,y4)
            pd(9)
            i=i+0.01
    elif event in (None,"Ne"):
        cycle(2,8,0,0)
        while True:
            cycle1(50)
            et1.goto(x1,y1)
            et2.goto(-x1,-y1)
            cycle1(100)
            et3.goto(x1,y1)
            et4.goto(-x1,-y1)
            cycle2(100)
            et5.goto(x2,y2)
            et6.goto(-x2,-y2)
            cycle3(100)
            et7.goto(x3,y3)
            et8.goto(-x3,-y3)
            cycle4(100)
            et9.goto(x4,y4)
            et10.goto(-x4,-y4)
            pd(10)
            i=i+0.01
    elif event in (None,"Na"):
        cycle(2,8,1,0)
        while True:
            cycle1(50)
            et1.goto(x1,y1)
            et2.goto(-x1,-y1)
            cycle1(100)
            et3.goto(x1,y1)
            et4.goto(-x1,-y1)
            cycle1(150)
            et11.goto(x1,y1)
            cycle2(100)
            et5.goto(x2,y2)
            et6.goto(-x2,-y2)
            cycle3(100)
            et7.goto(x3,y3)
            et8.goto(-x3,-y3)
            cycle4(100)
            et9.goto(x4,y4)
            et10.goto(-x4,-y4)
            pd(11)
            i=i+0.01
    elif event in (None,"Mg"):
        cycle(2,8,2,0)
        while True:
            cycle1(50)
            et1.goto(x1,y1)
            et2.goto(-x1,-y1)
            cycle1(100)
            et3.goto(x1,y1)
            et4.goto(-x1,-y1)
            cycle1(150)
            et11.goto(x1,y1)
            et12.goto(-x1,-y1)
            cycle2(100)
            et5.goto(x2,y2)
            et6.goto(-x2,-y2)
            cycle3(100)
            et7.goto(x3,y3)
            et8.goto(-x3,-y3)
            cycle4(100)
            et9.goto(x4,y4)
            et10.goto(-x4,-y4)
            pd(12)
            i=i+0.01
    elif event in (None,"Al"):
        cycle(2,8,3,0)
        while True:
            cycle1(50)
            et1.goto(x1,y1)
            et2.goto(-x1,-y1)
            cycle1(100)
            et3.goto(x1,y1)
            et4.goto(-x1,-y1)
            cycle1(150)
            et11.goto(x1,y1)
            et12.goto(-x1,-y1)
            cycle2(100)
            et5.goto(x2,y2)
            et6.goto(-x2,-y2)
            cycle2(150)
            et13.goto(x2,y2)
            cycle3(100)
            et7.goto(x3,y3)
            et8.goto(-x3,-y3)
            cycle4(100)
            et9.goto(x4,y4)
            et10.goto(-x4,-y4)
            pd(13)
            i=i+0.01
    elif event in (None,"Si"):
        cycle(2,8,4,0)
        while True:
            cycle1(50)
            et1.goto(x1,y1)
            et2.goto(-x1,-y1)
            cycle1(100)
            et3.goto(x1,y1)
            et4.goto(-x1,-y1)
            cycle1(150)
            et11.goto(x1,y1)
            et12.goto(-x1,-y1)
            cycle2(100)
            et5.goto(x2,y2)
            et6.goto(-x2,-y2)
            cycle2(150)
            et13.goto(x2,y2)
            et14.goto(-x2,-y2)
            cycle3(100)
            et7.goto(x3,y3)
            et8.goto(-x3,-y3)
            cycle4(100)
            et9.goto(x4,y4)
            et10.goto(-x4,-y4)
            pd(14)
            i=i+0.01
    elif event in (None,"P"):
        cycle(2,8,5,0)
        while True:
            cycle1(50)
            et1.goto(x1,y1)
            et2.goto(-x1,-y1)
            cycle1(100)
            et3.goto(x1,y1)
            et4.goto(-x1,-y1)
            cycle1(150)
            et11.goto(x1,y1)
            et12.goto(-x1,-y1)
            cycle2(100)
            et5.goto(x2,y2)
            et6.goto(-x2,-y2)
            cycle2(150)
            et13.goto(x2,y2)
            et14.goto(-x2,-y2)
            cycle3(100)
            et7.goto(x3,y3)
            et8.goto(-x3,-y3)
            cycle4(150)
            et15.goto(x3,y3)
            cycle4(100)
            et9.goto(x4,y4)
            et10.goto(-x4,-y4)
            pd(15)
            i=i+0.01
    elif event in (None,"S"):
        cycle(2,8,6,0)
        while True:
            cycle1(50)
            et1.goto(x1,y1)
            et2.goto(-x1,-y1)
            cycle1(100)
            et3.goto(x1,y1)
            et4.goto(-x1,-y1)
            cycle1(150)
            et11.goto(x1,y1)
            et12.goto(-x1,-y1)
            cycle2(100)
            et5.goto(x2,y2)
            et6.goto(-x2,-y2)
            cycle2(150)
            et13.goto(x2,y2)
            et14.goto(-x2,-y2)
            cycle3(100)
            et7.goto(x3,y3)
            et8.goto(-x3,-y3)
            cycle4(150)
            et15.goto(x3,y3)
            et16.goto(-x3,-y3)           
            cycle4(100)
            et9.goto(x4,y4)
            et10.goto(-x4,-y4)
            pd(16)
            i=i+0.01
    elif event in (None,"Cl"):
        cycle(2,8,7,0)
        while True:
            cycle1(50)
            et1.goto(x1,y1)
            et2.goto(-x1,-y1)
            cycle1(100)
            et3.goto(x1,y1)
            et4.goto(-x1,-y1)
            cycle1(150)
            et11.goto(x1,y1)
            et12.goto(-x1,-y1)
            cycle2(100)
            et5.goto(x2,y2)
            et6.goto(-x2,-y2)
            cycle2(150)
            et13.goto(x2,y2)
            et14.goto(-x2,-y2)
            cycle3(100)
            et7.goto(x3,y3)
            et8.goto(-x3,-y3)
            cycle3(150)
            et15.goto(x3,y3)
            et16.goto(-x3,-y3)           
            cycle4(100)
            et9.goto(x4,y4)
            et10.goto(-x4,-y4)
            ctcle4(150)
            et17.goto(x4,y4)
            pd(17)
            i=i+0.01
    elif event in (None,"Ar"):
        cycle(2,8,8,0)
        while True:
            cycle1(50)
            et1.goto(x1,y1)
            et2.goto(-x1,-y1)
            cycle1(100)
            et3.goto(x1,y1)
            et4.goto(-x1,-y1)
            cycle1(150)
            et11.goto(x1,y1)
            et12.goto(-x1,-y1)
            cycle2(100)
            et5.goto(x2,y2)
            et6.goto(-x2,-y2)
            cycle2(150)
            et13.goto(x2,y2)
            et14.goto(-x2,-y2)
            cycle3(100)
            et7.goto(x3,y3)
            et8.goto(-x3,-y3)
            cycle3(150)
            et15.goto(x3,y3)
            et16.goto(-x3,-y3)           
            cycle4(100)
            et9.goto(x4,y4)
            et10.goto(-x4,-y4)
            cycle4(150)
            et17.goto(x4,y4)
            et18.goto(-x4,-y4)
            pd(18)
            i=i+0.01
    elif event in (None,"K"):
        cycle(2,8,8,1)
        while True:
            cycle1(50)
            et1.goto(x1,y1)
            et2.goto(-x1,-y1)
            cycle1(100)
            et3.goto(x1,y1)
            et4.goto(-x1,-y1)
            cycle1(150)
            et11.goto(x1,y1)
            et12.goto(-x1,-y1)
            cycle1(200)
            et19.goto(x1,y1)
            cycle2(100)
            et5.goto(x2,y2)
            et6.goto(-x2,-y2)
            cycle2(150)
            et13.goto(x2,y2)
            et14.goto(-x2,-y2)
            cycle3(100)
            et7.goto(x3,y3)
            et8.goto(-x3,-y3)
            cycle3(150)
            et15.goto(x3,y3)
            et16.goto(-x3,-y3)           
            cycle4(100)
            et9.goto(x4,y4)
            et10.goto(-x4,-y4)
            cycle4(150)
            et17.goto(x4,y4)
            et18.goto(-x4,-y4)
            pd(19)
            i=i+0.01
    elif event in (None,"Ca"):
        cycle(2,8,8,2)
        while True:
            cycle1(50)
            et1.goto(x1,y1)
            et2.goto(-x1,-y1)
            cycle1(100)
            et3.goto(x1,y1)
            et4.goto(-x1,-y1)
            cycle1(150)
            et11.goto(x1,y1)
            et12.goto(-x1,-y1)
            cycle1(200)
            et19.goto(x1,y1)
            et20.goto(-x1,-y1)
            cycle2(100)
            et5.goto(x2,y2)
            et6.goto(-x2,-y2)
            cycle2(150)
            et13.goto(x2,y2)
            et14.goto(-x2,-y2)
            cycle3(100)
            et7.goto(x3,y3)
            et8.goto(-x3,-y3)
            cycle3(150)
            et15.goto(x3,y3)
            et16.goto(-x3,-y3)           
            cycle4(100)
            et9.goto(x4,y4)
            et10.goto(-x4,-y4)
            cycle4(150)
            et17.goto(x4,y4)
            et18.goto(-x4,-y4)
            pd(20)
            i=i+0.01
