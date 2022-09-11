def step2_umbrella():
    print(
        'Вообще-то утки ходят без зонтов, даже маляры. На то они и утки?'
    )

def step2_no_umbrella():
    print(
        'Утки маляры ходят в шапках, им зонты не нужны'
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