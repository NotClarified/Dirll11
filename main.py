from pico2d import open_canvas, delay, close_canvas
import play_mode

open_canvas()
play_mode.init()
while play_mode.running:
    play_mode.handle_events()
    play_mode.update()
    play_mode.draw()
    play_mode.draw()
    delay(0.01)
play_mode.finish()
close_canvas()