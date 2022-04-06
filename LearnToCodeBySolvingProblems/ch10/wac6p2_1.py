lights, flick = map(int, input().split())
state = map(int, input().split())
flicks = map(int, input().split())
state = list(state)
flicks = list(flicks)
sec = 0
on = state.count(1)
#print(state)
if on == 0:
    print(0)
else:
    while sec < flick and sec < on:
        if state[flicks[sec] - 1] == 1:
            state[flicks[sec] - 1] = 0
            on -= 1
        else:
            state[flicks[sec] - 1] = 1
            on += 1
        sec += 1
        #print(state, sec, on)
    if on < sec:
        print(sec)
    else:
        print(on)