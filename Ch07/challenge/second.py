def second(values):
    top, second = values[0], values[1]
    for value in values[2:]:
        if value > top:
            top, second = value, top
        elif value > second:
            second = value
    return second
