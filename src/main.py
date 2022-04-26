def coprime_apparitions(sir, character, no):
    global max_len

    if len(sir) > max_len:
        raise Exception('String length too big')
    if no <= 1:
        raise Exception('Invalid number')
    if not character.islower():
        raise Exception('Invalid character')

    apparitions = 0
    for c in sir:
        if c == character:
            apparitions += 1

    if apparitions == 0:
        raise Exception('0 apparitions')

    if no > apparitions:
        lower = apparitions
    else:
        lower = no

    div = 2
    while div <= lower:
        if apparitions % div == 0 and no % div == 0:
            return False
        div += 1

    return True


if __name__ == '__main__':
    max_len = 50
