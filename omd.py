import winsound


def step2_umbrella():
    print(
        'Чтобы взять зонтик, утке надо сильно постараться.А когда утки стараются, '
        'они крякают'
    )
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 1000  # Set Duration To 1000 ms == 1 second

    winsound.Beep(frequency, duration)
    winsound.Beep(frequency, duration)
    winsound.Beep(frequency, duration)


def step2_no_umbrella():
    print(
        'И правильно, после бара, всё нипочём! Еще, чего доброго, его и забыть можно. '
    )


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()
