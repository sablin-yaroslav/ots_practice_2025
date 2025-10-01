import turtle


def perform_switch_case(state, t, turn):
    x = round(t.position()[0] / 10)
    y = round(t.position()[1] / 10)
    num_turns = 5

    if state == "DOWN":
        t.forward(10)  # Перемещение

        if round(t.position()[1]/10) <= turn + 1:
            state = "LEFT"
            t.setheading(180)  # Разворот влево
            return state, turn
        return state, turn
    if state == "RIGHT":
        t.forward(10)  # Перемещение

        if round(t.position()[0]/10) >= num_turns - turn:
            state = "DOWN"
            t.setheading(270)  # Разворот вниз
            return state, turn
        return state, turn
    if state == "LEFT":
        t.forward(10)  # Перемещение

        if round(t.position()[0]/10) <= turn + 1:
            state = "UP"
            turn = turn + 1  # Начало нового витка
            t.setheading(90)  # Разворот вверх
            return state, turn
        return state, turn
    if state == "INIT":

        if True:
            state = "UP"
            t.setheading(90)  # Разворот вверх
            turn = turn - 1  # Обнуление
            return state, turn
        return state, turn
    if state == "UP":
        t.forward(10)  # Перемещение

        if round(t.position()[1]/10) >= num_turns - turn and not(turn >= num_turns - 3):
            state = "RIGHT"
            t.setheading(0)  # Разворот вправо
            return state, turn
        if turn >= num_turns - 3:
            state = "STOP"
            return state, turn
        return state, turn
    return state, turn


def draw():
    start_state = "INIT"
    end_state = "STOP"
    curr_state = start_state
    t = turtle.Turtle()
    t.speed(0)
    turn = 1

    while curr_state != end_state:
        curr_state, turn = perform_switch_case(curr_state, t, turn)
    turtle.done()


if  __name__ == "__main__":
    draw()