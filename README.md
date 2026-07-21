# BGCEC 22nd

> 부산광역시정보영재교육원(BGCEC) 22기 고1 정보심화반에서 학습한 Python 프로그래밍과 수학 알고리즘 실습을 정리한 저장소입니다.

Python의 기본 문법과 문제 해결 방법을 익히기 위해 CodeUp 기초 100제 문제를 풀고, `turtle`과 PySimpleGUI를 활용한 그래픽 프로젝트를 제작했습니다. 수론 학습 내용으로 유클리드 알고리즘을 이용한 최대공약수 계산기도 구현했습니다.

## Overview

| Item | Description |
| --- | --- |
| Institution | 부산광역시정보영재교육원 (BGCEC) |
| Program | 제22기 고1 정보심화반 |
| Achievement | 고1 정보심화반 차석 · 교육감상 수상 |

## Repository Structure

```text
bgcec-22nd
├── Number_Theory
│   └── 유클리드 알고리즘 최대공약수 계산기.py
├── Python_Programming
│   ├── CodeUP #6001.py ~ CodeUP #6098.py
│   ├── Project01_겹치지 않는 랜덤 원 배치 생성.py
│   ├── Project02_겹치지 않는 랜덤 사각형 생성.py
│   ├── Project03_원자모형 시뮬레이터 프로젝트.py
│   └── Turtle 드로잉 컨트롤 프로그램.py
└── README.md
```

## Contents

### Python Programming

- **CodeUp 기초 100제**: 입출력, 자료형, 연산자, 조건문, 반복문, 비트 연산, 리스트 등 Python 기초 문법 실습
- **랜덤 원 배치**: 원의 중심 거리와 반지름을 비교하여 서로 겹치지 않는 원을 무작위로 배치
- **랜덤 사각형 배치**: 좌표와 너비·높이를 이용해 충돌 여부를 검사하고 서로 겹치지 않는 사각형을 생성
- **원자 모형 시뮬레이터**: 주기율표에서 원소를 선택하면 원자 번호에 맞는 전자 배치를 Turtle 애니메이션으로 표현
- **Turtle 드로잉 컨트롤**: 방향키 또는 WASD와 마우스를 사용해 거북이를 움직이며 그림을 그리는 프로그램

### Number Theory

- **최대공약수 계산기**: 두 정수를 입력받아 유클리드 호제법으로 최대공약수(GCD)를 계산

## Tech Stack

| Category | Technology |
| --- | --- |
| Language | Python 3 |
| GUI | Turtle, PySimpleGUI |
| Standard Libraries | `math`, `random`, `turtle` |
| Practice Platform | CodeUp |

## Learning Goals

- Python 기본 문법과 표준 입출력 익히기
- 조건문과 반복문을 활용한 문제 해결 능력 기르기
- 함수, 리스트 및 좌표 계산을 실제 프로그램에 적용하기
- GUI 이벤트 처리와 Turtle 그래픽의 동작 방식 이해하기
- 기초 수론 알고리즘을 코드로 구현하기

## Notes

- 각 CodeUp 파일은 해당 문제 번호의 독립적인 풀이입니다.
- 일부 그래픽 프로젝트는 실행 시 별도의 Turtle 창과 PySimpleGUI 창을 엽니다.
- 학습 당시 작성한 코드의 구현 방식과 주석을 기록 목적으로 보존하고 있습니다.
