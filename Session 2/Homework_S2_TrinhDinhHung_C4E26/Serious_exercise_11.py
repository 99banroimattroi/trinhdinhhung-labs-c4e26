def is_inside(x,y):
    if x[0] < y[0] or x[0] > y[0] + y[2]:
        s = False
    else:
        if x[1] < y[1] or x[1] > y[1] + y[3]:
            s = False
        else:
            s = True
    print(s)
is_inside([100, 120], [140, 60, 	])
# is_inside([200, 120],[140, 60, 100, 200])
