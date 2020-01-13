import turtle
import time

def setup_simulator_window():
    """
    set up a window with default settings to draw Traffic Lights
    :param:
    :return t: turtle object 
    """
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    return t


def draw_circle(t):
    """
    Draws a Traffic Light circle
    :param:
    :return: 
    """
    t.begin_fill()
    t.circle(100)
    t.end_fill()


def set_pos(x, y, t):
    """
    Set up the position for next circle
    :param x: x axis position
    :param y: y axis position 
    :param t: turtle object
    :return: 
    """
    t.setpos(x,y)


def fill_circle(x,y,current_light, light, t):
    """
    Set up the position for Traffic Light and fills it
    :param x: x axis position 
    :param y: y axis position 
    :param current_light: current light that should be displayed 
    :param light: corresponding light for this circle 
    :param t: turtle object 
    :return: 
    """
    set_pos(x,y,t)
    if(current_light == light):
        t.fillcolor(current_light)
    else:
        t.fillcolor('white')
    draw_circle(t)


def switch_light(current_light):
    """
    Generates the next light in sequence that should be displayed
    :param current_light: current light that should be displayed 
    :return next_light: next light that should be displayed 
    """
    if(current_light == "green"):
        next_light = "yellow"
    elif(current_light == "yellow"):
        next_light = "red"
    elif(current_light == "red"):
        next_light = "green"
    return next_light


def open_simulator(times):
    """
    Generates a simulator window to display traffic lights and 
    iterates thru each light as per the given transition times
    :param times: corresponding transition times for each lights 
    """
    t = setup_simulator_window()
    current_light = "green"
    while(True):
        fill_circle(0, 220, current_light, "red", t)
        fill_circle(0, 0, current_light, "yellow", t)
        fill_circle(0, -220, current_light, "green", t)
        time.sleep(times[current_light])
        current_light = switch_light(current_light)
