from pico2d import get_events, load_image, update_canvas, clear_canvas, get_time

import game_framework
import title_mode


def init():
    global  image
    global running
    global logo_start_time

    logo_start_time = get_time()
    image = load_image('tuk_credit.png')
    running = True
    pass

def finish():
    pass

def update():
    global running
    if get_time() - logo_start_time >= 2.0:
        game_framework.change_mode(title_mode)
    pass

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    pass

def handle_events():
    events = get_events()