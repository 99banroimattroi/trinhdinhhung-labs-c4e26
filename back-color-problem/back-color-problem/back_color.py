from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():

    m = choice(shapes)
    c = choice(shapes)
    meaning = m["text"]
    color = c["color"]
    
    return [
            meaning,
            color,
            randint(0, 1) # 0 : meaning, 1: color
            ]

def is_inside(v,b):
    if v[0] < b[0] or v[0] > b[0] + b[2]:
        return False
    else:
        if v[1] < b[1] or v[1] > b[1] + b[3]:
            return False
        else:
            return True

def mouse_press(x, y, text, color, quiz_type):
    v = [x, y]
    for i in range(4):
        if is_inside(v, shapes[i]["rect"]) == True:
            check = [shapes[i]["text"], shapes[i]["color"]]
    if quiz_type == 0:
        if check[0] == text:
            return True
        else:
            return False
    elif quiz_type == 1:
        if check[1] == color:
            return True
        else:
            return False
            

