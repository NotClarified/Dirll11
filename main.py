from pico2d import open_canvas, delay, close_canvas
# import logo_mode as start_mode
import game_framework
#import play_mode as start_mode
import title_mode as start_mode # title_mode를 import하되 start_mode로 취급하라


open_canvas()
game_framework.run(start_mode)
close_canvas()