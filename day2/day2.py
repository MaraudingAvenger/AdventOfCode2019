initial_input = open('day2.txt','r').read()


def one(iterable, curr_pos):
    assert iterable[curr_pos] == 1, "current position is not a oneCode"
    iterable[
        get_value(iterable, curr_pos+3)
    ] = iterable[
        get_value(iterable, curr_pos+1)
    ] + iterable[
        get_value(iterable, curr_pos+2)
    ]
    return True


def two(iterable, curr_pos):
    assert iterable[curr_pos] == 2, "current position is not a twoCode"
    iterable[
        get_value(iterable, curr_pos+3)
    ] = iterable[
        get_value(iterable, curr_pos+1)
    ] * iterable[
        get_value(iterable, curr_pos+2)
    ]
    return True


def get_value(iterable, input_pos):
    return iterable[input_pos]


def print_iter(iterable, _curr_pos):
    #print(iterable[0])
    return False


func_dict = {
    1: one,
    2: two,
    99: print_iter
}


def gen_input(initial_input):
    return [int(item.strip()) for item in initial_input.split(',')]


def run_once(iterable):
    go = True
    i = 0
    while go:
        go = func_dict[iterable[i]](iterable, i)
        i += 4


def find_value():
    for noun in range(0, 99):
        for verb in range(0, 99):
            iterable = gen_input(initial_input)
            iterable[1] = noun
            iterable[2] = verb
            try:
                run_once(iterable)
            except Exception as e:
                print(e)
            if iterable[0] == 19690720:
                print("noun =", noun)
                print("verb =", verb)
                break

find_value()
