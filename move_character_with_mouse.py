from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

def handle_events():
    global running
    global arrow_x, arrow_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            arrow_x, arrow_y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            click_point.append((event.x, TUK_HEIGHT - 1 - event.y))
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def draw_arrows():
    global click_point
    for p in click_point:
        arrow.draw(p[0], p[1])
    pass

def move_character():
    global x, y, click_point

    if (len(click_point) > 0):
        point_x, point_y = click_point[0]
    else:
        point_x, point_y = x, y

    t = 0.03
    x = (1 - t) * x + t * point_x
    y = (1 - t) * y + t * point_y

    dis = math.sqrt((point_x - x) ** 2 + (point_y - y) ** 2)
    if dis < 5:
        if (len(click_point) > 0):
            click_point.pop(0)

    pass

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hide_cursor()
click_point = []
arrow_x, arrow_y = 0, 0

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    move_character()

    draw_arrows()
    arrow.draw(arrow_x, arrow_y)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

    update_canvas()

    frame = (frame + 1) % 8
    handle_events()
    delay(0.01)

close_canvas()




