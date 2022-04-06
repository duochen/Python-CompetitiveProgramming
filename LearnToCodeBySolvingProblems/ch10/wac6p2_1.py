lights, flick = map(int, input().split())
light_state = map(int, input().split())
flicks = map(int, input().split())
light_state = list(light_state)
flicks = list(flicks)
second = 0
lights_on = light_state.count(1)

if lights_on == 0:
    print(0)
else:
    while second < flick and second < lights_on:
        if light_state[flicks[second] - 1] == 1:
            light_state[flicks[second] - 1] = 0
            lights_on -= 1
        else:
            light_state[flicks[second] - 1] = 1
            lights_on += 1
        second += 1

    if lights_on < second:
        print(second)
    else:
        print(lights_on)