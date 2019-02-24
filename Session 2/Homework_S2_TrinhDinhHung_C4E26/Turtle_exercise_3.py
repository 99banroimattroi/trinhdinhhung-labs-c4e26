def draw_square(length,colors):

    import turtle as cr

    cr.speed(1)
    cr.color(colors)

    for i in range(4):
        cr.fd(length)
        cr.lt(90)
    
# draw_square(159,"gold")
