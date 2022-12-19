def on_forever():
    if input.pin_is_pressed(TouchPin.P0):
        basic.show_icon(IconNames.CHESSBOARD)
    else:
        basic.clear_screen()
basic.forever(on_forever)
