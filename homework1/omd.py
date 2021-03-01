yes = ('да', 'Да', 'yes', 'Yes')
no = ('нет', 'Нет', 'no', 'No')


def ask_question(question, yes_answer, no_answer):
    print(question)
    answer = ''
    while answer not in yes and answer not in no:
        answer = input("Введите ваш ответ (да/нет): ")
    if answer in yes:
        print(yes_answer)
    else:
        print(no_answer)
    print()


def start_quest():
    ask_question('Утка-маляр решила сходить погулять. Взять ей зонтик?',
                 'Лишним не будет, вдруг пойдет дождь',
                 'Ну и правильно, нечего таскать его в руках(лапах)')

    ask_question('Недавно утка-маляр познакомилась с селезнем-штукатуром. Позвать его на прогулку?',
                 'Конечно, так будет веселее, может что-то из этого и получится',
                 'Да зачем он нам нужен, лучше погрузиться в свои мысли')

    ask_question('Утка-маляр вышла на улицу, но спустя некоторое время ей стало прохладно. '
                 'Рядом как раз оказался торговый центр. Зайти в него?',
                 'А тут гораздо теплее, еще и можно присмотреть себе что-то',
                 'Можно же просто ускорить шаг, так и теплее и немного разомнешься')

    ask_question('Наша героиня уже долго гуляет и проголодалась. Зайти в кафе?',
                 'Так гораздо лучше. Здесь тепло и вкусно',
                 'Лучше сэкономить, а дома приготовить что-то вкусненькое')

    ask_question('По дороге домой к утке начали докапываться вороны-гопники. Убежать?',
                 'Естественно, утка еще нужна нам живой и здоровой',
                 'Пфф, конечно нет, у утки же есть травмат, она сама до кого угодно докопается')


if __name__ == '__main__':
    start_quest()
