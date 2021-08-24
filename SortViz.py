import turtle
import random
import time

# Screen
wn = turtle.Screen()
wn.title("Sorting Visualiser")
wn.setup(width = 1200, height = 700)
wn.tracer(0)

# Background
def display_vis():
    dispbg = turtle.Turtle()
    dispbg.color("grey")
    dispbg.fillcolor("#DAECFF")
    dispbg.speed(0)
    dispbg.hideturtle()
    dispbg.penup()
    dispbg.width(4)
    dispbg.goto(-412.5, 266)
    dispbg.pendown()
    dispbg.begin_fill()
    for i in range(2):
        dispbg.forward(831.5)
        dispbg.right(90)
        dispbg.forward(569)
        dispbg.right(90)
    dispbg.end_fill()
    wn.update()
display_vis()

# Initialization
a = [0]*100
l = []
pen = [0]*4
writer = [0]*4
fv = 0
gv = 0

write_time = turtle.Turtle()
write_time.hideturtle()

# Hiding Turtle
def hide_turtle():
    for i in range(4):
        pen[i].clear()
        writer[i].clear()
    wn.update()
    
# Showing Turtle
def show_turtle():
    function_button()

# Generating Lines
def generate_lines():
    global fv, gv
    if a[0] == 0 or fv == 1:
        fv=0
        d = 8
        for i in range(100):
            a[i] = turtle.Turtle()
            a[i].hideturtle()
            a[i].shape("square")
            a[i].color("cyan")
            alen = random.uniform(0.1,28)
            a[i].shapesize(stretch_len = alen, stretch_wid= .2)
            l.append(alen)
            a[i].speed(0)
            a[i].left(90)
            a[i].penup()
            res_len_sel = 300 - (l[i] * 10)
            a[i].goto((-400 + d), -res_len_sel)
            a[i].showturtle()
            d+=8
        wn.update()
    else:
        gv = 1
        clear_screen()

# Selection Sort
def sel_sort():
    for jump in range(100):
        a[jump].color("#FF1100")
        var = a[jump].xcor()
        len = l[jump]
        pos = jump

        res_len_sel = res_len_strd = 300 - (l[jump] * 10)

        for ice in range(jump+1, 100):

            if l[ice] < len:
                len = l[ice]
                var = a[ice].xcor()
                res_len_strd = 300 - (l[ice] * 10)
                pos = ice
            a[ice].color("cyan")
        
        a[pos].color("green")
        a[pos].goto(a[jump].xcor(), -res_len_strd)
        a[jump].goto(var, -res_len_sel)
        a[jump], a[pos] = a[pos], a[jump]
        l[jump], l[pos] = l[pos], l[jump]
        wn.update()

# Bubble Sort
def bub_sort():
    for i in range(99):
        for j in range(99-i):
            var = a[j].xcor()
            vara = a[j+1].xcor()
            res_len_small = 300 - (l[j] * 10)
            res_len_large = 300 - (l[j+1] * 10)
            if l[j] > l[j+1]:
                a[j].goto(vara, - res_len_small)
                a[j+1].goto(var, - res_len_large)
                a[j], a[j+1] = a[j+1], a[j]
                l[j], l[j+1] = l[j+1], l[j]
            a[j].color("cyan")
            a[j+1].color("green")
        wn.update()
    a[0].color("green")
    wn.update()

# Clearing Screen
def clear_screen():
    global fv, gv
    for lina in a:
        lina.clear()
        lina.hideturtle()
    l.clear()
    wn.update()
    fv = 1
    if gv == 1:
        gv = 0
        generate_lines()

# Generating Buttons
def generate_buttons(x,y,obj,msg):
    pen[obj] = turtle.Turtle()
    pen[obj].hideturtle()
    pen[obj].penup()
    pen[obj].goto(x-80,y-20)
    pen[obj].pendown()
    pen[obj].color("#52A1FA")
    pen[obj].begin_fill()
    for i in range(2):
        pen[obj].fd(160)
        pen[obj].left(90)
        pen[obj].fd(40)
        pen[obj].left(90)
    pen[obj].end_fill()
    writer[obj] = turtle.Turtle()
    writer[obj].hideturtle()
    writer[obj].penup()
    writer[obj].goto(x,y-7.5)
    writer[obj].write(msg,font=('Verdana',12,'normal'),align="center")
    wn.update()

# Generating Buttons
def function_button():
    generate_buttons(-300,300,0,"Create New Lines")
    generate_buttons(-100,300,1,"Selection Sort")
    generate_buttons(100,300,2,"Bubble Sort")
    generate_buttons(300,300,3,"Clear Screen")

# Time Taken
def write_timeTaken(t):
    global write_time
    write_time.hideturtle()
    write_time.penup()
    write_time.goto(0,-325)
    write_time.write("Time Taken : " +str(t),font=('Verdana',12,'normal'),align="center")
    wn.update()

# Checking Screen Click
def checki(x,y):
    write_time.clear()
    if x>(-380) and x<(-220) and y>(280) and y<(320):
        hide_turtle()
        generate_lines()
        show_turtle()
    if x>(-180) and x<(-20) and y>(280) and y<(320):
        hide_turtle()
        t1 = time.time()
        sel_sort()
        t2 = time.time()
        write_timeTaken(t2-t1)
        show_turtle()
    if x>(20) and x<(180) and y>(280) and y<(320):
        hide_turtle()
        t1 = time.time()
        bub_sort()
        t2 = time.time()
        write_timeTaken(t2-t1)
        show_turtle()
    if x>(220) and x<(380) and y>(280) and y<(320):
        hide_turtle()
        clear_screen()
        show_turtle()

function_button()
turtle.onscreenclick(checki)
turtle.listen()

turtle.done()